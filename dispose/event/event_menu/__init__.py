from PyQt6.QtWidgets import QFileDialog
from database import DBManager
import os

MYDB = DBManager()
MENU_STRUCT = None


class EventFile:
    def __init__(self):
        pass


class EventTools:
    def __init__(self):
        pass

    def add_application(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "choose application", "C:", "*.exe")
        if file_path:
            file_name = os.path.basename(file_path)
            MYDB.setAppInfo(file_name, file_path)
        else:
            print("null")

    def pos_application(self):
        pass
