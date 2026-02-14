from PyQt5.QtCore import Qt

from controls.gulpease_panel import GulpeasePanel
from controls.index_panel import IndexPanel
from controls.info_panel import InfoPanel
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QFrame

class BottomPanel(QWidget):
    def __init__(self, file):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.file = file

        info_panel = InfoPanel(file.words_num, file.unique_words_num, file.sentences_num, file.letters_num)
        self.layout.addWidget(info_panel, 0, 0)

        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line, 0, 1)

        gulpease_index, grades = file.calculate_gix()
        gulpease_panel = GulpeasePanel(gulpease_index, grades, has_header=True)
        self.layout.addWidget(gulpease_panel, 0, 2)

        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line, 0, 3)

        lix = file.calculate_lix()
        lix_legend = ("""
            <p> It measures the variety of words used in a text, helping to assess the richness or variation in vocabulary </p><br>
            <p> Percentage value where higher value means more words variety </p> 
        """)
        lix_panel = IndexPanel("Lexical diversity index", lix, lix_legend)
        self.layout.addWidget(lix_panel, 0, 4)

        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(line, 0, 5)

        scix = file.calculate_scix()
        scix_legend = ("""
            <p> It measures the complexity of sentence structure in a text </p><br>
            <p> Higher value means higher syntactic complexity </p> 
        """)
        scix_panel = IndexPanel("Syntactic complexity index", scix, scix_legend)
        self.layout.addWidget(scix_panel, 0, 6)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setColumnStretch(3, 1)
        self.layout.setColumnStretch(4, 1)
        self.layout.setColumnStretch(5, 1)
        self.layout.setColumnStretch(6, 1)
