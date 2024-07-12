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
from tkinter import messagebox
from ttkbootstrap.constants import *
from src.common.path_utils import *
from tkinter.filedialog import askopenfilename
from src.common.input_validation import validate_number


class SettingsFrame(ttk.Frame):

    def __init__(self, master, lang) -> None:
        
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

        # ------ 读取语言设置 ------ #
        self.lang = lang
        with open(
            resource_path("resources/languages/languages.json"), 
            mode="r", encoding="utf-8"
        ) as f:
            self.LANGUAGE = json.load(f)
        
        # ------ 创建页面 ------ #
        self.create_page()
    
    def create_page(self) -> None:

        """
        创建界面
        """

        # ------ 输入珍珠初始位置的x坐标 ------ #
        self.x0_label = ttk.Label(
            master=self.frame, 
            text=self.LANGUAGE[self.lang]["settings_frame"]["default_x"], 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.x0_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        x0_input = ttk.Entry(
            master=self.frame, textvariable=self.x0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        x0_input.grid(row=0, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入珍珠初始位置的z坐标 ------ #
        self.z0_label = ttk.Label(
            master=self.frame,
            text=self.LANGUAGE[self.lang]["settings_frame"]["default_z"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.z0_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        z0_input = ttk.Entry(
            master=self.frame, textvariable=self.z0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        z0_input.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

        # ------ 输入最大TNT数量 ------ #
        self.tnt_input_label = ttk.Label(
            master=self.frame,
            text=self.LANGUAGE[self.lang]["settings_frame"]["default_max_tnt"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.tnt_input_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        tnt_input = ttk.Entry(
            master=self.frame, textvariable=self.max_tnt_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        tnt_input.grid(row=2, column=1, padx=5, pady=5, sticky=EW)

        # ------ 应用按钮 ------ #
        self.apply_button = ttk.Button(
            master=self.frame,
            text=self.LANGUAGE[self.lang]["settings_frame"]["button_apply"],
            command=self.apply_settings,
            bootstyle=(PRIMARY, LIGHT),
        )
        self.apply_button.grid(
            row=3, column=0, padx=5, pady=5, sticky=EW, columnspan=2
        )

        # ------ 导入设置文件按钮 ------ #
        self.upload_buttons = ttk.Button(
            master=self.frame,
            text=self.LANGUAGE[self.lang]["settings_frame"]["button_import"],
            command=self.upload_button,
            bootstyle=(INFO, LIGHT),
        )
        self.upload_buttons.grid(
            row=4, column=0, padx=5, pady=5, sticky=EW, columnspan=2
        )


    def apply_settings(self) -> None:

        """
        应用设置
        """

        # ------ 读取现有的设置并进行修改 ------ #
        settings = load_settings()
        try:
            if self.x0_input.get() != '':
                settings["INIT_POSITION"]["X"] = float(self.x0_input.get())
            if self.z0_input.get() != '':
                settings["INIT_POSITION"]["Z"] = float(self.z0_input.get())
            if self.max_tnt_input.get() != '':
                settings["MAX_TNT"] = int(self.max_tnt_input.get())
            # 出错时显示弹窗
        except Exception:
            messagebox.showerror(
                title=self.LANGUAGE[self.lang]["error_frame"]["title"], 
                message=self.LANGUAGE[self.lang]["error_frame"]["error_message"]
            )
            return

        # ------ 将修改后的设置进行保存 ------ #
        save_settings(settings)

        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def upload_button(self) -> None:

        """
        导入设置
        """

        # ------ 导入文件窗口 ------ #
        file_path = askopenfilename(
            title="导入设置",
            filetypes=[("JSON files", "*.json")]
        )
        if not file_path:
            return

        # ------ 将导入的文件内容写入应用的设置文件中 ------ #
        try:
            with open(file_path, mode="r") as file:
                settings = json.load(file)
            save_settings(settings)
            
            # ------ 重启应用，设置生效 ------ #
            python = sys.executable
            os.execl(python, python, *sys.argv)

        except Exception as e:
            print(file_path)
            messagebox.showerror("Error", f"Failed to import settings: {e}")
        