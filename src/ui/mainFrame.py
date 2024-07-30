# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-29                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 主程序的界面           #
# =================================== #
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.ui.frames.output import OutputFrame
from src.common.path_utils import resource_path
from src.ui.frames.user_input import InputFrame


class MainFrame(ttk.Frame):

    def __init__(self, master) -> None:

        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.pack(fill=BOTH, expand=YES)

        # ------ 子页面列表 ------ #
        self.sub_pages = []

        # ------ 读取语言设置 ------ #
        self.language = ttk.StringVar(value="简体中文")
        self.language_code = {
            "English": "en", "简体中文": "zh_CN", "繁體中文": "zh_TW"
        }
        with open(
            resource_path("resources/languages/languages.json"), 
            mode="r", encoding="utf-8"
        ) as f:
            self.LANGUAGE = json.load(f)
        
        # ------ 创建页面 ------ #
        self.create_page()

    def create_page(self) -> None:
        
        """
        创建页面
        """

        # ------ 加载图片 ------ #
        self.images = [
            ttk.PhotoImage(
                name="logo", 
                file=resource_path("resources/images/Ender_Pearl.png")
            ),
        ]

        # ------ 创建窗口标题的容器 ------ #
        hdr_frame = ttk.Frame(self, bootstyle=INFO, width=1200, height=70)
        hdr_frame.pack(fill=X, side=TOP, pady=5)
        # 向标题子容器中放入一幅logo图片
        hdr_label = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE, INFO)
        )
        hdr_label.pack(side=LEFT)
        # 向标题子容器中添加标题文字
        self.logo_text = ttk.Label(
            master=hdr_frame,
            text='LSP Hub通用珍珠炮配置器',
            font=('TkDefaultFont', 30),
            bootstyle=(INVERSE, INFO)
        )
        self.logo_text.pack(side=LEFT, padx=15, ipadx=50)
        # 向标题子容器中添加语言设置
        self.language_menu = ttk.Combobox(
            master=hdr_frame, 
            textvariable=self.language, 
            values=["English", "简体中文", "繁體中文"],
            bootstyle=SUCCESS,
            width=10,
            state="readonly"
        )
        self.language_menu.pack(side=RIGHT, padx=(0, 10))
        self.language_menu.bind("<<ComboboxSelected>>", lambda e: self.update_language())
        self.language_menu.select_clear()
        # 向标题子容器中添加语言设置标签
        lang_label = ttk.Label(
            master=hdr_frame,
            text='LANG:',
            font=('TkDefaultFont', 15),
            bootstyle=(INVERSE, INFO)
        )
        lang_label.pack(side=RIGHT, padx=(0, 4))

        # ------ 创建存放用户输入与结果显示的容器 ------ #
        self.main_frame = ttk.Frame(self, bootstyle=LIGHT)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=3)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=YES)
        # 向主容器中添加结果显示子容器
        result_frame = OutputFrame(self.main_frame, width=800, height=730)
        result_frame.grid(row=0, column=1, sticky=NSEW)
        self.sub_pages.append(result_frame)
        # 向主容器中添加用户输入子容器
        input_frame = InputFrame(self.main_frame, result_frame, width=400, height=730)
        input_frame.grid(row=0, column=0, sticky=NSEW)
        self.sub_pages.append(input_frame)
    
    def update_language(self) -> None:

        """
        更新语言设置
        """

        # ------ 清除选中状态 ------ #
        self.after(1, lambda: self.language_menu.selection_clear())

        # ------ 更新主界面的语言 ------ #
        lang = self.language_code[self.language.get()]
        self.logo_text.config(text=self.LANGUAGE[lang]["title"])

        # ------ 更新其他子页面的语言 ------ #
        for page in self.sub_pages:
            page.update_language(lang)

    @staticmethod
    def _show() -> None:
        root = ttk.Window(title="LSP_PearlConfig v6.3", size=(1200, 800))
        root.resizable(False, False)
        MainFrame(root)
        root.mainloop()

    @classmethod
    def show(cls) -> None:
        MainFrame._show()
    