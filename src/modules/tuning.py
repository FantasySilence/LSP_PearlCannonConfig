# ========================================= #
# @Author: Fantasy_Silence                  #
# @Time: 2024-06-26                         #
# @IDE: Visual Studio Code & PyCharm        #
# @Python: 3.9.7                            #
# ========================================= #
# @Descript: 这个模块用于实现配置数量的微调    #
# ========================================= #
import itertools
import numpy as np


class TNTNumberAdjustment:
    
    """
    生成TNT数量调整的结果
    """

    @staticmethod
    def generate(
        tnt_num_array: np.ndarray, modifiers: range=range(-2, 3)
    ) -> np.ndarray:

        """
        tnt_num_array: 生成的TNT数量配置信息
        modifiers: 用于调整TNT数量的修正值, 默认为 range(-2, 3)
        """

        # ------ 生成所有组合 ------ #
        all_combinations = list(itertools.product(modifiers, repeat=len(tnt_num_array)))

        # ------ 生成所有可能的结果 ------ #
        all_results = np.array([
            [x + y for x, y in zip(tnt_num_array, comb)] for comb in all_combinations
        ])

        # ------ 返回所有可能的结果 ------ #
        return all_results
