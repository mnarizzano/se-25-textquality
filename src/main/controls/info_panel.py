import customtkinter as ctk
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel


class InfoPanel(QWidget):
    def __init__(self, words, unique_words, sentences, letters):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        title_label = QLabel("Info")
        title_label.setFixedHeight(20)
        title_label.setStyleSheet("padding: 0px 2px 0px 2px; background-color: lightgray; font-weight: bold; border:1px solid gray;")
        title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title_label, 0, 0, 1, 2)

        words_label = QLabel(text="words")
        self.layout.addWidget(words_label, 1, 0, alignment=Qt.AlignCenter)
        words_value_label = QLabel(text=str(words))
        self.layout.addWidget(words_value_label, 1, 1, alignment=Qt.AlignCenter)

        unique_words_label = QLabel(text="unique words")
        self.layout.addWidget(unique_words_label, 2, 0, alignment=Qt.AlignCenter)
        unique_words_value_label = QLabel(text=str(unique_words))
        self.layout.addWidget(unique_words_value_label, 2, 1, alignment=Qt.AlignCenter)

        sentences_label = QLabel(text="sentences")
        self.layout.addWidget(sentences_label, 3, 0, alignment=Qt.AlignCenter)
        sentences_value_label = QLabel(text=str(sentences))
        self.layout.addWidget(sentences_value_label, 3, 1, alignment=Qt.AlignCenter)

        letters_label = QLabel(text="letters")
        self.layout.addWidget(letters_label, 4, 0, alignment=Qt.AlignCenter)
        letters_value_label = QLabel(text=str(letters))
        self.layout.addWidget(letters_value_label, 4, 1, alignment=Qt.AlignCenter)

