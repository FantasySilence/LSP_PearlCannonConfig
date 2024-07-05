# ============================================= #
# @Author: Fantasy_Silence                      #
# @Time: 2024-07-05                             #
# @IDE: Visual Studio Code & PyCharm            #
# @Python: 3.9.7                                #
# ============================================= #
# @Description: 为适应打包编写的文件路径工具       #
# ============================================= #
import os
import sys


def resource_path(relative_path: str) -> str:

    """
    获取资源文件的绝对路径
    relative_path：资源文件相对main.py的相对路径
    """

    try:
        # PyInstaller创建临时文件
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
