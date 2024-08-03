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

    # ------ 如果字符串为空，返回 False ------ #
    if x == "":
        return False
    
    # ------ 尝试将字符串转换为浮点数 ------ # 
    try:
        float(x)
        return True
    except ValueError:
        return False
