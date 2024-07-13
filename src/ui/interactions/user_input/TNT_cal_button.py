# ========================================= #
# @Author: Fantasy_Silence                  #
# @Time: 2024-07-13                         #
# @IDE: Visual Studio Code & PyCharm        #
# @Python: 3.9.7                            #
# ========================================= #
# @Description: “计算TNT数量”按钮的功能函数   #
# ========================================= #
from tkinter import messagebox
from src.modules.calTNT_flat import TNTConfigForFlat
from src.modules.calTNT_eject import TNTConfigForEjection


def func_calc_button(cls) -> None:

    """
    "计算TNT当量"按钮的功能
    """

    # ------ 平射配置 ------ #
    if cls.angel.get() == "flat":
        # 尝试计算TNT数量与方向
        try:
            direction, TNT_config = TNTConfigForFlat.config(
                x_target=int(cls.x_input.get()), z_target=int(cls.z_input.get()), 
                x_0=float(cls.x0_input.get()), z_0=float(cls.z0_input.get()),
                max_TNT=int(cls.max_tnt_input.get()), settings=cls.settings
            )
        # 出错时显示弹窗
        except Exception:
            messagebox.showerror(
                title=cls.LANGUAGE[cls.lang]["error_frame"]["title"], 
                message=cls.LANGUAGE[cls.lang]["error_frame"]["error_message"]
            )
            return
        cls.direction.set(direction)
        cls.res_page.load_TNT_config(TNT_config, cls.settings)

    # ------ 抛射配置 ------ #
    if cls.angel.get() == "eject":
        # 尝试计算TNT数量与方向
        try:
            direction, TNT_config = TNTConfigForEjection.config(
                x_target=int(cls.x_input.get()), z_target=int(cls.z_input.get()), 
                x_0=float(cls.x0_input.get()), z_0=float(cls.z0_input.get()),
                max_TNT=int(cls.max_tnt_input.get()), settings=cls.settings
            )
        # 出错时显示弹窗
        except Exception:
            messagebox.showerror(
                title=cls.LANGUAGE[cls.lang]["error_frame"]["title"], 
                message=cls.LANGUAGE[cls.lang]["error_frame"]["error_message"]
            )
            return
        cls.direction.set(direction)
        cls.res_page.load_TNT_config(TNT_config, cls.settings)
