# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 用户在设置界面的输入    #
# =================================== #
import json
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO
from src.ui.frames.previews import PreviewFrame
from src.common.input_validation import validate_number
from src.ui.interactions.settings_input.check_settings import check_func
from src.ui.interactions.settings_input.import_settings import import_func
from src.ui.interactions.settings_input.flat_switch import flat_switch_func
from src.ui.interactions.settings_input.preview_settings import preview_func
from src.ui.interactions.settings_input.eject_switch import eject_switch_func


class AdvancedSettingInput(ttk.Frame):

    """
    输入界面
    """

    def __init__(self, master, res_frame: PreviewFrame, lang, *args, **kwargs) -> None:

        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master, *args, **kwargs)
        self.pack_propagate(False)
        self.grid_propagate(False)

        # ------ 读取语言设置 ------ #
        self.lang = lang
        with open(
            FilesIO.getLanguage("languages.json"), mode="r", encoding="utf-8"
        ) as f:
            self.LANGUAGE = json.load(f)

        # ------ 创建根页面 ------ #
        text = self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["settings_input_labelframe_text"]
        self.setting_input_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5), width=550
        )
        self.setting_input_frame.columnconfigure(0, weight=1)
        self.setting_input_frame.grid_propagate(False)
        self.setting_input_frame.pack(fill=BOTH, expand=YES)

        # ------ 输入框中的默认值 ------ #
        self.x0_input = ttk.StringVar(value="0")
        self.z0_input = ttk.StringVar(value="0")
        self.max_tnt_input = ttk.StringVar(value="0")
        self.tnt_per_unit = ttk.StringVar(value="0")

        self.y0_flat = ttk.StringVar(value="0")
        self.y_init_motion_f = ttk.StringVar(value="0")
        self.xz_flat = ttk.StringVar(value="0")
        self.y_flat_motion = ttk.StringVar(value="0")

        self.y0_eject = ttk.StringVar(value="0")
        self.y_init_motion_e = ttk.StringVar(value="0")
        self.xz_eject = ttk.StringVar(value="0")
        self.y_eject_motion = ttk.StringVar(value="0")

        self.values_to_input = [
            self.x0_input, self.z0_input, self.max_tnt_input, self.tnt_per_unit,
            self.y0_flat, self.y_init_motion_f, self.xz_flat, self.y_flat_motion,
            self.y0_eject, self.y_init_motion_e, self.xz_eject, self.y_eject_motion
        ]

        # ------ 创建多选按钮的相应值 ------ #
        self.flat_switch = ttk.StringVar(value="normal")
        self.eject_switch = ttk.StringVar(value="readonly")

        # ------ 最终存取的设置 ------ #
        self.final_settings = None
        self.res_frame = res_frame

        # ------ 设置验证函数 ------ #
        self.validation_func = self.setting_input_frame.register(validate_number)

        # ------ 创建页面 ------ #
        self.create_init_page()
        self.create_flat_settings_page()
        self.create_eject_page()
        self.create_button_page()
    

    def create_init_page(self) -> None:

        """
        创建珍珠初始位置等信息输入页面
        """

        # ------ 创建存放珍珠初始位置类输入框的容器 ------ #
        self.init_page = ttk.Frame(self.setting_input_frame, width=550, height=90)
        self.init_page.grid_propagate(False)
        self.init_page.grid(row=0, column=0, sticky=NSEW, pady=(0, 5))

        # ------ 珍珠初始坐标 ------ #
        self.origin_x_label = ttk.Label(
            master=self.init_page, 
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["default_x"], 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.origin_x_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.init_page, textvariable=self.x0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        x_input.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.origin_z_label = ttk.Label(
            master=self.init_page, 
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["default_z"], 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.origin_z_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.init_page, textvariable=self.z0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        z_input.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # ------ TNT阵列信息 ------ #
        self.max_tnt_label = ttk.Label(
            master=self.init_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["default_max_tnt"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.max_tnt_label.grid(row=0, column=2, padx=(10, 5), pady=5, sticky=W)
        max_tnt_input = ttk.Entry(
            master=self.init_page, textvariable=self.max_tnt_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        max_tnt_input.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        self.tnt_per_unit_label = ttk.Label(
            master=self.init_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["default_tnt_unit"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.tnt_per_unit_label.grid(row=1, column=2, padx=(10, 5), pady=5, sticky=W)
        tnt_per_unit_input = ttk.Entry(
            master=self.init_page, textvariable=self.tnt_per_unit, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        tnt_per_unit_input.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        
    def create_flat_settings_page(self) -> None:

        """
        创建平射参数设置输入界面
        """

        # ------ 创建平射参数设置界面 ------ #
        self.flat_settings_page = ttk.Frame(self.setting_input_frame, width=550, height=205)
        self.flat_settings_page.grid_propagate(False)
        self.flat_settings_page.grid(row=1, column=0, sticky=NSEW, pady=5)

        # ------ 创建一个多选按钮，激活这部分输入，平射默认激活 ------ #
        self.flat_settings_switch = ttk.Checkbutton(
            master=self.flat_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["flat"]["button_text"],
            bootstyle=(ROUND, TOGGLE),
            variable=self.flat_switch,
            onvalue="normal",
            offvalue="readonly",
            command=lambda: flat_switch_func(self)
        )
        self.flat_settings_switch.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # ------ 输入平射时珍珠炮Y坐标 ------ #
        self.y_flat_label = ttk.Label(
            master=self.flat_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["flat"]["default_y"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.y_flat_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.y_flat_input = ttk.Entry(
            master=self.flat_settings_page, state=self.flat_switch.get(),
            textvariable=self.y0_flat, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.y_flat_input.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入0个TNT配置下，珍珠开炮时具有的初始Y动量 ------ #
        self.init_y_motion_flat_label = ttk.Label(
            master=self.flat_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["flat"]["zero_TNT_y_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.init_y_motion_flat_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.init_y_motion_flat_input = ttk.Entry(
            master=self.flat_settings_page, state=self.flat_switch.get(),
            textvariable=self.y_init_motion_f, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.init_y_motion_flat_input.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入1个TNT配置下，珍珠开炮时具有的初始Y动量 ------ #
        self.y_motion_flat_label = ttk.Label(
            master=self.flat_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["flat"]["one_TNT_y_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.y_motion_flat_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.y_motion_flat_input = ttk.Entry(
            master=self.flat_settings_page, state=self.flat_switch.get(),
            textvariable=self.y_flat_motion, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.y_motion_flat_input.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入1个TNT配置下，珍珠开炮时具有的初始XZ动量 ------ #
        self.xz_init_motion_flat_label = ttk.Label(
            master=self.flat_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["flat"]["one_TNT_xz_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.xz_init_motion_flat_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.xz_init_motion_flat_input = ttk.Entry(
            master=self.flat_settings_page, state=self.flat_switch.get(),
            textvariable=self.xz_flat, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.xz_init_motion_flat_input.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    def create_eject_page(self) -> None:

        """
        创建抛射参数设置输入界面
        """

        # ------ 创建抛射参数设置界面 ------ #
        self.eject_settings_page = ttk.Frame(self.setting_input_frame, width=550, height=205)
        self.eject_settings_page.grid_propagate(False)
        self.eject_settings_page.grid(row=2, column=0, sticky=NSEW, pady=5)

        # ------ 创建一个多选按钮，激活这部分输入，抛射默认不激活 ------ #
        self.eject_settings_switch = ttk.Checkbutton(
            master=self.eject_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["eject"]["button_text"],
            bootstyle=(ROUND, TOGGLE),
            variable=self.eject_switch,
            onvalue="normal",
            offvalue="readonly",
            command=lambda: eject_switch_func(self)
        )
        self.eject_settings_switch.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # ------ 输入抛射时珍珠炮Y坐标 ------ #
        self.y_eject_label = ttk.Label(
            master=self.eject_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["eject"]["default_y"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.y_eject_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.y_eject_input = ttk.Entry(
            master=self.eject_settings_page, state=self.eject_switch.get(),
            textvariable=self.y0_eject, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.y_eject_input.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入0个TNT配置下，珍珠开炮时具有的初始Y动量 ------ #
        self.init_y_motion_eject_label = ttk.Label(
            master=self.eject_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["eject"]["zero_TNT_y_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.init_y_motion_eject_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.init_y_motion_eject_input = ttk.Entry(
            master=self.eject_settings_page, state=self.eject_switch.get(),
            textvariable=self.y_init_motion_e, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.init_y_motion_eject_input.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入1个TNT配置下，珍珠开炮时具有的初始Y动量 ------ #
        self.y_motion_eject_label = ttk.Label(
            master=self.eject_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["eject"]["one_TNT_y_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.y_motion_eject_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.y_motion_eject_input = ttk.Entry(
            master=self.eject_settings_page, state=self.eject_switch.get(),
            textvariable=self.y_eject_motion, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.y_motion_eject_input.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # ------ 输入1个TNT配置下，珍珠开炮时具有的初始XZ动量 ------ #
        self.xz_init_motion_eject_label = ttk.Label(
            master=self.eject_settings_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["eject"]["one_TNT_xz_motion"],
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        self.xz_init_motion_eject_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.xz_init_motion_eject_input = ttk.Entry(
            master=self.eject_settings_page, state=self.eject_switch.get(),
            textvariable=self.xz_eject, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        self.xz_init_motion_eject_input.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    def create_button_page(self) -> None:

        """
        创建功能按钮界面
        """

        # ------ 创建功能按钮界面 ------ #
        self.button_page = ttk.Frame(self.setting_input_frame, width=550, height=200)
        self.button_page.grid_propagate(False)
        self.button_page.grid_columnconfigure(0, weight=1)
        self.button_page.grid(row=3, column=0, sticky=NSEW, pady=5)

        # ------ 预览设置功能按钮 ------ #
        self.preview_button = ttk.Button(
            master=self.button_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["button_preview"],
            bootstyle=(PRIMARY, OUTLINE),
            command=lambda: preview_func(self),
        )
        self.preview_button.grid(row=0, column=0, padx=5, pady=5, sticky=EW)

        # ------ 查看当前设置功能按钮 ------ #
        self.check_button = ttk.Button(
            master=self.button_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["button_check_settings"],
            bootstyle=(SUCCESS, OUTLINE),
            command=lambda: check_func(self),
        )
        self.check_button.grid(row=1, column=0, padx=5, pady=5, sticky=EW)

        # ------ 导入设置功能按钮 ------ #
        self.import_button = ttk.Button(
            master=self.button_page,
            text=self.LANGUAGE[self.lang]["settings_frame"]["settings_input_frame"]["button_import"],
            bootstyle=(SUCCESS, OUTLINE),
            command=lambda: import_func(self),
        )
        self.import_button.grid(row=2, column=0, padx=5, pady=5, sticky=EW)
