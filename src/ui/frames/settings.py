# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-30                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 设置界面               #
# =================================== #
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO
from src.ui.frames.previews import PreviewFrame
from src.ui.frames.settings_input import AdvancedSettingInput


class AdvancedSettings(ttk.Frame):

    """
    高级设置界面
    """

    def __init__(self, master, lang) -> None:

        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        self.pack_propagate(False)
        self.grid_propagate(False)

        # ------ 读取语言设置 ------ #
        self.lang = lang

        # ------ 创建页面 ------ #
        self.create_page()
    

    def create_page(self):

        """
        创建高级设置页面
        """

        # ------ 创建主界面 ------ #
        self.main_frame = ttk.Frame(self, bootstyle=LIGHT)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=3)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=YES)
        # 向主容器中添加结果预览子容器
        preview = PreviewFrame(self.main_frame, lang=self.lang, width=650, height=700)
        preview.grid(row=0, column=1, sticky=NSEW)
        # 向主容器中添加用户输入子容器
        setting_input = AdvancedSettingInput(
            self.main_frame, preview, lang=self.lang, width=550, height=700
        )
        setting_input.grid(row=0, column=0, sticky=NSEW)
