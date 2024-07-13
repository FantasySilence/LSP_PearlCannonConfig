# ============================================= #
# @Author: Fantasy_Silence                      #
# @Time: 2024-07-13                             #
# @IDE: Visual Studio Code & PyCharm            #
# @Python: 3.9.7                                #
# ============================================= #
# @Description: "默认值设置"按钮的功能函数        #
# ============================================= #
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.ui.frames.settings import SettingsFrame


def func_upload_button(cls) -> None:

    """
    "默认值设置"按钮的功能
    """

    # ------ 如果已经存在一个窗口，先销毁它 ------ #
    if cls.settings_window:
        cls.settings_window.destroy()

    # ------ 创建弹窗 ------ #
    cls.settings_window = ttk.Toplevel(cls.input_frame)
    cls.settings_window.title(" ")
    
    # ------ 显示在主窗口的靠中心位置 ------ #
    x = cls.input_frame.winfo_rootx() + cls.input_frame.winfo_width() // 2
    y = cls.input_frame.winfo_rooty()
    cls.settings_window.geometry(f"+{x}+{y}")

    # ------ 创建页面 ------ #
    settings_frame = SettingsFrame(cls.settings_window, cls.lang)
    cls.sub_pages.append(settings_frame)
    settings_frame.pack(fill=BOTH, expand=YES)
