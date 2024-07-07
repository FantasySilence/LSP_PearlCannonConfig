# =============================================== #
# @Author: Fantasy_Silence                        #
# @Time: 2024-06-29                               #
# @IDE: Visual Studio Code & PyCharm              #
# @Python: 3.9.7                                  #
# =============================================== #
# @Description: 用户输入页面，进行主炮及返程炮的配置  #
# =============================================== #
import json
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO
from src.ui.frames.output import OutputFrame
from src.ui.frames.settings import SettingsFrame
from src.modules.calTNT_flat import TNTConfigForFlat
from src.common.input_validation import validate_number
from src.modules.calTNT_eject import TNTConfigForEjection


class InputFrame(ttk.Frame):

    def __init__(self, master, res_page: OutputFrame, *args, **kwargs):

        # ------ 读取设置文件中的默认设置 ------ #
        with open(FilesIO.load_json("settings.json"), "r") as f:
            self.settings = json.load(f)

        # ------ 创建输入窗口的根容器 ------ #
        super().__init__(master, *args, **kwargs)
        self.x0_input = ttk.StringVar(value=self.settings["XZ_INIT_POSTION"]["X"])
        self.z0_input = ttk.StringVar(value=self.settings["XZ_INIT_POSTION"]["Z"])
        self.x_input = ttk.StringVar(value=0)
        self.z_input = ttk.StringVar(value=0)
        self.max_tnt_input = ttk.StringVar(value=self.settings["MAX_TNT"])
        self.angel =ttk.StringVar(value="flat")
        self.direction = ttk.StringVar(value="north")

        # ------ 与结果显示页面建立通信 ------ #
        self.res_page = res_page

        # ------ 设置界面 ------ #
        self.settings_window = None

        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        self.pack_propagate(False)
        self.grid_propagate(False)
        text = "输入珍珠的坐标"
        self.input_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5), width=400
        )
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.grid_propagate(False)
        self.input_frame.pack(fill=BOTH, expand=YES)

        # ------ 设置验证函数 ------ #
        self.validation_func = self.input_frame.register(validate_number)

        # ------ 创建页面 ------ #
        self.create_page()
    
    def create_page(self) -> None:

        """
        创建页面
        """

        # ------ 创建存放坐标输入框的页面容器 ------ #
        self.input_page = ttk.Frame(self.input_frame, width=400, height=380)
        self.input_page.columnconfigure(0, weight=1)
        self.input_page.grid_propagate(False)
        self.input_page.grid(row=0, column=0, sticky=NSEW, pady=(0, 0))
        
        # ------ 配置珍珠炮炮口的初始位置 ------ #
        self.original_config()

        # ------ 配置珍珠炮炮口的目标位置 ------ #
        self.target_config()

        # ------ 配置最大TNT数量的输入框 ------ #
        TNT_label = ttk.Label(
            master=self.input_page, 
            text="最大TNT数量：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        TNT_label.grid(row=8, column=0, padx=5, pady=5, sticky=W)
        TNT_input = ttk.Entry(
            master=self.input_page, textvariable=self.max_tnt_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        TNT_input.grid(row=9, column=0, padx=5, pady=5, sticky=EW)



        # ------ 创建存放发射角度多选按钮的页面容器 ------ #
        self.angle_select_page = ttk.Frame(self.input_frame, width=400, height=40)
        self.angle_select_page.columnconfigure(0, weight=1)
        self.angle_select_page.columnconfigure(1, weight=1)
        self.angle_select_page.columnconfigure(2, weight=1)
        self.angle_select_page.columnconfigure(3, weight=1)
        self.angle_select_page.grid_propagate(False)
        self.angle_select_page.grid(row=1, column=0, sticky=NSEW, pady=(0, 0))

        # ------ 创建发射角度的多选按钮 ------ #
        angle_label = ttk.Label(
            master=self.angle_select_page,
            text="珍珠发射角度：",
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        angle_label.grid(row=0, column=0, padx=5, pady=(10, 10), sticky=W, columnspan=2)
        flat_buttons = ttk.Radiobutton(
            master=self.angle_select_page,
            text="平射",
            variable=self.angel,
            value="flat"
        )
        flat_buttons.grid(row=0, column=2, padx=5, pady=(10, 10), sticky=EW)
        eject_buttons = ttk.Radiobutton(
            master=self.angle_select_page,
            text="抛射",
            variable=self.angel,
            value="eject"
        )
        eject_buttons.grid(row=0, column=3, padx=5, pady=(10, 10), sticky=EW)
        flat_buttons.invoke()

        # ------ 如果没有抛射模块，禁用抛射选项 ------ #
        if not self.settings["IS_EJECTION_AVAILABLE"]:
            eject_buttons.configure(state=DISABLED)



        # ------ 创建存放方向多选按钮的页面容器 ------ #
        self.direc_select_page = ttk.Frame(self.input_frame, width=400, height=40)
        self.direc_select_page.columnconfigure(0, weight=1)
        self.direc_select_page.columnconfigure(1, weight=1)
        self.direc_select_page.columnconfigure(2, weight=1)
        self.direc_select_page.columnconfigure(3, weight=1)
        self.direc_select_page.grid_propagate(False)
        self.direc_select_page.grid(row=2, column=0, sticky=NSEW, pady=(0, 0))

        # ------ 创建方向多选按钮 ------ #
        north_button = ttk.Radiobutton(
            master=self.direc_select_page,
            text="North",
            variable=self.direction,
            value="north"
        )
        north_button.grid(row=1, column=0, padx=5, pady=(10, 10), sticky=EW)
        north_button.invoke()
        south_button = ttk.Radiobutton(
            master=self.direc_select_page,
            text="South",
            variable=self.direction,
            value="south"
        )
        south_button.grid(row=1, column=1, padx=5, pady=(10, 10), sticky=EW)
        east_button = ttk.Radiobutton(
            master=self.direc_select_page,
            text="East",
            variable=self.direction,
            value="east"
        )
        east_button.grid(row=1, column=2, padx=5, pady=(10, 10), sticky=EW)
        west_button = ttk.Radiobutton(
            master=self.direc_select_page,
            text="West",
            variable=self.direction,
            value="west"
        )
        west_button.grid(row=1, column=3, padx=5, pady=(10, 10), sticky=EW)



        # ------ 创建存放按钮的的页面容器 ------ #
        self.button_page = ttk.Frame(self.input_frame, width=400, height=250)
        self.button_page.columnconfigure(0, weight=1)
        self.button_page.grid_propagate(False)
        self.button_page.grid(row=3, column=0, sticky=NSEW, pady=(10, 0))

        # ------ 计算TNT当量按钮 ------ #
        calc_button = ttk.Button(
            master=self.button_page,
            text="计算TNT当量",
            bootstyle=(PRIMARY, OUTLINE),
            command=self._func_calc_button
        )
        calc_button.grid(row=1, column=0, padx=5, pady=(10, 10), sticky=EW)

        # ------ 珍珠模拟按钮 ------ #
        simulation_button = ttk.Button(
            master=self.button_page,
            text="珍珠模拟",
            bootstyle=(SECONDARY, OUTLINE),
            command=self._func_simulation_button
        )
        simulation_button.grid(row=2, column=0, padx=5, pady=(10, 10), sticky=EW)

        # ------ 默认值设置按钮 ------ #
        upload_button = ttk.Button(
            master=self.button_page,
            text="默认值设置",
            bootstyle=(INFO, OUTLINE),
            command=self._func_upload_button
        )
        upload_button.grid(row=3, column=0, padx=5, pady=(10, 10), sticky=EW)

        # ------ 退出按钮 ------ #
        exit_button = ttk.Button(
            master=self.button_page,
            text="退出",
            bootstyle=(DANGER, OUTLINE),
            command=quit
        )
        exit_button.grid(row=4, column=0, padx=5, pady=(10, 10), sticky=EW)

    def original_config(self) -> None:

        """
        炮口坐标输入
        """

        # 输入珍珠x坐标
        x_label = ttk.Label(
            master=self.input_page, 
            text="炮口X坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.input_page, textvariable=self.x0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        x_input.grid(row=1, column=0, padx=5, pady=5, sticky=EW)

        # 输入珍珠z坐标
        z_label = ttk.Label(
            master=self.input_page, 
            text="炮口Z坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT),
        )
        z_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.input_page, textvariable=self.z0_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P'),
        )
        z_input.grid(row=3, column=0, padx=5, pady=5, sticky=EW)

    def target_config(self) -> None:

        """
        目标位置输入
        """

        # 输入目标x坐标
        x_label = ttk.Label(
            master=self.input_page, 
            text="目标X坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        x_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        x_input = ttk.Entry(
            master=self.input_page, textvariable=self.x_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        x_input.grid(row=5, column=0, padx=5, pady=5, sticky=EW)

        # 输入目标z坐标
        z_label = ttk.Label(
            master=self.input_page, 
            text="目标Z坐标：", 
            font=Font(family="宋体", size=10),
            bootstyle=(INVERSE, LIGHT)
        )
        z_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)
        z_input = ttk.Entry(
            master=self.input_page, textvariable=self.z_input, width=10,
            validate="focus", validatecommand=(self.validation_func, '%P')
        )
        z_input.grid(row=7, column=0, padx=5, pady=5, sticky=EW)

    def _func_calc_button(self) -> None:

        """
        "计算TNT当量"按钮的功能
        """

        # ------ 平射配置 ------ #
        if self.angel.get() == "flat":
            direction, TNT_config = TNTConfigForFlat.config(
                x_target=int(self.x_input.get()), z_target=int(self.z_input.get()), 
                x_0=float(self.x0_input.get()), z_0=float(self.z0_input.get()),
                max_TNT=int(self.max_tnt_input.get()), settings=self.settings
            )
            self.direction.set(direction)
            self.res_page.load_TNT_config(TNT_config, self.settings)

        # ------ 抛射配置 ------ #
        if self.angel.get() == "eject":
            direction, TNT_config = TNTConfigForEjection.config(
                x_target=int(self.x_input.get()), z_target=int(self.z_input.get()), 
                x_0=float(self.x0_input.get()), z_0=float(self.z0_input.get()),
                max_TNT=int(self.max_tnt_input.get()), settings=self.settings
            )
            self.direction.set(direction)
            self.res_page.load_TNT_config(TNT_config, self.settings)
    
    def _func_simulation_button(self) -> None:

        """
        "珍珠模拟"按钮的功能
        """

        self.res_page.load_pearl_trace(
            float(self.x0_input.get()), float(self.z0_input.get()),
            self.direction.get(), self.angel.get(), settings=self.settings
        )

    def _func_upload_button(self) -> None:

        """
        "默认值设置"按钮的功能
        """

        # ------ 如果已经存在一个窗口，先销毁它 ------ #
        if self.settings_window:
            self.settings_window.destroy()

        # ------ 创建弹窗 ------ #
        self.settings_window = ttk.Toplevel(self.input_frame)
        self.settings_window.title("设置")
        
        # ------ 显示在主窗口的靠中心位置 ------ #
        x = self.input_frame.winfo_rootx() + self.input_frame.winfo_width() // 2
        y = self.input_frame.winfo_rooty()
        self.settings_window.geometry(f"+{x}+{y}")

        # ------ 创建页面 ------ #
        settings_frame = SettingsFrame(self.settings_window)
        settings_frame.pack(fill=BOTH, expand=YES)
