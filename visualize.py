from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QVBoxLayout
import sys
from PyQt6.QtGui import QIcon
from pyperclip import copy
from num2words import num2words

import generate

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minesweeper About Me")
        self.setWindowIcon(QIcon("banan.jpg"))
        self.setGeometry(500,300,400,300)

        stylesheet = (
            'background-color:rgb(29, 29, 38); color:rgb(179, 179, 212)'
        )
        self.setStyleSheet(stylesheet)
        
        self.create()

    def create(self):
        self.tb = QTextBrowser(self)
        self.btn = QPushButton('generate new field', self)
        self.btn.clicked.connect(self.visualize)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.btn)
        
        self.setLayout(vbox)
        
        self.show()
        
        self.visualize()
        
    def visualize(self):
        generatedField = generate.generate(4)

        self.tb.clear()
        field = ''
        for i in range(0, len(generatedField)):
            for j in generatedField[i]:
                if j == -1:
                    field = field + '💣'
                if -1 < j < 9:
                    field = field + str(j) + ' '
            field = field + '\n'
        text = ''
        for i in range(0, len(generatedField)):
            for j in generatedField[i]:
                if j == -1:
                    text = f'{text}||:bomb:||'
                if -1 < j < 9:
                    text = f'{text}||:{num2words(j)}:||'
            text = text + '\n'
        copy(text)
        self.tb.append(field)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())