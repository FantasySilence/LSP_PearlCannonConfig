# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-30                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 设置界面               #
# =================================== #
import os
import sys
import json
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *
from src.common.path_utils import resource_path
from src.common.input_validation import validate_number


class SettingsFrame(ttk.Frame):

    def __init__(self, master) -> None:
        
        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        # 珍珠初始位置
        self.x0_input = ttk.StringVar()
        self.z0_input = ttk.StringVar()
        # 最大TNT数量
        self.max_tnt_input = ttk.StringVar()
        # 存放输入框的根容器
        self.frame = ttk.Frame(
            self, padding=(10, 10)
        )
        self.frame.pack(fill=BOTH, expand=YES)
        self.validation_func = self.frame.register(validate_number)
        self.pack(fill=BOTH, expand=YES)
        self.create_page()
    
    def create_page(self) -> None:

        """
        创建界面
        """

        # ------ 输入珍珠初始位置的x坐标 ------ #
        x0_label = ttk.Label(
            master=self.frame, 
            text="输入珍珠默认初始x位置:", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x0_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        x0_input = ttk.Entry(
            master=self.frame, textvariable=self.x0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        x0_input.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入珍珠初始位置的z坐标 ------ #
        z0_label = ttk.Label(
            master=self.frame,
            text="输入珍珠默认初始z位置:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z0_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        z0_input = ttk.Entry(
            master=self.frame, textvariable=self.z0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        z0_input.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入最大TNT数量 ------ #
        tnt_input_label = ttk.Label(
            master=self.frame,
            text="输入默认最大TNT数量:",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        tnt_input_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        tnt_input = ttk.Entry(
            master=self.frame, textvariable=self.max_tnt_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        tnt_input.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

        # ------ 应用按钮 ------ #
        apply_button = ttk.Button(
            master=self.frame,
            text="应用",
            command=self.apply_settings,
            bootstyle=(PRIMARY, LIGHT),
        )
        apply_button.grid(
            row=3, column=0, padx=5, pady=5, sticky=EW, columnspan=2
        )

    def apply_settings(self) -> None:

        """
        应用设置
        """

        # ------ 读取现有的设置并进行修改 ------ #
        with open(
            resource_path("resources/settings/settings.json"), mode="r"
        ) as file:
            settings = json.load(file)
            if self.x0_input.get() != '':
                settings["INIT_POSITION"]["X"] = float(self.x0_input.get())
            if self.z0_input.get() != '':
                settings["INIT_POSITION"]["X"] = float(self.z0_input.get())
            if self.max_tnt_input.get() != '':
                settings["MAX_TNT"] = int(self.max_tnt_input.get())

        # ------ 将修改后的设置进行保存 ------ #
        with open(
            resource_path("resources/settings/settings.json"), mode="w"
        ) as files:    
            json.dump(settings, files, indent=4)

        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)
