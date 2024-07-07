# ========================================= #
# @Author: Fantasy_Silence                  #
# @Time: 2024-06-26                         #
# @IDE: Visual Studio Code & PyCharm        #
# @Python: 3.9.7                            #
# ========================================= #
# @Descript: 这个模块用于实现珍珠轨迹的模拟    #
# ========================================= #
import numpy as np
import pandas as pd
from typing import Literal
from src.common.const import *


class PearlPathTracing:

    """
    珍珠落点位置的预报
    """

    @staticmethod
    def generate(
        x0: float, z0: float, tnt_num: np.ndarray, 
        direction: Literal["east", "west", "north", "south"], 
        max_ticks: int, mode: Literal["flat", "eject"] = "flat",
        settings: dict = None
    ) -> pd.DataFrame:
        
        """
        x0, z0：炮口初始位置
        tnt_num：蓝色TNT与红色TNT数量
        direction：方向
        max_ticks: 最大tick数
        mode: 珍珠出射方式(平射或抛射), 默认为平射
        """

        # ------ 珍珠初始位置 ------ #
        x = x_init = x0
        z = z_init = z0
        if mode == "flat":
            y = y_init = settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_POSITION"]
        if mode == "eject":
            y = y_init = settings["MOTION_FOR_EJECTIONS"]["Y_INIT_POSITION"]

        # ------ 初始化存储结果的列表 ------ #
        PearlLocation = [[0, x_init, y_init, z_init]]
        tick = 0

        # ------ 生成方向矩阵 ------ #
        if direction == "east":
            direc_matrix = np.array([[1, 1], [-1, 1]])
        if direction == "west":
            direc_matrix = np.array([[-1, -1], [-1, 1]])
        if direction == "north":
            direc_matrix = np.array([[1, -1], [-1, -1]])
        if direction == "south":
            direc_matrix = np.array([[1, -1], [1, 1]])
        
        # ------ 计算三轴动量 ------ #
        if mode.lower() == "flat":
            motion = settings["MOTION_FOR_FLAT_FIRE"]["XZ_MOTION"] * direc_matrix.dot(tnt_num)
            x_motion, z_motion = motion[0], motion[1]
            y_motion =  y_motion = settings["MOTION_FOR_FLAT_FIRE"]["Y_MOTION"] *\
                                sum(tnt_num) + settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_MOTION"]
        if mode.lower() == "eject":
            motion = settings["MOTION_FOR_EJECTIONS"]["XZ_MOTION"] * direc_matrix.dot(tnt_num)
            x_motion, z_motion = motion[0], motion[1]
            y_motion =  y_motion = settings["MOTION_FOR_EJECTIONS"]["Y_MOTION"] *\
                                sum(tnt_num) + settings["MOTION_FOR_EJECTIONS"]["Y_INIT_MOTION"]
            
        # ------ 计算珍珠途径位置 ------ #
        while tick < max_ticks:
            tick = tick + 1
            x = x + x_motion
            y = y + y_motion
            z = z + z_motion
            x_motion = 0.99 * x_motion
            y_motion = 0.99 * y_motion - 0.03
            z_motion = 0.99 * z_motion
            PearlLocation.append([tick, x, y, z])

        # ------ 返回结果 ------ #
        PearlLocationFrame = pd.DataFrame(
            PearlLocation, columns=['time','x','y','z']
        )
        return PearlLocationFrame
