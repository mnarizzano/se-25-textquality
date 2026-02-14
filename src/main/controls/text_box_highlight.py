import customtkinter as ctk
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import QTextEdit, QSizePolicy
from PyQt5.QtCore import Qt


def classify_token(token, base_voc):
    if not token.is_alpha:
        return None

    lemma = token.lemma_.lower()
    if lemma in base_voc.fo or lemma in base_voc.au:
        return "base"
    elif lemma in base_voc.ad:
        return "alta_disponibilita"
    else:
        return "non_base"

class TextBoxHighlight(QTextEdit):
    def __init__(self, doc, base_voc):
        super().__init__()
        self.base_voc = base_voc
        self.doc = doc
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )

        for tok in doc.tokens:
            self.insert_word(tok)

        self.textChanged.connect(self.adapt)
        self._padding = 6

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adapt()

    def insert_word(self, word):
        cursor = self.textCursor()
        form = QTextCharFormat()

        tag = classify_token(word, self.base_voc)
        if tag == "non_base":
            form.setForeground(QColor("red"))
            form.setFontItalic(True)
        elif tag == "alta_disponibilita":
            form.setForeground(QColor("orange"))
            form.setFontItalic(True)
        else:
            form.setForeground(QColor("black"))

        cursor.insertText(word.text + " ", form)

    def adapt(self):
        doc = self.document()
        doc.setTextWidth(self.viewport().width())
        height = doc.size().height()
        self.setFixedHeight(int(height) + 10)