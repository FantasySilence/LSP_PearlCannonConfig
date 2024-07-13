# ======================================== #
# @Author: Fantasy_Silence                 #
# @Time: 2024-07-13                        #
# @IDE: Visual Studio Code & PyCharm       #
# @Python: 3.9.7                           #
# ======================================== #
# @Description: "珍珠模拟"按钮的功能函数     #
# ======================================== #

def func_simulation_button(cls) -> None:

    """
    "珍珠模拟"按钮的功能
    """

    cls.res_page.load_pearl_trace(
        float(cls.x0_input.get()), float(cls.z0_input.get()),
        cls.direction.get(), cls.angel.get(), settings=cls.settings
    )
