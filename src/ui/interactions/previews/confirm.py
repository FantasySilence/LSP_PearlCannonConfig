# ================================================= #
# @Author: Fantasy_Silence                          #
# @Time: 2024-07-28                                 #
# @IDE: Visual Studio Code & PyCharm                #
# @Python: 3.9.7                                    #
# ================================================= #
# @Description: 使用预览中的设置按钮的功能             #
# ================================================= #
import os
import sys
import json
from ttkbootstrap.constants import *
from src.common.filesio import FilesIO


def confirm_func(cls) -> None:

    """
    使用预览中的设置按钮的功能
    """

    try:
        # ------ 获取文本内容 ------ #
        settings_str = cls.text_area.get(1.0, END)

        # ------ 清除注释与空行 ------ #
        settings = ""
        for line in settings_str.split('\n'):
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            settings += line.strip()
                
        # ------ 转换为字典 ------ #
        settings_dict = eval(settings)

        # ------ 存入设置文件中 ------ #
        with open(FilesIO.load_json("settings.json"), "w", encoding="utf-8") as f:
            json.dump(settings_dict, f, ensure_ascii=False, indent=4)
        
        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)
    except Exception:
        pass
