from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtCore import QTimer, QDateTime
from PyQt6.QtWidgets import QLabel

from psutil import cpu_percent, virtual_memory


class Status(QStatusBar):
    # message 显示临时信息
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()
        self.showTime()
        self.settings()

    def load_widgets(self):
        self.computer = ComputerMSG()
        self.addPermanentWidget(self.computer)

    def showTime(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.__showTime)
        self.timer.start()

    def __showTime(self):
        nowTime = QDateTime().currentDateTime()
        timeFormat = nowTime.toString('yyyy年MM月dd日 hh:mm:ss')
        self.showMessage(timeFormat)

    def settings(self):
        self.setStyleSheet("""
            color: #fff;
        """)


class ComputerMSG(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.showMessage()
        self.refresh()

    def refresh(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.__refresh)
        self.timer.start(1000)

    def __refresh(self):
        self.showMessage()

    def showMessage(self):
        CPU, VIRTUAL = self.getMessage()
        self.setText(f"CPU: \t\t{CPU}%\nVIRTUAL: \t{VIRTUAL}%")

    @staticmethod
    def getMessage():
        CPU = cpu_percent()
        VIRTUAL = virtual_memory()[2]
        return CPU, VIRTUAL
