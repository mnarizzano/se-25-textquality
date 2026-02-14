from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QHBoxLayout


class IndexPanel(QWidget):
    def __init__(self, title, index, tooltip_text=None):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.index = index
        self.title = title

        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        label = QLabel(title)
        label.setFixedHeight(20)
        label.setStyleSheet("background-color: lightgray; font-weight: bold; border:1px solid gray;")
        label.setAlignment(Qt.AlignCenter)

        if tooltip_text:
            icon_label = QLabel()
            icon_label.setPixmap(
                QPixmap("icons/qmark.png").scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setToolTip(tooltip_text)
            label.setLayout(layout)
            layout.addWidget(icon_label, 0, Qt.AlignRight)

        self.layout.addWidget(label, 0, 0,)
        index_label = QLabel(str(index))
        font = QFont()
        font.setPointSize(18)
        index_label.setFont(font)
        self.layout.addWidget(index_label, 1, 0, alignment=Qt.AlignCenter)