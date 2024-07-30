# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description:                       #
# =================================== #
from ttkbootstrap.constants import *   


def load(
        cls, is_eject_available: bool, params: dict, lang: str, language: dict
) -> None:

    """
    与设置输入界面进行通信
    params: 填入模板的参数
    lang: 语言标识符
    language: 语言设置文件
    """

    # ------ 预览文本 ------ #
    if is_eject_available:
        text = \
        f"""
        {{
            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_1"]}
            "IS_EJECTION_AVAILABLE": {is_eject_available},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_2"]}
            "MAX_TNT": {params["basic"]["max_tnt"]},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_3"]}
            "MAX_TNT_UNIT": {params["basic"]["tnt_per_unit"]},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_4"]}
            "XZ_INIT_POSITION": {{
                "X": {params["basic"]["x0"]},
                "Z": {params["basic"]["z0"]}
            }},

            "MOTION_FOR_FLAT_FIRE": {{
                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_5"]}
                "XZ_MOTION": {params["flat"]["xz"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_6"]}
                "Y_MOTION": {params["flat"]["y_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_7"]}
                "Y_INIT_MOTION": {params["flat"]["y_init_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_8"]}
                "Y_INIT_POSITION": {params["flat"]["y0"]}
            }},

            "MOTION_FOR_EJECTIONS": {{
                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_9"]}
                "XZ_MOTION": {params["eject"]["xz"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_10"]}
                "Y_MOTION": {params["eject"]["y_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_11"]}
                "Y_INIT_MOTION": {params["eject"]["y_init_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_12"]}
                "Y_INIT_POSITION": {params["eject"]["y0"]}
            }}
        }}
        """
    else:
        text = \
        f"""
        {{
            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_1"]}
            "IS_EJECTION_AVAILABLE": {is_eject_available},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_2"]}
            "MAX_TNT": {params["basic"]["max_tnt"]},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_3"]}
            "MAX_TNT_UNIT": {params["basic"]["tnt_per_unit"]},

            # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_4"]}
            "XZ_INIT_POSITION": {{
                "X": {params["basic"]["x0"]},
                "Z": {params["basic"]["z0"]}
            }},

            "MOTION_FOR_FLAT_FIRE": {{
                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_5"]}
                "XZ_MOTION": {params["flat"]["xz"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_6"]}
                "Y_MOTION": {params["flat"]["y_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_7"]}
                "Y_INIT_MOTION": {params["flat"]["y_init_motion"]},

                # {language[lang]["settings_frame"]["preview_frame"]["preview_text"]["row_8"]}
                "Y_INIT_POSITION": {params["flat"]["y0"]}
            }}
        }}
        """
    
    # ------ 去掉多余的缩进 ------ #
    formated_text = "\n".join([
        line[8:] if len(line) > 8 else line
        for line in text.split('\n')
    ])
    formated_text = formated_text.strip()

    # ------ 插入到预览框中 ------ #
    cls.text_area.configure(state=NORMAL)
    cls.text_area.delete(1.0, END)
    cls.text_area.insert(END, formated_text)
    cls.text_area.configure(state=DISABLED)
