from PyQt6.QtWidgets import QHBoxLayout

from .child_layout import *


class CorePart(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()
        self.load_layouts()

    def load_layouts(self):
        self.core_mid_part = CoreMidPart()
        self.core_right_part = CoreRightPart()
        self.addLayout(self.core_mid_part, 7)
        self.addLayout(self.core_right_part, 1)

    def load_widgets(self):
        pass

    def settings(self):
        self.setContentsMargins(10, 0, 10, 0)
        self.setSpacing(10)