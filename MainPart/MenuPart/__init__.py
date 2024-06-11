from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtCore import Qt
from .child_widgets import Search, Menu


class MenuPart(QHBoxLayout):
    """
    菜单、 搜索框，确认按钮
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()
        self.settings()

    # 布局不能作为父属性
    def load_widgets(self):
        self.menu = Menu()
        self.search = Search()
        # self.search_left = SearchLeft()
        # self.search_right = SearchRight()

        self.addWidget(self.menu)
        self.addLayout(self.search)

    def settings(self):
        self.setAlignment(self.menu, Qt.AlignmentFlag.AlignLeft)
        self.setAlignment(self.search, Qt.AlignmentFlag.AlignRight)
