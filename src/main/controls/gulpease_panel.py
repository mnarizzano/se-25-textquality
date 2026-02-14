from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout
from indexes.gulpease_index import GulpeaseGrade

class GulpeasePanel(QWidget):
    def __init__(self, index=0, grades=None, has_header=False):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(15)

        # magari aggiungere tooltip in cui si spiega cos'è

        i = QLabel(text=str(index))
        font = QFont()
        font.setPointSize(18)
        i.setFont(font)
        self.layout.addWidget(i, 2, 0, alignment=Qt.AlignCenter)

        column = 1
        for level in GulpeaseGrade.LEVELS.keys():
            level_label = QLabel(text=level)
            self.layout.addWidget(level_label, 1, column, alignment=Qt.AlignCenter)

            label_img = QLabel()
            pixmap = QPixmap(grades[level].img)
            label_img.setPixmap(pixmap)
            label_img.setScaledContents(True)
            self.layout.addWidget(label_img, 2, column, alignment=Qt.AlignCenter)

            column += 1

        if has_header:
            title_label = QLabel("Gulpease index")
            title_label.setFixedHeight(20)
            title_label.setStyleSheet("padding: 0px 2px 0px 2px; background-color: lightgray; font-weight: bold; border:1px solid gray;")
            title_label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(title_label, 0, 0, 1, column)

