# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 导出设置功能           #
# =================================== #
import json
from tkinter.constants import *
from tkinter.filedialog import asksaveasfilename

def export_func(cls) -> None:

    """
    导出设置功能
    """

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

    # ------ 导出文件 ------ #
    file_path = asksaveasfilename(
        title=" ",
        initialfile="settings.json",
        defaultextension=".json", 
        filetypes=[("JSON files", "*.json")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(settings_dict, f, ensure_ascii=False, indent=4) 
