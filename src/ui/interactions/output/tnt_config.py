# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 展示TNT配置结果        #
# =================================== #
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.ui.interactions.output.select import on_item_selected


def show_tnt_config(cls, config: pd.DataFrame, settings: dict) -> None:

    """
    展示TNT配置结果
    """

    # ------ 获取settings ------ #
    cls.settings = settings

    # ------ 清除原先的TNT详细信息 ------ #
    cls.blue_TNT_info.set(
        cls.LANGUAGE[cls.lang]["output_frame"]["blue_tnt_label"]
    )
    cls.red_TNT_info.set(
        cls.LANGUAGE[cls.lang]["output_frame"]["red_tnt_label"]
    )

    # ------ 清除原先的轨迹信息 ------ #
    cls.item_index = None

    # ------ 彻底清除原先的Treeview ------ #
    if cls.treeview:
        cls.treeview.destroy()
    if cls.trace_treeview:
        cls.trace_treeview.destroy()

    # ------ 表头 ------ #
    columns=(
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_1"],
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_2"],
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_3"],
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_4"],
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_5"],
    )

    # ------ 创建Treeview ------ #
    cls.treeview = ttk.Treeview(
        cls.treeview_frame, columns=columns, show="headings"
    )
    cls.treeview.pack(fill=BOTH, expand=YES)

    # ------ 为表头配置函数，点击进行排序 ------ #
    cls.treeview.heading(
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_1"], 
        text=cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_1"], 
        command=lambda: cls.sort_column(
            cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_1"]
        )
    )
    cls.treeview.heading(
        cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_2"], 
        text=cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_2"], 
        command=lambda: cls.sort_column(
            cls.LANGUAGE[cls.lang]["output_frame"]["config_treeview"]["columns_2"]
        )
    )

    # ------ 设置列格式，确保对齐等 ------ #
    for col in columns:
        cls.treeview.heading(col, text=col, anchor=CENTER)
        cls.treeview.column(col, width=140, anchor=CENTER)
    
    # ------ 捕捉选中某一行，并绑定功能函数 ------ #
    cls.treeview.bind(
        "<<TreeviewSelect>>", 
        lambda event: on_item_selected(cls, event)
    )

    # ------ 从配置结果中获取信息 ------ #
    cls.output_dataframe = config[[
        '距离偏移', '飞行时间', '蓝色TNT数量', '红色TNT数量', 'TNT总数量'
    ]]
    cls.output_dataframe["距离偏移"] = cls.output_dataframe["距离偏移"].map(
        lambda x: round(x, 8)
    )

    # ------ 将配置信息插入进先前创建的Treeview ------ #
    for _, row in cls.output_dataframe.iterrows():
        cls.treeview.insert(
            "", "end", values=(
                row["距离偏移"], row["飞行时间"],
                row["蓝色TNT数量"], row["红色TNT数量"], row["TNT总数量"]
            )
        )
    
    # ------ 数据量可能较大，设置一个滚动条 ------ #
    if cls.scrollbar:
        pass
    else:
        cls.scrollbar = ttk.Scrollbar(
            cls.treeview, orient="vertical", command=cls.treeview.yview
        )
        cls.scrollbar.pack(side='right', fill='y')
        cls.treeview.configure(yscrollcommand=cls.scrollbar.set)
        cls.scrollbar = None
