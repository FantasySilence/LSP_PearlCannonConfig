# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Descript: 这个模块用于抛射配置       #
# =================================== #
import json
import numpy as np
import pandas as pd
from src.common.const import *
from src.common.filesio import FilesIO
from src.modules.direction import Directions
from src.modules.tuning import TNTNumberAdjustment


class TNTConfigForEjection:

    """
    计算抛射状态下，TNT的配置
    """
    
    @staticmethod
    def config(x_target: int, z_target: int) -> tuple[str, pd.DataFrame]:

        """
        x_target, z_target：目的地坐标
        """
        
        # ------ 读取设置 ------ #
        with open(FilesIO.load_json("settings.json"), "r") as f:
            settings = json.load(f)

        # ------ 判断方向 ------ #
        direction, direc_matrix = Directions.judge(x_target, z_target)

        # ------ 计算TNT数量 ------ #
        tick = 100
        preliminary_results = {}
        final_result = {}
        while tick <= 300:

            # 计算达到目的地所需动量
            px = (x_target - settings["INIT_POSITION"]["X"]) / (100 * (1 - 0.99 ** tick))
            py = (128 - MOTION_FOR_EJECTIONS["Y_INIT_POSITION"] + 3 * tick) / (100 * (1 - 0.99 ** tick)) - 3 
            pz = (z_target - settings["INIT_POSITION"]["Z"]) / (100 * (1 - 0.99 ** tick))

            # 生成求解TNT数量的方程组
            P_xz = direc_matrix.dot(np.array([px, pz]))
            coefs = np.array([[1, 1], P_xz])
            consts = np.array([
                (py - MOTION_FOR_EJECTIONS["Y_INIT_MOTION"]) / MOTION_FOR_EJECTIONS["Y_MOTION"],
                0
            ])

            # 求解
            x = pd.Series(
                np.linalg.solve(coefs, consts)
            ).map(lambda x: round(x)).to_numpy()

            # 将合适的解存入初步结果等待进一步调整
            if x[0] <= settings["MAX_TNT"] and x[1] <= settings["MAX_TNT"]:
                preliminary_results[tick] = x
        
            tick += 1
        
        # ------ 对初步结果进行进一步修正 ------ #
        for tick in preliminary_results.keys():
            # 生成所有的组合
            tuning_range = TNTNumberAdjustment.generate(
                preliminary_results[tick], modifiers=range(-10, 11)
            )
            sub_res = []
            # 每个组合计算误差取最小
            for comb in tuning_range:
                # 计算XYZ轴动量
                motion = MOTION_FOR_EJECTIONS["XZ_MOTION"] * direc_matrix.dot(comb)
                y_motion = MOTION_FOR_EJECTIONS["Y_MOTION"] *\
                            sum(comb) + MOTION_FOR_EJECTIONS["Y_INIT_MOTION"]
                # 计算落点
                xt = settings["INIT_POSITION"]["X"] + 100 * motion[0] * (1 - 0.99 ** tick)
                yt = MOTION_FOR_EJECTIONS["Y_INIT_POSITION"] + 100 * (y_motion + 3) * (1 - 0.99 ** tick) - 3 * tick
                zt = settings["INIT_POSITION"]["Z"] + 100 * motion[1] * (1 - 0.99 ** tick)

                # 计算误差
                error = np.sqrt((xt - x_target) ** 2 + (zt - z_target) ** 2)
                sub_res.append([error, comb])
            final_result[tick] = sorted(sub_res, key=lambda x: x[0])[0]
        
        # ------ 生成输出结果的Dataframe ------ #
        output = pd.DataFrame()
        output["距离偏移"] = [i[0] for i in final_result.values()]
        output["飞行时间"] = final_result.keys()
        output["蓝色TNT数量"] = [i[1][0] for i in final_result.values()]
        output["红色TNT数量"] = [i[1][1] for i in final_result.values()]
        output["TNT总数量"] = output["蓝色TNT数量"] + output["红色TNT数量"]
        output.sort_values(by="距离偏移", inplace=True)

        # ------ 返回结果 ------ #
        return direction, output
