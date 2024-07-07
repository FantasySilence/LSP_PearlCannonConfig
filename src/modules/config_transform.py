# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-30                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 翻译信息，便于玩家配置  #
# =================================== #
import numpy as np


class ConfigInfoTransform:

    """
    将配置器计算出的TNT数量翻译为珍珠炮阵列能看懂的信息
    方便玩家配置主炮或者返程炮
    """

    @staticmethod
    def translate(
        blue_TNT: int, red_TNT: int, settings: dict=None
    ) -> tuple[str, str]:

        """
        blue_TNT：蓝色TNT数量，例如：913
        red_TNT：红色TNT数量，例如：612
        输出：(如果单个阵列数为260)
        蓝色TNT数量：913 = 520 + 260 + 80 + 40 + 10 + 2 + 1
        红色TNT数量：612 = 520 + 80 + 10 + 2
        """

        TNT_num = np.array([blue_TNT, red_TNT])

        # ------ 数量矩阵与二进制单位数矩阵的点乘 ------ #
        TNT_vector = np.array([settings["MAX_TNT_UNIT"], 10, 1]).reshape(3, 1)
        bin_unit = np.array([
            [16, 8, 4, 2, 1],
            [16, 8, 4, 2, 1],
            [16, 8, 4, 2, 1],
        ])
        unit = TNT_vector * bin_unit

        # ------ 计算TNT当量中单个阵列TNT数, 10, 1的数量 ------ #
        rest_num_of_tnt_unit = TNT_num // settings["MAX_TNT_UNIT"]
        rest_num_of_10 = TNT_num % settings["MAX_TNT_UNIT"] // 10
        rest_num_of_1 = TNT_num % settings["MAX_TNT_UNIT"] % 10
        rest_num_matrix = np.array(
            [rest_num_of_tnt_unit, rest_num_of_10, rest_num_of_1]
        )

        # ------ 生成一个矩阵用于存储二进制结果 ------ #
        blue_num_matrix = np.zeros((3, 5))
        red_num_matrix = np.zeros((3, 5))

        # ------ 遍历填入，第i行为第i个数量对应的二进制码 ------ #
        for i in range(3):
            blue_num_matrix[i] = np.array(
                list(map(int, bin(rest_num_matrix[i, 0])[2:].zfill(5)))
            )

        for i in range(3):
            red_num_matrix[i] = np.array(
                list(map(int, bin(rest_num_matrix[i, 1])[2:].zfill(5)))
            )
        
        # ------ 计算TNT数量 ------ #
        blue_num_matrix = blue_num_matrix * unit
        red_num_matrix = red_num_matrix * unit

        # ------ 遍历矩阵，生成结果字符串 ------ #
        blue_tnt_res_str = "%d = " % blue_TNT
        for i in range(blue_num_matrix.shape[0]):
            for j in range(blue_num_matrix.shape[1]):
                if blue_num_matrix[i, j] != 0:
                    blue_tnt_res_str += "%d + " % blue_num_matrix[i, j]
        blue_tnt_res_str = blue_tnt_res_str[:-2]

        red_tnt_res_str = "%d = " % red_TNT
        for i in range(red_num_matrix.shape[0]):
            for j in range(red_num_matrix.shape[1]):
                if red_num_matrix[i, j] != 0:
                    red_tnt_res_str += "%d + " % red_num_matrix[i, j]
        red_tnt_res_str = red_tnt_res_str[:-2]

        return blue_tnt_res_str, red_tnt_res_str
        