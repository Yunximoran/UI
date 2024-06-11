from PyQt6.QtWidgets import QMenu, QMenuBar, QFileDialog
from PyQt6.QtCore import Qt

import os

from database import DBManager

mydb = DBManager()


class MenuConf:
    def __init__(self):
        self.MENU = {
            "file": None,
            "tool": {
                "add application": self.tools_add_application_event,  # eval("self.tools_add_application_event"),
                "remove application": None,
                "func3": None
            },
            "setting": None,
            # "setting": {
            #     'background': self.background_event,
            #     "conf": None,   # 这里要弹出一个对话框，修改程序设置
            # },
            "help": self.help_event,
        }
        self.ACTION = {}

    @staticmethod
    def background_event(self):
        print("The is background event")

    @staticmethod
    def help_event(self):
        print("The is help event")

    @staticmethod
    def tools_add_application_event():
        file_dialog = QFileDialog()
        file_path, file_type = file_dialog.getOpenFileName(None, "find app address", r"C:", "*.exe")
        print(file_type)
        if file_path:
            file_name, suffix = os.path.basename(file_path).split('.')
            mydb.setAppInfo(file_name, file_path)
        else:
            print("not fond application")

    def tools_remove_application_event(self):
        pass


CONF = MenuConf()
