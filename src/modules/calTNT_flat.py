# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Descript: 这个模块用于平射配置       #
# =================================== #
import numpy as np
import pandas as pd
from src.common.const import *
from src.modules.direction import Directions
from src.modules.tuning import TNTNumberAdjustment


class TNTConfigForFlat:

    """
    计算平射状态下，TNT的配置
    """

    @staticmethod
    def config(
        x_target: int, z_target: int, 
        x_0: float, z_0: float, max_TNT: int=None, settings: dict=None
    ) -> tuple[str, pd.DataFrame]:

        """
        x0, z0：炮口初始位置
        x_target, z_target：目的地坐标
        """
        
        # ------ 判断方向 ------ #
        direction, direc_matrix = Directions.judge(x_target, z_target, x_0, z_0)

        # ------ 计算TNT数量 ------ #
        tick = 1
        preliminary_results = {}
        final_result = {}
        while tick <= 300:

            # 计算达到目的地所需动量
            b = np.array([
                (x_target - x_0)/(100 * (1 - 0.99 ** tick)), 
                (z_target - z_0)/(100 * (1 - 0.99 ** tick)),
            ])

            # 求解
            x = pd.Series(
                np.linalg.solve(
                    settings["MOTION_FOR_FLAT_FIRE"]["XZ_MOTION"] * direc_matrix, b
                )
            ).map(lambda x: round(x)).to_numpy()

            # 将合适的解存入初步结果等待进一步调整
            if max_TNT is not None:
                if 0 <= x[0] <= max_TNT and 0 <= x[1] <= max_TNT:
                    preliminary_results[tick] = x
            else:
                if x[0] <= settings["MAX_TNT"] and x[1] <= settings["MAX_TNT"]:
                    preliminary_results[tick] = x
        
            tick += 1
        
        # ------ 对初步结果进行进一步修正 ------ #
        for tick in preliminary_results.keys():

            # 生成所有的组合
            tuning_range = TNTNumberAdjustment.generate(preliminary_results[tick])
            sub_res = []

            # 每个组合计算误差取最小
            for comb in tuning_range:

                # 计算XZ轴动量
                motion = settings["MOTION_FOR_FLAT_FIRE"]["XZ_MOTION"] * direc_matrix.dot(comb)
                
                # 计算落点
                xt = x_0 + 100 * motion[0] * (1 - 0.99 ** tick)
                zt = z_0 + 100 * motion[1] * (1 - 0.99 ** tick)
                
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

        # ------ 返回结果 ------ #
        return direction, output
    