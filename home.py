from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

import sys

from MainPart import BaseLayout

from PyQt6.QtWidgets import QLabel

APPLICATION = QApplication(sys.argv)


class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.show()
        sys.exit(APPLICATION.exec())

    def settings(self):
        self.setGeometry(180, 60, 1080, 720)
        self.setWindowTitle("Home")
        self.setLayout(BaseLayout())
        self.setStyleSheet("""
            background-color: #bebebe;
        """)


# 应用的功能
# 常用软件启动器？？？
# 自定义工具集合
"""
菜单栏、主窗口、底部状态栏，CPU、当前时间（年月日时分秒）
"""

if __name__ == '__main__':
    Home()
