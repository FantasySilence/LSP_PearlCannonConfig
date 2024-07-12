# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-07                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 珍珠炮配置文件生成器    #
# =================================== #
import os
import json
from typing import Type, TypeVar


# ------ 写在前面的信息 ------ #
banner = """

  _____                _  _____             __ _        _____                           _             
 |  __ \              | |/ ____|           / _(_)      / ____|                         | |            
 | |__) |__  __ _ _ __| | |     ___  _ __ | |_ _  __ _| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _ \/ _` | '__| | |    / _ \| '_ \|  _| |/ _` | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  |  __/ (_| | |  | | |___| (_) | | | | | | | (_| | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \___|\__,_|_|  |_|\_____\___/|_| |_|_| |_|\__, |\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                  __/ |                                               
                                                 |___/                                                

Powered By 御河DE天街
Github: https://github.com/FantasySilence/LSP_PearlCannonConfig

欢迎使用珍珠炮技术参数JSON文件生成器。
使用这个生成器生成的JSON文件将作为珍珠炮配置器的设置文件，配置时导入即可
请确保在使用本生成器前，您的MC客户端能够在游戏中获取 /log projectiles full 指令的信息
"""
print(banner)
print("如果您已经了解，请按下回车键......")
input()

datatype = TypeVar('datatype')
def get_user_input(data_type: Type[datatype]=float) -> datatype:

    """
    定义一个输入验证函数
    """

    while True:
        try:
            return data_type(input())
        except ValueError:
            print("格式不正确，请重新输入...")

# ------ 第一层次 ------ #
print("请输入炮口的X坐标：")
x_init = get_user_input()

print("请输入炮口的Z坐标：")
z_init = get_user_input()

print("请输入您的珍珠炮单边最大TNT数量：")
max_tnt = get_user_input(int)

print("请输入您的珍珠炮单个阵列的最大TNT数：")
max_tnt_unit = get_user_input(int)

print("请输入您的珍珠炮是否具有抛射的功能(Y/N)：")
is_eject = input()

# ------ 第二层次 ------ #
print("接下来请为您的珍珠炮配置0个TNT，并在MC中输入指令 /log projectiles full ")
print("珍珠落地后，找到开炮的时刻，读取log信息...")
if is_eject.lower() == "y":
    print("首先将珍珠炮设置为平射模式，丢出珍珠...")
    print("请输入炮口的Y坐标：")
    y_init_f = get_user_input()

    print("请输入开炮时刻珍珠的Y轴动量：")
    y_init_motion_f = get_user_input()

    print("接下来，接下来请为您的珍珠炮配置1个TNT")
    print("请输入1个TNT赋予珍珠的XZ轴动量大小(一个正数)：")
    xz_motion_f = get_user_input()

    print("请输入1个TNT配置下珍珠的Y轴动量大小：")
    y1_motion_f = get_user_input()
    y_motion_f = y1_motion_f - y_init_motion_f

    print("然后将珍珠炮设置为抛射模式并配置0个TNT...")
    print("请输入炮口的Y坐标：")
    y_init_e = get_user_input()

    print("请输入开炮时刻珍珠的Y轴动量：")
    y_init_motion_e = get_user_input()

    print("接下来，接下来请为您的珍珠炮配置1个TNT")
    print("请输入1个TNT赋予珍珠的XZ轴动量大小(一个正数)：")
    xz_motion_e = get_user_input()

    print("请输入1个TNT配置下珍珠的Y轴动量大小：")
    y1_motion_e = get_user_input()
    y_motion_e = y1_motion_e - y_init_motion_e

else:
    print("请输入炮口的Y坐标：")
    y_init_f = get_user_input()

    print("请输入开炮时刻珍珠的Y轴动量：")
    y_init_motion_f = get_user_input()

    print("接下来，接下来请为您的珍珠炮配置1个TNT")
    print("请输入1个TNT赋予珍珠的XZ轴动量大小(一个正数)：")
    xz_motion_f = get_user_input()

    print("请输入1个TNT配置下珍珠的Y轴动量大小：")
    y1_motion_f = get_user_input()
    y_motion_f = y1_motion_f - y_init_motion_f

# ------ 第三层次 ------ #
print("请为您的珍珠炮配置文件命名：")
config_name = input() + ".json"
if is_eject.lower() == "y":

    # ------ 生成设置文件的字典 ------ #
    settings = {
        "IS_EJECTION_AVAILABLE": True,
        "MAX_TNT": max_tnt,
        "MAX_TNT_UNIT": max_tnt_unit,
        "XZ_INIT_POSTION": {
            "X": x_init,
            "Z": z_init
        },
        "MOTION_FOR_FLAT_FIRE": {
            "XZ_MOTION": xz_motion_f,
            "Y_MOTION": y_motion_f,
            "Y_INIT_MOTION": y_init_motion_f,
            "Y_INIT_POSITION": y_init_f
        },
        "MOTION_FOR_EJECTIONS": {
            "XZ_MOTION": xz_motion_e,
            "Y_MOTION": y_motion_e,
            "Y_INIT_MOTION": y_init_motion_e,
            "Y_INIT_POSITION": y_init_e
        }
    }

    # ------ 写入JSON文件 ------ #
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    with open(os.path.join(desktop_path, config_name), "w") as f:
        json.dump(settings, f, indent=4)
    print("配置文件已保存至桌面%s" % os.path.join(desktop_path, config_name))

else:
    
    # ------ 生成设置文件的字典 ------ #
    settings = {
        "IS_EJECTION_AVAILABLE": False,
        "MAX_TNT": max_tnt,
        "MAX_TNT_UNIT": max_tnt_unit,
        "XZ_INIT_POSTION": {
            "X": x_init,
            "Z": z_init
        },
        "MOTION_FOR_FLAT_FIRE": {
            "XZ_MOTION": xz_motion_f,
            "Y_MOTION": y_motion_f,
            "Y_INIT_MOTION": y_init_motion_f,
            "Y_INIT_POSITION": y_init_f
        }
    }

    # ------ 写入JSON文件 ------ #
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    with open(os.path.join(desktop_path, config_name), "w") as f:
        json.dump(settings, f, indent=4)
    print("配置文件已保存至桌面%s" % os.path.join(desktop_path, config_name))
