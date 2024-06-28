# ========================================= #
# @Author: Fantasy_Silence                  #
# @Time: 2024-06-26                         #
# @IDE: Visual Studio Code & PyCharm        #
# @Python: 3.9.7                            #
# ========================================= #
# @Descript: 这个模块用于实现落点方向的判断    #
# ========================================= #
import json
import numpy as np
from src.common.filesio import FilesIO


class Directions:
    
    """
    方向判断
    """

    @staticmethod
    def judge(x1: float, z1: float) -> tuple[str, np.ndarray]:

        """
        x1, z1: 目标位置
        """

        # ------ 读取设置 ------ #
        with open(FilesIO.load_json("settings.json"), "r") as f:
            settings = json.load(f)

        # ------ 平移坐标原点至炮口坐标 ------ #
        destination = np.array([
            x1 - settings["INIT_POSITION"]["X"], 
            z1 - settings["INIT_POSITION"]["Z"]
        ])

        # ------ 定义旋转矩阵，将目的地坐标顺时针旋转45度 ------ #
        rotate_matrix = np.array([
            [np.cos(np.pi / 4), -np.sin(np.pi / 4)],
            [np.sin(np.pi / 4), np.cos(np.pi / 4)],
        ]).T
        rotated_destination = np.dot(rotate_matrix, destination)
        
        # ------ 判断旋转后的坐标所在方位 ------ #
        if rotated_destination[0] >= 0 and rotated_destination[1] < 0:
            return "east", np.array([[1, 1], [-1, 1]])
        if rotated_destination[0] > 0 and rotated_destination[1] >= 0:
            return "south", np.array([[1, -1], [1, 1]])
        if rotated_destination[0] <= 0 and rotated_destination[1] > 0:
            return "west", np.array([[-1, -1], [-1, 1]])
        if rotated_destination[0] < 0 and rotated_destination[1] <= 0:
            return "north", np.array([[1, -1], [-1, -1]])
    