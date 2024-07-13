# ============================================= #
# @Author: Fantasy_Silence                      #
# @Time: 2024-07-13                             #
# @IDE: Visual Studio Code & PyCharm            #
# @Python: 3.9.7                                #
# ============================================= #
# @Description: 用户输入界面的语言设置功能        #
# ============================================= #

def update_language_in_user_input(cls, lang: str) -> None:

    """
    更新语言设置
    """

    # ------ 通信，获取语言设置 ------ #
    cls.lang = lang

    # ------ 更新标签语言 ------ #
    cls.input_frame.config(
        text=cls.LANGUAGE[lang]["input_frame"]["input_labelframe_text"],
    )

    # ------ 更新炮口坐标 ------ #
    cls.origin_x_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["original_x"],
    )  
    cls.origin_z_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["original_z"],
    )

    # ------ 更新目的地坐标 ------ #
    cls.target_x_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["target_x"],
    )  
    cls.target_z_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["target_z"],
    )

    # ------ 更新最大TNT数量 ------ #
    cls.TNT_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["max_tnt"],
    )

    # ------ 更新珍珠发射角度 ------ #
    cls.angle_label.config(
        text=cls.LANGUAGE[lang]["input_frame"]["angle"],
    )
    cls.flat_buttons.config(
        text=cls.LANGUAGE[lang]["input_frame"]["flat"],
    )
    cls.eject_buttons.config(
        text=cls.LANGUAGE[lang]["input_frame"]["eject"],
    )

    # ------ 更新操作按钮的语言 ------ #
    cls.calc_button.config(
        text=cls.LANGUAGE[lang]["input_frame"]["button_cal_tnt"],
    )
    cls.simulation_button.config(
        text=cls.LANGUAGE[lang]["input_frame"]["button_pearl_simu"],
    )
    cls.upload_button.config(
        text=cls.LANGUAGE[lang]["input_frame"]["button_settings"],
    )
    cls.exit_button.config(
        text=cls.LANGUAGE[lang]["input_frame"]["button_exit"],
    )