from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt

from .child_widgets import Status


class StatPart(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()
        self.settings()

    def load_widgets(self):
        self.status = Status()
        self.addWidget(self.status)

    def settings(self):
        self.setAlignment(Qt.AlignmentFlag.AlignBottom)

