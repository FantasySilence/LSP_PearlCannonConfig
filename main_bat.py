# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Descript: 这里是主程序入口的cmd版本  #
# =================================== #
from src.modules.calTNT_flat import TNTConfigForFlat
from src.modules.calTNT_eject import TNTConfigForEjection

print("输入目标地点的X坐标: ")
x = int(input())
print("输入目标地点的Z坐标: ")
z = int(input())
print("选择平射模式或抛射模式(F/E)：")
mode = input()

if mode.lower() == "f":
    dir, res = TNTConfigForFlat.config(x, z)
elif mode.lower() == "e":
    dir, res = TNTConfigForEjection.config(x, z)
else:
    print("Invalid mode selected.")
    exit()

print("=" * 100)
print("方向：", dir)
print("=" * 100)
print("距离偏移\t\t飞行时间\t蓝色TNT数量\t红色TNT数量\tTNT总数量")
for index, row in res.iterrows():
    print(f'{row["距离偏移"]}\t{row["飞行时间"]}\t\t{row["蓝色TNT数量"]}\t\t{row["红色TNT数量"]}\t\t{row["TNT总数量"]}')
print("=" * 100)
