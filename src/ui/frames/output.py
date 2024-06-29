# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-29                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 结果输出页面           #
# =================================== #
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


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
        self.blue_TNT_info = ttk.StringVar(value="蓝色TNT：")
        self.red_TNT_info = ttk.StringVar(value="红色TNT：")
        self.scrollbar = None
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


if __name__ == "__main__":
    
    app = ttk.Window("OutputFrame", size=(700, 730))
    OutputFrame(app)
    app.mainloop()
