from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from .MenuPart import MenuPart
from .StatPart import StatPart
from .CorePart import CorePart


# QVBoxLayout()
class BaseLayout(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_layout()

    def load_layout(self):
        # 布局的父属性不能是布局
        self.addLayout(MenuPart(), 0)
        self.addLayout(CorePart(), 10)
        self.addLayout(StatPart(), 0)

# class StatPart(QHBoxLayout):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

# 导入布局？？？， 布局定义组件， 组件绑定方法
