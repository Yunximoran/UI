from PyQt6.QtWidgets import QHBoxLayout, QLabel, QListWidget


class RecommendationList(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_items()

    def load_items(self):
        self.item1 = Item()
        self.item1.setText("hello")
        self.addItem("t1")
        self.setItemWidget(self.item(0), self.item1)


class Item(QLabel):
    def __init__(self):
        super().__init__()
        self.settings()

    def settings(self):
        self.setStyleSheet("""
            background-color: #474449;
        """)

    def mousePressEvent(self, ev):
        print("Hello World!")
