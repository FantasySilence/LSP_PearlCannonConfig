# =================================== #
# @Author: Fantasy_Silence            #
# @Time: 2024-06-28                   #
# @IDE: Visual Studio Code & PyCharm  #
# @Python: 3.9.7                      #
# =================================== #
# @Descript: 自动生成文件路径           #
# =================================== #
import os
import json


class FilesIO:

    """
    文件IO流, 用于读取文件
    """

    @staticmethod
    def load_json(filename: str) -> str:

        """
        加载JSON文件路径
        """

        src_path = os.path.dirname(os.path.dirname(__file__))
        ROOTPATH = os.path.dirname(src_path)
        resources_path = os.path.join(ROOTPATH, 'resources')
        settings_path = os.path.join(resources_path, 'settings')
        return os.path.join(settings_path, filename)
    
    @staticmethod
    def getFigPath(filename: str) -> str:

        """
        加载图片路径
        """

        src_path = os.path.dirname(os.path.dirname(__file__))
        ROOTPATH = os.path.dirname(src_path)
        resources_path = os.path.join(ROOTPATH, 'resources')
        images_path = os.path.join(resources_path, 'images')
        return os.path.join(images_path, filename)

    @staticmethod
    def getLanguage(filename: str) -> str:

        """
        加载语言包
        """

        src_path = os.path.dirname(os.path.dirname(__file__))
        ROOTPATH = os.path.dirname(src_path)
        resources_path = os.path.join(ROOTPATH, 'resources')
        language_path = os.path.join(resources_path, 'languages')
        return os.path.join(language_path, filename)
