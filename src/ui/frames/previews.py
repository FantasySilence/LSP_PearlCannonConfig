# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 设置结果的预览         #
# =================================== #
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO
from src.ui.interactions.previews.confirm import confirm_func
from src.ui.interactions.previews.export_settings import export_func


class PreviewFrame(ttk.Frame):
    
    def __init__(self, master, lang, *args, **kwargs) -> None:

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
        text = self.LANGUAGE[self.lang]["settings_frame"]["preview_frame"]["preview_labelframe_text"]
        self.res_frame = ttk.Labelframe(
            self, text=text, padding=(0, 5), width=550
        )
        self.res_frame.columnconfigure(0, weight=1)
        self.res_frame.grid_propagate(False)
        self.res_frame.pack(fill=BOTH, expand=YES)
        
        # ------ 创建页面 ------ #
        self.create_page()
    
    def create_page(self) -> None:

        """
        创建页面
        """

        # ------ 创建存放结果预览的页面容器 ------ #
        self.preview_frame = ttk.Frame(master=self.res_frame, width=650, height=560)
        self.preview_frame.grid_propagate(False)
        self.preview_frame.grid(row=0, column=0, sticky=NSEW, pady=(0, 5))
        self.preview_frame.columnconfigure(0, weight=1)

        # ------ 将文本显示窗口加入到存放结果预览的页面容器 ------ #
        self.text_area = ttk.ScrolledText(self.preview_frame, height=27)
        self.text_area.grid(row=0, column=0, sticky=NSEW)
        self.text_area.configure(state=DISABLED)

        # ------ 创建存放按钮的页面容器 ------ #
        self.button_frame = ttk.Frame(master=self.res_frame, width=650, height=100)
        self.button_frame.grid_propagate(False)
        self.button_frame.grid(row=1, column=0, sticky=EW, pady=14)
        self.button_frame.columnconfigure(0, weight=1)

        # ------ 将确认按钮加入到存放按钮的页面容器 ------ #
        self.confirm_button = ttk.Button(
            master=self.button_frame, 
            text=self.LANGUAGE[self.lang]["settings_frame"]["preview_frame"]["button_confirm"], 
            bootstyle=(PRIMARY, OUTLINE),
            command=lambda: confirm_func(self)
        )
        self.confirm_button.grid(row=1, column=0, sticky=EW, padx=5, pady=(0, 5))

        # ------ 将导出设置按钮加入到存放按钮的页面容器 ------ #
        self.export_button = ttk.Button(
            master=self.button_frame,
            text=self.LANGUAGE[self.lang]["settings_frame"]["preview_frame"]["button_export"],
            bootstyle=(PRIMARY, OUTLINE),
            command=lambda: export_func(self),
        )
        self.export_button.grid(row=2, column=0, padx=5, pady=5, sticky=EW)


    def communicate(self, is_eject_available: bool, params: dict) -> None:

        """
        与设置输入界面进行通信
        """

        from src.ui.interactions.previews.conmmunication import load
        load(self, is_eject_available, params, lang=self.lang, language=self.LANGUAGE)
    