# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Descript: 这里是主程序入口的cmd版本  #
# =================================== #
from src.modules.pearltrace import PearlPathTracing
from src.modules.calTNT_flat import TNTConfigForFlat
from src.modules.calTNT_eject import TNTConfigForEjection

while True:
    print("输入目标地点的X坐标: ")
    x = int(input())
    print("输入目标地点的Z坐标: ")
    z = int(input())
    print("选择平射模式或抛射模式(F/E)：")
    mode = input()

    # ------ 计算TNT数量 ------ #
    if mode.lower() == "f":
        dir, res = TNTConfigForFlat.config(x, z)
    elif mode.lower() == "e":
        dir, res = TNTConfigForEjection.config(x, z)
    else:
        print("Invalid mode selected.")
        exit()

    # ------ 显示配置结果 ------ #
    print("=" * 100)
    print("方向：", dir)
    print("=" * 100)
    print("距离偏移\t\t飞行时间\t蓝色TNT数量\t红色TNT数量\tTNT总数量")
    for index, row in res.iterrows():
        print(f'{row["距离偏移"]}\t{row["飞行时间"]}\t\t{row["蓝色TNT数量"]}\t\t{row["红色TNT数量"]}\t\t{row["TNT总数量"]}')
    print("=" * 100)

    # ------ 选择一个配置模拟珍珠轨迹 ------ #
    print("\n")
    print("请从上方结果中选择你预期的到达时间")
    time = int(input())
    if mode.lower() == "f":
        tnt_num = res.loc[res["飞行时间"] == time, ["蓝色TNT数量", "红色TNT数量"]].values[0]
        PearlLocation = PearlPathTracing.generate(tnt_num, dir, time, mode="flat")
        print("飞行时间\tX坐标\t\tY坐标\t\tZ坐标")
        for index, row in PearlLocation.iterrows():
            print("{}\t\t{:.6f}\t{:.6f}\t{:.6f}".format(row["time"], row["x"], row["y"], row["z"]))
    elif mode.lower() == "e":
        tnt_num = res.loc[res["飞行时间"] == time, ["蓝色TNT数量", "红色TNT数量"]].values[0]
        PearlLocation = PearlPathTracing.generate(tnt_num, dir, time, mode="eject")
        print("飞行时间\tX坐标\t\tY坐标\t\tZ坐标")
        for index, row in PearlLocation.iterrows():
            print("{}\t\t{:.6f}\t{:.6f}\t{:.6f}".format(row["time"], row["x"], row["y"], row["z"]))
    else:
        print("Invalid mode selected.")
        exit()

    # ------ 是否继续 ------ #
    print("是否继续(Y/N)")
    flag = input()
    if flag.lower() == "n":
        break
