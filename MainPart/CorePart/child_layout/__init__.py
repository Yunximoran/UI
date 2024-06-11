from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QTabWidget

from .recommendation import Item, RecommendationList
from .tabcard import TabList

import numpy as np

__all__ = ["CoreRightPart", "CoreMidPart"]

ALL_APPLICATION = [("YuanShen", r"D:\Yuncy Moran\Life\miHoYo\Genshin Impact\launcher.exe")]

BASE_NULL = np.full((4, 4), None)

# class CoreLeftPart(None):
#     pass
from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtGui import QIcon


class CoreMidPart(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addWidget(TabList())
        self.setContentsMargins(0, 0, 0, 0)
        # self.setSizeConstraint()  # 尺寸限制


class CoreRightPart(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()

    def load_widgets(self):
        self.rlist = RecommendationList()
        self.addWidget(self.rlist)
