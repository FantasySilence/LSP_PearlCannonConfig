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
import json


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

def get_config_path() -> str:

    """
    获取用户目录中的配置文件路径
    """

    exe_dir = get_executable_path()
    config_dir = os.path.join(exe_dir, 'AppSettings')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return os.path.join(config_dir, 'settings.json')

def load_settings() -> dict:

    """
    读取配置
    """

    config_path = get_config_path()
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            settings = json.load(f)
    else:
        # 如果配置文件不存在，则从资源目录中复制默认配置文件
        default_config_path = resource_path('resources/settings/settings.json')
        with open(default_config_path, 'r') as f:
            settings = json.load(f)
        with open(config_path, 'w') as f:
            json.dump(settings, f, indent=4)
    return settings

def save_settings(settings) -> None:

    """
    保存配置
    """

    config_path = get_config_path()
    with open(config_path, 'w') as f:
        json.dump(settings, f, indent=4)

def get_executable_path() -> str:

    """
    获取可执行文件的目录
    """

    if getattr(sys, 'frozen', False):
        # 打包后的可执行文件
        return os.path.dirname(sys.executable)
    else:
        # 未打包的脚本文件
        return os.path.dirname(os.path.abspath(__file__))
