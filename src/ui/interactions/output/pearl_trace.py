# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 显示珍珠轨迹           #
# =================================== #
import numpy as np
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.modules.pearltrace import PearlPathTracing


def show_pearl_trace(
        cls, x0: float, z0: float, direction: str, mode: str, settings: dict
    ) -> None:

    """
    显示珍珠飞行时每时刻的位置
    """

    # ------ 如果没有选中某个配置 ------ #
    if cls.item_index is None:
        return

    # ------ 彻底清除原先的Treeview ------ #
    if cls.treeview:
        cls.treeview.destroy()
    if cls.trace_treeview:
        cls.trace_treeview.destroy()

    # ------ 表头 ------ #
    columns = (
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_1"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_2"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_3"],
        cls.LANGUAGE[cls.lang]["output_frame"]["trace_treeview"]["columns_4"],
    )

    # ------ 创建Treeview ------ #
    cls.trace_treeview = ttk.Treeview(
        cls.treeview_frame, columns=columns, show="headings"
    )
    cls.trace_treeview.pack(fill=BOTH, expand=YES)

    # ------ 设置列格式，确保对齐等 ------ #
    for col in columns:
        cls.trace_treeview.heading(col, text=col, anchor=CENTER)
        cls.trace_treeview.column(col, width=175, anchor=CENTER)
    
    # ------ 清除Treeview中的旧数据 ------ #
    cls.trace_treeview.delete(*cls.trace_treeview.get_children())

    # ------ 从选中的结果中获取信息 ------ #
    res = pd.Series(
        cls.item_values[1: 4], 
        index=['飞行时间', '蓝色TNT数量', '红色TNT数量']
    ).astype(float).to_numpy()
    
    # ------ 计算珍珠运行轨迹 ------ #
    trace_info = PearlPathTracing.generate(
        x0, z0, tnt_num=res[1:], direction=direction, 
        max_ticks=int(res[0]) + 50, mode=mode, settings=settings
    )
    trace_info[["x", "y", "z"]] = np.round(trace_info[["x", "y", "z"]], 6)

    # ------ 将配置信息插入进先前创建的Treeview ------ #
    for _, row in trace_info.iterrows():
        cls.trace_treeview.insert(
            "", "end", values=(
                row["time"], row["x"], row["y"], row["z"]
            )
        )
    
    # ------ 将到达目的地的那一条高亮显示 ------ #
    item_id_highlight = cls.trace_treeview.get_children()[int(res[0])]
    cls.trace_treeview.tag_configure("highlight", background="yellow")
    cls.trace_treeview.item(item_id_highlight, tags=("highlight",))
    
    # ------ 数据量可能较大，设置一个滚动条 ------ #
    if cls.scrollbar_trace:
        pass
    else:
        cls.scrollbar_trace = ttk.Scrollbar(
            cls.trace_treeview, orient="vertical", command=cls.trace_treeview.yview
        )
        cls.scrollbar_trace.pack(side='right', fill='y')
        cls.trace_treeview.configure(yscrollcommand=cls.scrollbar_trace.set)
        cls.scrollbar_trace = None
