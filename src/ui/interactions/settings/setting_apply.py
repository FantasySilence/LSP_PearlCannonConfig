# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 应用设置               #
# =================================== #
import os
import sys
import json
from tkinter import messagebox
from src.common.filesio import FilesIO


def apply_settings(self) -> None:

        """
        应用设置
        """

        # ------ 读取现有的设置并进行修改 ------ #
        with open(
            FilesIO.load_json("settings.json"), mode="r"
        ) as file:
            settings = json.load(file)
            try:
                if self.x0_input.get() != '':
                    settings["INIT_POSITION"]["X"] = float(self.x0_input.get())
                if self.z0_input.get() != '':
                    settings["INIT_POSITION"]["Z"] = float(self.z0_input.get())
                if self.max_tnt_input.get() != '':
                    settings["MAX_TNT"] = int(self.max_tnt_input.get())
             # 出错时显示弹窗
            except Exception:
                messagebox.showerror(
                    title=self.LANGUAGE[self.lang]["error_frame"]["title"], 
                    message=self.LANGUAGE[self.lang]["error_frame"]["error_message"]
                )
                return

        # ------ 将修改后的设置进行保存 ------ #
        with open(
            FilesIO.load_json("settings.json"), mode="w"
        ) as files:    
            json.dump(settings, files, indent=4)

        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)
