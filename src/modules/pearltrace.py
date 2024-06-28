# ========================================= #
# @Author: Fantasy_Silence                  #
# @Time: 2024-06-26                         #
# @IDE: Visual Studio Code & PyCharm        #
# @Python: 3.9.7                            #
# ========================================= #
# @Descript: 这个模块用于实现珍珠轨迹的模拟    #
# ========================================= #
import json
import pandas as pd
from typing import Literal
from src.common.const import *
from src.common.filesio import FilesIO


class PearlPathTracing:

    """
    珍珠落点位置的预报
    """

    @staticmethod
    def generate(
        x_motion: float, y_motion: float, z_motion: float, max_ticks: int,
        mode: Literal["flat", "eject"] = "flat"
    ) -> pd.DataFrame:
        
        """
        x_motion, y_motion, z_motion: 珍珠起始动量
        mode: 珍珠出射方式(平射或抛射), 默认为平射
        """

        # ------ 读取设置 ------ #
        with open(FilesIO.load_json("settings.json"), "r") as f:
            settings = json.load(f)
        
        # ------ 珍珠初始位置 ------ #
        x = x_init = settings["INIT_POSITION"]["X"]
        z = z_init = settings["INIT_POSITION"]["Z"]
        if mode == "flat":
            y = y_init = MOTION_FOR_FLAT_FIRE["Y_INIT_POSITION"]
        if mode == "eject":
            y = y_init = MOTION_FOR_EJECTIONS["Y_INIT_POSITION"]

        # ------ 初始化存储结果的列表 ------ #
        PearlLocation = [[0, x_init, y_init, z_init]]
        tick = 0

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
