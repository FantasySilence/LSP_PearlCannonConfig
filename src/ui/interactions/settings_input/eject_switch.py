# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 抛射选项的按钮功能配置  #
# =================================== #

def eject_switch_func(self) -> None:

    """
    抛射选项的按钮功能配置
    """

    entry_list = [
        self.y_eject_input,
        self.init_y_motion_eject_input,
        self.y_motion_eject_input,
        self.xz_init_motion_eject_input,
    ]

    if self.eject_switch.get() == "normal":
        for entry in entry_list:
            entry.configure(state="normal")
    else:
        for entry in entry_list:
            entry.configure(state="readonly")
