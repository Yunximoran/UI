from PyQt6.QtWidgets import QTabWidget

from .app_tab import AppTab


class TabList(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.appTab = AppTab()
        self.addTab(self.appTab, "app set")
        self.setContentsMargins(0, 0, 0, 0)
        print(type(self), self.height())
        print(type(self), self.width())
