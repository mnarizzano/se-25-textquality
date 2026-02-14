import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QTextEdit, QFileDialog, QMessageBox, \
    QGridLayout, QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QLabel, QProgressDialog
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtCore import Qt

from base_vocabulary import BaseVocabulary
from controls.bottom_panel import BottomPanel
from controls.main_panel import MainPanel
from word_file import WordFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text quality evaluator")
        self.setGeometry(100, 100, 1000, 800)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        open_icon = QIcon("icons/open.png")
        open_action = QAction(open_icon, "Open file", self)
        open_action.triggered.connect(self.load_file)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.toolbar.addAction(open_action)
        self.docx_file = None
        self.base_voc = None

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.main_layout = QVBoxLayout()
        self.container.setLayout(self.main_layout)

        self.welcome_label = QLabel("Welcome to Text quality evaluator\n please load a .docx file to start")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 18px; color: gray;")
        self.main_layout.addWidget(self.welcome_label)

    def load_file(self):
        if self.docx_file is not None:
            result = QMessageBox.question(self, "Warning",
                                  "A file has already been loaded. Are you sure you want to load another one?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if result != QMessageBox.Yes:
                return

        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "File Word(*.docx);;Tutti i file (*.*)")
        if file_path:
            try:
                if self.base_voc is None:
                    self.base_voc = BaseVocabulary()
                self.docx_file = WordFile(file_path)
                if self.docx_file.words_num == 0:
                    _ = QMessageBox.critical(self, "Warning",
                                          "File has no words",
                                          QMessageBox.Ok)
                    return
                if self.docx_file.lang:
                    if self.docx_file.lang != "it":
                        _ = QMessageBox.warning(self, "Warning",
                                                 f"Detected a non italian document ({self.docx_file.lang}) \nResults may be inconsistent.",
                                                 QMessageBox.Ok)

                container = QWidget()
                self.setCentralWidget(container)

                main_layout = QVBoxLayout()
                container.setLayout(main_layout)

                if self.welcome_label is not None:
                    self.welcome_label.deleteLater()
                    self.welcome_label = None

                main_panel = MainPanel(self.docx_file, self.base_voc)
                main_layout.addWidget(main_panel)

                bottom_panel = BottomPanel(self.docx_file)
                main_layout.addWidget(bottom_panel, 0)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error has occurred:\n{str(e)}")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
