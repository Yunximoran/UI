from PyQt6.QtWidgets import QLabel, QScrollArea, QWidget, QHBoxLayout
from PyQt6.QtGui import QPalette, QPixmap, QBrush
from PyQt6.QtCore import Qt

import os
import cv2
from multiprocessing import Process

from self_layout import FlowLayout
from database import DBManager

MYDB = DBManager()
ALL_APPLICATION = MYDB.getAppInfo()


class AppTab(QScrollArea):
    COLUMNS = 8

    def __init__(self, *args, **kwargs):
        super(AppTab, self).__init__(*args, **kwargs)
        self.tabLayout = QHBoxLayout()
        self.tabSpace = TabSpace()
        self.tabLayout.addWidget(self.tabSpace)
        self.setWidget(self.tabSpace)
        self.setWidgetResizable(True)
        self.setLayout(self.tabLayout)
        # self.tabSpace = TabSpace(self)    # 窗口默认尺寸30， 100,
        # 想要子窗口填充父窗口需要使用布局
        # print(type(self), self.height())
        # print(type(self), self.width())

    # def load_items(self):
    #     self.addScrollBarWidget()
    # 要不要试下手动输入尺寸，resize

    # def resizeEvent(self, a0):
    #     size = a0.size()
    #     h, w = size.height(), size.width()
    #     print(h, w)
    #     # self.tabSpace.setMinimumWidth(w)
    #     # self.tabSpace.setMaximumWidth(w)


class TabSpace(QWidget):
    def __init__(self, *args, **kwargs):
        super(TabSpace, self).__init__(*args, **kwargs)
        self.__settings()
        self.load_items()

    def load_items(self):
        for appName, appPath in ALL_APPLICATION:
            self.appTabLayout.addWidget(AppItem(self, appName, appPath))

    def __settings(self):
        self.appTabLayout = FlowLayout(self)
        # self.setLayout(self.appTabLayout)
        # print(type(self.parent()))


# class AppTabLayout(FlowLayout):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.load_items()

# def load_items(self):
#     pass


class AppItem(QLabel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        # self.setText(title)
        self.setParent(parent)
        self.settings()
        try:
            self.appName = args[0]
            self.appPath = args[1]
        except IndexError:
            pass

    def paintEvent(self, a0):
        pass

    def mouseDoubleClickEvent(self, ev):
        if ev.button() == Qt.MouseButton.LeftButton:
            print("The is LeftButton Event")
            try:
                print(self.appName)
                print(self.appPath)
                Process(target=self.runApp, args=(self.appPath,)).start()
            except AttributeError:
                pass

    @staticmethod
    def runApp(path):
        # 创建新进程启动程序
        os.startfile(path)

    def enterEvent(self, event):
        # 这里要实现悬浮窗
        print(self.appName)

    def leaveEvent(self, a0):
        pass

    # def setIcon(self):
    #     pass

    def settings(self):
        self.setStyleSheet("""
            background-color: #333;
            border-radius: 12px;
        """)
        self.setMinimumSize(160, 160)
        self.setMaximumSize(240, 240)


def scaled(img, ih):
    pass


if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    tw = AppTab()
    tw.show()
    sys.exit(app.exec())
