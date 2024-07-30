# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 平射选项的按钮功能配置  #
# =================================== #

def flat_switch_func(cls) -> None:

    """
    平射选项的按钮功能配置
    """

    entry_list = [
        cls.y_flat_input,
        cls.init_y_motion_flat_input,
        cls.y_motion_flat_input,
        cls.xz_init_motion_flat_input,
    ]

    if cls.flat_switch.get() == "normal":
        for entry in entry_list:
            entry.configure(state="normal")
    else:
        for entry in entry_list:
            entry.configure(state="readonly")
