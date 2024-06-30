# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-30                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Description: 输入框输入验证         #
# =================================== #

def validate_number(x: str) -> bool:
    
    """
    验证输入的字符是否为数字
    """

    # ------ 确保负数也能正确的识别出来 ------ #
    try:
        str_to_validate = x[1:]
    except IndexError:
        str_to_validate = x

    # ------ 判断输入的字符是否满足条件 ------ #
    if str_to_validate.isdigit():
        return True
    elif str_to_validate == "":
        return True
    else:
        return False
