# ============================================== #
# @Author: Fantasy_Silence                       #
# @Time: 2024-07-13                              #
# @IDE: Visual Studio Code & PyCharm             #
# @Python: 3.9.7                                 #
# ============================================== #
# @Description: 为用户输入页面创建输入框           #
# ============================================== #
import ttkbootstrap as ttk
from tkinter.font import Font
from ttkbootstrap.constants import *


def original_config(cls) -> None:

    """
    炮口坐标输入
    """

    # 输入珍珠x坐标
    cls.origin_x_label = ttk.Label(
        master=cls.input_page, 
        text="炮口X坐标：", 
        font=Font(family="宋体", size=10),
        bootstyle=(INVERSE, LIGHT)
    )
    cls.origin_x_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    x_input = ttk.Entry(
        master=cls.input_page, textvariable=cls.x0_input, width=10,
        validate="focus", validatecommand=(cls.validation_func, '%P'),
    )
    x_input.grid(row=1, column=0, padx=5, pady=5, sticky=EW)

    # 输入珍珠z坐标
    cls.origin_z_label = ttk.Label(
        master=cls.input_page, 
        text="炮口Z坐标：", 
        font=Font(family="宋体", size=10),
        bootstyle=(INVERSE, LIGHT),
    )
    cls.origin_z_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    z_input = ttk.Entry(
        master=cls.input_page, textvariable=cls.z0_input, width=10,
        validate="focus", validatecommand=(cls.validation_func, '%P'),
    )
    z_input.grid(row=3, column=0, padx=5, pady=5, sticky=EW)


def target_config(cls) -> None:

    """
    目标位置输入
    """

    # 输入目标x坐标
    cls.target_x_label = ttk.Label(
        master=cls.input_page, 
        text="目标X坐标：", 
        font=Font(family="宋体", size=10),
        bootstyle=(INVERSE, LIGHT)
    )
    cls.target_x_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    x_input = ttk.Entry(
        master=cls.input_page, textvariable=cls.x_input, width=10,
        validate="focus", validatecommand=(cls.validation_func, '%P')
    )
    x_input.grid(row=5, column=0, padx=5, pady=5, sticky=EW)

    # 输入目标z坐标
    cls.target_z_label = ttk.Label(
        master=cls.input_page, 
        text="目标Z坐标：", 
        font=Font(family="宋体", size=10),
        bootstyle=(INVERSE, LIGHT)
    )
    cls.target_z_label.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    z_input = ttk.Entry(
        master=cls.input_page, textvariable=cls.z_input, width=10,
        validate="focus", validatecommand=(cls.validation_func, '%P')
    )
    z_input.grid(row=7, column=0, padx=5, pady=5, sticky=EW)
