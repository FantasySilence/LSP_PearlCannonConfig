# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-29                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 结果输出页面           #
# =================================== #
import numpy as np
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.modules.pearltrace import PearlPathTracing
from src.modules.config_transform import ConfigInfoTransform


class OutputFrame(ttk.Frame):

    def __init__(self, master, *args, **kwargs):

        super().__init__(master, *args, **kwargs)
        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        self.pack(fill=BOTH, expand=YES)
        text = "配置信息结果输出"
        self.res_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5), width=800, height=730
        )
        self.res_frame.columnconfigure(0, weight=1)
        self.res_frame.grid_propagate(False)
        self.res_frame.pack(fill=BOTH, expand=YES)
        self.blue_TNT_info = ttk.StringVar(value="蓝色TNT数量：")
        self.red_TNT_info = ttk.StringVar(value="红色TNT数量：")
        self.treeview, self.trace_treeview = None, None
        self.item_index = None
        self.scrollbar, self.scrollbar_trace = None, None
        self.create_page()

    def create_page(self) -> None:

        """
        创建页面
        """

        # ------ 创建存放Treeview的页面容器 ------ #
        self.treeview_frame = ttk.Frame(self.res_frame, width=800, height=635)
        self.treeview_frame.pack_propagate(False)
        self.treeview_frame.grid(row=0, column=0, sticky=NSEW)

        # ------ 表头 ------ #
        columns = ("距离偏移", "飞行时间", "蓝色TNT数量", "红色TNT数量", "TNT总数量")

        # ------ 创建Treeview ------ #
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=columns, show="headings"
        )
        self.treeview.pack(fill=BOTH, expand=YES)

        # ------ 设置列格式，确保对齐等 ------ #
        for col in columns:
            self.treeview.heading(col, text=col, anchor=CENTER)
            self.treeview.column(col, width=140, anchor=CENTER)
        
        # ------ 创建存放TNT配置数详细信息的页面容器 ------ #
        self.tnt_frame = ttk.Frame(self.res_frame, width=800, height=95)
        self.tnt_frame.grid_propagate(False)
        self.tnt_frame.grid(row=1, column=0, sticky=NSEW)

        # ------ 创建显示TNT详细配置的标签 ------ #
        blue_TNT_label = ttk.Label(
            master=self.tnt_frame, textvariable=self.blue_TNT_info, font=("宋体", 10)
        )
        blue_TNT_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        red_TNT_label = ttk.Label(
            master=self.tnt_frame, textvariable=self.red_TNT_info, font=("宋体", 10)
        )
        red_TNT_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    def on_item_selected(self, event) -> None:

        """
        当Treeview选中某一行时，将选中行的信息返回到用户输入界面
        """

        # ------ 获取选中行的标识符 ------ #
        selected_item = self.treeview.focus()
        
        # ------ 获取该行的值 ------ #
        self.item_values = self.treeview.item(selected_item, 'values')

        # ------ 获取选中行的索引 ------ #
        item_id = self.treeview.selection()[0]
        self.item_index = self.treeview.index(item_id)

        # ------ 更新TNT详细信息 ------ #
        blue_TNT, red_TNT = self.item_values[2:4]
        blue_TNT_str, red_TNT_str = ConfigInfoTransform.translate(
            int(blue_TNT[:-2]), int(red_TNT[:-2]), settings=self.settings
        )
        self.blue_TNT_info.set(f"蓝色TNT数量：{blue_TNT_str}")
        self.red_TNT_info.set(f"红色TNT数量：{red_TNT_str}")
    
    def load_TNT_config(self, config: pd.DataFrame, settings: dict) -> None:

        """
        与用户输入进行通信，显示TNT配置信息
        """

        # ------ 获取settings ------ #
        self.settings = settings

        # ------ 清除原先的TNT详细信息 ------ #
        self.blue_TNT_info.set("蓝色TNT数量：")
        self.red_TNT_info.set("红色TNT数量：")

        # ------ 清除原先的轨迹信息 ------ #
        self.item_index = None

        # ------ 彻底清除原先的Treeview ------ #
        if self.treeview:
            self.treeview.destroy()
        if self.trace_treeview:
            self.trace_treeview.destroy()

        # ------ 表头 ------ #
        columns = ("距离偏移", "飞行时间", "蓝色TNT数量", "红色TNT数量", "TNT总数量")

        # ------ 创建Treeview ------ #
        self.treeview = ttk.Treeview(
            self.treeview_frame, columns=columns, show="headings"
        )
        self.treeview.pack(fill=BOTH, expand=YES)

        # ------ 为表头配置函数，点击进行排序 ------ #
        self.treeview.heading(
            '距离偏移', text='距离偏移', 
            command=lambda: self.sort_column('距离偏移')
        )
        self.treeview.heading(
            '飞行时间', text='飞行时间', 
            command=lambda: self.sort_column('飞行时间')
        )

        # ------ 设置列格式，确保对齐等 ------ #
        for col in columns:
            self.treeview.heading(col, text=col, anchor=CENTER)
            self.treeview.column(col, width=140, anchor=CENTER)
        
        # ------ 捕捉选中某一行，并绑定功能函数 ------ #
        self.treeview.bind("<<TreeviewSelect>>", self.on_item_selected)

        # ------ 从配置结果中获取信息 ------ #
        self.output_dataframe = config[[
            '距离偏移', '飞行时间', '蓝色TNT数量', '红色TNT数量', 'TNT总数量'
        ]]
        self.output_dataframe["距离偏移"] = self.output_dataframe["距离偏移"].map(
            lambda x: round(x, 8)
        )

        # ------ 将配置信息插入进先前创建的Treeview ------ #
        for _, row in self.output_dataframe.iterrows():
            self.treeview.insert(
                "", "end", values=(
                    row["距离偏移"], row["飞行时间"],
                    row["蓝色TNT数量"], row["红色TNT数量"], row["TNT总数量"]
                )
            )
        
        # ------ 数据量可能较大，设置一个滚动条 ------ #
        if self.scrollbar:
            pass
        else:
            self.scrollbar = ttk.Scrollbar(
                self.treeview, orient="vertical", command=self.treeview.yview
            )
            self.scrollbar.pack(side='right', fill='y')
            self.treeview.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar = None

    def load_pearl_trace(
            self, x0: float, z0: float, direction: str, mode: str, settings: dict
    ) -> None:

        """
        与用户输入进行通信，显示珍珠飞行时每时刻的位置
        """

        # ------ 如果没有选中某个配置 ------ #
        if self.item_index is None:
            return

        # ------ 彻底清除原先的Treeview ------ #
        if self.treeview:
            self.treeview.destroy()
        if self.trace_treeview:
            self.trace_treeview.destroy()

        # ------ 表头 ------ #
        columns = ("游戏刻", "X坐标", "Y坐标", "Z坐标")

        # ------ 创建Treeview ------ #
        self.trace_treeview = ttk.Treeview(
            self.treeview_frame, columns=columns, show="headings"
        )
        self.trace_treeview.pack(fill=BOTH, expand=YES)

        # ------ 设置列格式，确保对齐等 ------ #
        for col in columns:
            self.trace_treeview.heading(col, text=col, anchor=CENTER)
            self.trace_treeview.column(col, width=175, anchor=CENTER)
        
        # ------ 清除Treeview中的旧数据 ------ #
        self.trace_treeview.delete(*self.trace_treeview.get_children())

        # ------ 从选中的结果中获取信息 ------ #
        res = pd.Series(
            self.item_values[1: 4], 
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
            self.trace_treeview.insert(
                "", "end", values=(
                    row["time"], row["x"], row["y"], row["z"]
                )
            )
        
        # ------ 将到达目的地的那一条高亮显示 ------ #
        item_id_highlight = self.trace_treeview.get_children()[int(res[0])]
        self.trace_treeview.tag_configure("highlight", background="yellow")
        self.trace_treeview.item(item_id_highlight, tags=("highlight",))
        
        # ------ 数据量可能较大，设置一个滚动条 ------ #
        if self.scrollbar_trace:
            pass
        else:
            self.scrollbar_trace = ttk.Scrollbar(
                self.trace_treeview, orient="vertical", command=self.trace_treeview.yview
            )
            self.scrollbar_trace.pack(side='right', fill='y')
            self.trace_treeview.configure(yscrollcommand=self.scrollbar_trace.set)
            self.scrollbar_trace = None

    def sort_column(self, col_id: str, reverse: bool=False) -> None:

        """
        排序
        """

        data = [
            (float(self.treeview.set(child, col_id)), child) 
            for child in self.treeview.get_children('')
        ]
        data.sort(reverse=reverse)
        for index, (val, child) in enumerate(data):
            self.treeview.move(child, '', index)
