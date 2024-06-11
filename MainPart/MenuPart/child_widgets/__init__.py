from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtGui import QAction
from .search import *
from .menu import *
from dispose.event import event_menu

MENU = CONF.MENU
ACTION = CONF.ACTION


class Search(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_widgets()
        self.settings()

    def band_btn_event(self):  # 两个组件之间的方法，在布局内设置
        self.search_btn.clicked.connect(self.__btn_event)

    def __btn_event(self):
        tags = self.search_box.text()
        print(tags)

    def load_widgets(self):
        self.search_box = SearchEdit()
        self.search_btn = SearchBtn()

        self.addWidget(self.search_box)
        self.addWidget(self.search_btn)
        self.band_btn_event()

    def settings(self):
        self.setSpacing(0)
        self.setAlignment(self.search_box, Qt.AlignmentFlag.AlignLeft)
        self.setAlignment(self.search_btn, Qt.AlignmentFlag.AlignLeft)


class Menu(QMenuBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buildMenuBar()
        self.bandAction()
        print(ACTION)

    def buildMenuBar(self, strut=MENU, parent=None):
        parent = parent if parent is not None else self
        for item in strut.keys():
            isMenu = isinstance(strut[item], dict)
            if isMenu:
                menu = QMenu(item, parent)
                parent.addMenu(menu)
                self.buildMenuBar(strut[item], parent=menu)
            else:
                action = QAction(item, parent)
                parent.addAction(action)
                ACTION[action] = strut[item]

    @staticmethod
    def bandAction():
        for act, event in ACTION.items():
            if event is None:
                continue
            # act.triggered.connect(event_menu.event_help)

    # xml中初始化项目配置数据库信息
    # 然后后面的数据交给数据库进行
    def SetMenus(self, menu):
        self.menu = menu
