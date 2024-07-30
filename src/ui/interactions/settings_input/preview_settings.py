# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 预览按钮的功能         #
# =================================== #
from tkinter import messagebox


def preview_func(cls) -> None:

    """
    预览功能
    """

    try:
        is_eject_available = cls.eject_switch.get() == "normal"
        params_inputed = {
            "basic": {
                "x0": float(cls.x0_input.get()),
                "z0": float(cls.z0_input.get()),
                "max_tnt": int(cls.max_tnt_input.get()),
                "tnt_per_unit": int(cls.tnt_per_unit.get())
            },
            "flat": {
                "y0": float(cls.y0_flat.get()),
                "y_init_motion": float(cls.y_init_motion_f.get()),
                "xz": float(cls.xz_flat.get()),
                "y_motion": float(cls.y_flat_motion.get()) - float(cls.y_init_motion_f.get())
            },
            "eject": {
                "y0": float(cls.y0_eject.get()),
                "y_init_motion": float(cls.y_init_motion_e.get()),
                "xz": float(cls.xz_eject.get()),
                "y_motion": float(cls.y_eject_motion.get()) - float(cls.y_init_motion_e.get())
            }
        }
        cls.res_frame.communicate(is_eject_available, params_inputed)
    except Exception:
        messagebox.showerror(
            title=cls.LANGUAGE[cls.lang]["error_frame"]["title"], 
            message=cls.LANGUAGE[cls.lang]["error_frame"]["error_message"]
        )
