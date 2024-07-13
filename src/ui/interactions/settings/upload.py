# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 导入设置               #
# =================================== #
import os
import sys
import json
from tkinter import messagebox
from src.common.filesio import FilesIO
from tkinter.filedialog import askopenfilename

def upload_button(cls) -> None:

    """
    导入设置
    """

    # ------ 导入文件窗口 ------ #
    file_path = askopenfilename(
        title=cls.LANGUAGE[cls.lang]["settings_frame"]["button_import"],
        filetypes=[("JSON files", "*.json")]
    )
    if not file_path:
        return

    # ------ 将导入的文件内容写入应用的设置文件中 ------ #
    try:
        with open(file_path, mode="r") as file:
            settings = json.load(file)
            with open(
                FilesIO.load_json("settings.json"), mode="w"
            ) as files:
                json.dump(settings, files, indent=4)
        
        # ------ 重启应用，设置生效 ------ #
        python = sys.executable
        os.execl(python, python, *sys.argv)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to import settings: {e}")
