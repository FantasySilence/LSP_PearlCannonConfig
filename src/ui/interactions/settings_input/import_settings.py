# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 导入设置文件按钮的功能  #
# =================================== #
import json
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


def import_func(cls) -> None:

    """
    导入设置设置功能
    """

    # ------ 导入文件窗口 ------ #
    file_path = askopenfilename(
        title=" ",
        filetypes=[("JSON files", "*.json")]
    )
    if not file_path:
        return
    
    # ------ 读取导入的设置文件 ------ #
    try:
        with open(file_path, encoding="utf-8") as f:
            settings = json.load(f)
    except Exception:
        messagebox.showerror(
            title=cls.LANGUAGE[cls.lang]["error_frame"]["title"], 
            message=cls.LANGUAGE[cls.lang]["error_frame"]["error_message"]
        )
    
    # ------ 将设置填入模板，便于形成预览 ------ #
    try:
        if settings["IS_EJECTION_AVAILABLE"]:
            params_inputed = {
                "basic": {
                    "x0": settings["XZ_INIT_POSITION"]["X"],
                    "z0": settings["XZ_INIT_POSITION"]["Z"],
                    "max_tnt": settings["MAX_TNT"],
                    "tnt_per_unit": settings["MAX_TNT_UNIT"]
                },
                "flat": {
                    "y0": settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_POSITION"],
                    "y_init_motion": settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_MOTION"],
                    "xz": settings["MOTION_FOR_FLAT_FIRE"]["XZ_MOTION"],
                    "y_motion": settings["MOTION_FOR_FLAT_FIRE"]["Y_MOTION"]
                },
                "eject": {
                    "y0": settings["MOTION_FOR_EJECTIONS"]["Y_INIT_POSITION"],
                    "y_init_motion": settings["MOTION_FOR_EJECTIONS"]["Y_INIT_MOTION"],
                    "xz": settings["MOTION_FOR_EJECTIONS"]["XZ_MOTION"],
                    "y_motion": settings["MOTION_FOR_EJECTIONS"]["Y_MOTION"]
                }
            }
            cls.res_frame.communicate(settings["IS_EJECTION_AVAILABLE"], params_inputed)
        else:
            params_inputed = {
            "basic": {
                "x0": settings["XZ_INIT_POSITION"]["X"],
                "z0": settings["XZ_INIT_POSITION"]["Z"],
                "max_tnt": settings["MAX_TNT"],
                "tnt_per_unit": settings["MAX_TNT_UNIT"]
            },
            "flat": {
                "y0": settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_POSITION"],
                "y_init_motion": settings["MOTION_FOR_FLAT_FIRE"]["Y_INIT_MOTION"],
                "xz": settings["MOTION_FOR_FLAT_FIRE"]["XZ_MOTION"],
                "y_motion": settings["MOTION_FOR_FLAT_FIRE"]["Y_MOTION"]
            }
        }
        cls.res_frame.communicate(settings["IS_EJECTION_AVAILABLE"], params_inputed)
    except Exception:
        messagebox.showerror(
            title=cls.LANGUAGE[cls.lang]["error_frame"]["title"], 
            message=cls.LANGUAGE[cls.lang]["error_frame"]["error_message"]
        )
