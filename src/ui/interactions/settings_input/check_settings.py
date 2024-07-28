# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 查看当前设置按钮的功能  #
# =================================== #
import json
from src.common.filesio import FilesIO


def check_func(cls) -> None:

        """
        查看当前设置功能
        """

        # ------ 读取当前设置 ------ #
        with open(FilesIO.load_json("settings.json")) as f:
            settings = json.load(f)
        
        # ------ 将设置填入模板，便于形成预览 ------ #
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