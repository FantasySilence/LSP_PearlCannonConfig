# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-07-13                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 选中某一行时执行的功能  #
# =================================== #
from src.modules.config_transform import ConfigInfoTransform


def on_item_selected(cls, event) -> None:

    """
    当Treeview选中某一行时，将选中行的信息返回到用户输入界面
    """

    # ------ 获取选中行的标识符 ------ #
    selected_item = cls.treeview.focus()
    
    # ------ 获取该行的值 ------ #
    cls.item_values = cls.treeview.item(selected_item, 'values')

    # ------ 获取选中行的索引 ------ #
    item_id = cls.treeview.selection()[0]
    cls.item_index = cls.treeview.index(item_id)

    # ------ 更新TNT详细信息 ------ #
    blue_TNT, red_TNT = cls.item_values[2:4]
    blue_TNT_str, red_TNT_str = ConfigInfoTransform.translate(
        int(blue_TNT[:-2]), int(red_TNT[:-2]), settings=cls.settings
    )
    cls.blue_TNT_info.set(
        cls.LANGUAGE[cls.lang]["output_frame"]["blue_tnt_label"] + blue_TNT_str
    )
    cls.red_TNT_info.set(
        cls.LANGUAGE[cls.lang]["output_frame"]["red_tnt_label"] + red_TNT_str
    )