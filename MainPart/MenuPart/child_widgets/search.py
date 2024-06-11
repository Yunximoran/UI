from PyQt6.QtWidgets import QLineEdit, QPushButton
from PyQt6.QtCore import Qt


class SearchEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings()

    def settings(self):
        self.setStyleSheet("""
            background-color: #fff;
        """)
        self.setMaximumSize(600, 20)
        self.setMinimumSize(300, 20)

    def keyPressEvent(self, a0):
        super().keyPressEvent(a0)
        if a0.key() == Qt.Key.Key_Return:
            print(self.text())
        # if a0.modifiers()


class SearchBtn(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings()

    def settings(self):
        self.setStyleSheet("""
            background-color: #312434;
            border-radius: 6px;
            font: 10px;
        """)

        self.setText("搜索")
        self.setMaximumSize(45, 20)
        self.setMinimumSize(30, 20)
