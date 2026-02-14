from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from controls.gulpease_panel import GulpeasePanel
from controls.text_box_highlight import TextBoxHighlight
from word_file import WordFile
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QFrame, QHBoxLayout, QScrollArea, QSizePolicy


class MainPanel(QWidget):
    def __init__(self, file, base_voc):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        title_label = QLabel(file.doc.core_properties.title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            margin: 10px;
        """)

        self.main_layout.addWidget(title_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.grid_layout = QGridLayout(self.scroll_content)

        headers = ["Num", "Paragraphs", "Gulpease index"]
        for col, h in enumerate(headers):
            container = QWidget()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(5)
            label = QLabel(h)
            label.setStyleSheet("background-color: lightgray; font-weight: bold; border:1px solid gray;")
            label.setAlignment(Qt.AlignCenter)
            if h == "Gulpease index":
                icon_label = QLabel()
                icon_label.setPixmap(
                    QPixmap("icons/qmark.png").scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setToolTip("""
                    <p> Legibility index specific for italian language where 0 represent the lowest legibility and 100 the highest </p>
                    <p> Below the legend to know how difficult is to read the text based on the index value and the of instruction (elementary, middle and high school):</p><br>
                    <img src='icons/impossible.png' width='16' height='16'> Almost incomprehensible<br>
                    <img src='icons/really_hard.png' width='16' height='16'> Really hard<br>
                    <img src='icons/hard.png' width='16' height='16'> Hard <br>
                    <img src='icons/easy.png' width='16' height='16'> Easy <br>
                    <img src='icons/really_easy.png' width='16' height='16'> Really easy
                """)
                label.setLayout(layout)
                layout.addWidget(icon_label, 0, Qt.AlignRight)
            if h == "Paragraphs":
                icon_label = QLabel()
                icon_label.setPixmap(
                    QPixmap("icons/qmark.png").scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                icon_label.setToolTip("""
                    <p> An <i style="color:red;">italic red</i> word means a Non-Base vocabulary word </p>
                    <p> An <i style="color:orange;">italic orange</i> word means an High-Disponibility vocabulary word</p>
                """)
                label.setLayout(layout)
                layout.addWidget(icon_label, 0, Qt.AlignRight)
            self.grid_layout.addWidget(label, 0, col)

        self.main_layout.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_content)

        row = 1
        row_count = 0
        for p in file.paragraphs:
            f = WordFile(text=p.text)
            if f.words_num == 0:
                continue

            row_count += 1
            label = QLabel(text=str(row_count))
            self.grid_layout.addWidget(label, row, 0)

            textbox = TextBoxHighlight(f, base_voc)
            textbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.grid_layout.addWidget(textbox, row, 1)

            container = QWidget()
            container_layout = QVBoxLayout(container)
            gulpease_index, grades = f.calculate_gix()
            gulpease_panel = GulpeasePanel(gulpease_index, grades)
            container_layout.addWidget(gulpease_panel)
            container_layout.addStretch()
            self.grid_layout.addWidget(container, row, 2)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            self.grid_layout.addWidget(line, row + 1, 0, 1, 3)

            row += 2
