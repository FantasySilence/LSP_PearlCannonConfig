# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 结果输出界面的语言更新  #
# =================================== #
from ttkbootstrap.constants import *


def update_language_in_output(cls, lang: str) -> None:

    """
    更新语言设置
    """

    # ------ 通信，获取语言设置 ------ #
    cls.lang = lang

    # ------ 更新页面标签语言 ------ #
    cls.res_frame.config(
        text=cls.LANGUAGE[lang]["output_frame"]["output_labelframe_text"]
    )

    # ------ 更新配置结果树状菜单语言 ------ #
    columns=(
        cls.LANGUAGE[lang]["output_frame"]["config_treeview"]["columns_1"],
        cls.LANGUAGE[lang]["output_frame"]["config_treeview"]["columns_2"],
        cls.LANGUAGE[lang]["output_frame"]["config_treeview"]["columns_3"],
        cls.LANGUAGE[lang]["output_frame"]["config_treeview"]["columns_4"],
        cls.LANGUAGE[lang]["output_frame"]["config_treeview"]["columns_5"],
    )
    try:
        cls.treeview.config(columns=columns)
        for col in columns:
            cls.treeview.heading(col, text=col, anchor=CENTER)
            cls.treeview.column(col, width=159, anchor=CENTER)
    except Exception:
        pass
    
    # ------ 更新轨迹模拟树状菜单语言 ------ #
    columns = (
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_1"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_2"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_3"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_4"],
    )
    try:
        cls.trace_treeview.config(columns=columns)
        for col in columns:
            cls.trace_treeview.heading(col, text=col, anchor=CENTER)
            cls.trace_treeview.column(col, width=198, anchor=CENTER)
    except Exception:
        pass

    # ------ 更新TNT数量标签 ------ #
    if len(cls.blue_TNT_info.get().split("：")) == 1:
        cls.blue_TNT_info.set(
            value=cls.LANGUAGE[lang]["output_frame"]["blue_tnt_label"],
        )
    # 如果调整语言时，已经存在配置信息
    else:
        blue_TNT_str = cls.blue_TNT_info.get().split("：")[1]
        cls.blue_TNT_info.set(
            value=cls.LANGUAGE[lang]["output_frame"]["blue_tnt_label"] + blue_TNT_str
        )
    
    if len(cls.red_TNT_info.get().split("：")) == 1:
        cls.red_TNT_info.set(
            value=cls.LANGUAGE[lang]["output_frame"]["red_tnt_label"],
        )
    # 如果调整语言时，已经存在配置信息
    else:
        red_TNT_str = cls.red_TNT_info.get().split("：")[1]
        cls.red_TNT_info.set(
            value=cls.LANGUAGE[lang]["output_frame"]["red_tnt_label"] + red_TNT_str
        )
