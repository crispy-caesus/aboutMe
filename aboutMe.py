from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QVBoxLayout
import sys
from PyQt6.QtGui import QIcon
import random
from pyperclip import copy

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
        self.btn.clicked.connect(self.generate)
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.tb)
        vbox.addWidget(self.btn)
        
        self.setLayout(vbox)
        
        self.show()
        
        self.generate()
        
        
    def generate(self):
        field = [[],[],[],[]]
        for i in range(0, 4):
            for j in range(0, 4):
                if random.randint(0,100) < 26:
                    field[i].append(-1)
                    
                else:
                    field[i].append(0)

        for i in range(0, 4):
            for j in range(0, 4):
                if field[i][j] != -1:
                    if j != 3:
                        if field[i][j+1] == -1:
                            field[i][j] = field[i][j] + 1
                    if j != 0:
                            if field[i][j-1] == -1:
                                field[i][j] = field[i][j] + 1
                    if i != 0:
                        if field[i-1][j] == -1:
                            field[i][j] = field[i][j] + 1
                        if j != 0:
                            if field[i-1][j-1] == -1:
                                field[i][j] = field[i][j] + 1
                        if j != 3:
                            if field[i-1][j+1] == -1:
                                field[i][j] = field[i][j] + 1
                    if i != 3:
                        if field[i+1][j] == -1:
                            field[i][j] = field[i][j] + 1
                        if j != 0:
                            if field[i+1][j-1] == -1:
                                field[i][j] = field[i][j] + 1
                        if j != 3:
                            if field[i+1][j+1] == -1:
                                field[i][j] = field[i][j] + 1
        self.fieldd = field
        self.visualize()
        
    def visualize(self):
        self.tb.clear()
        field = ''
        for i in range(0, len(self.fieldd)):
            for j in self.fieldd[i]:
                if j == -1:
                    field = field + '💣'
                if j == 0:
                    field = field + '0  '
                if j == 1:
                    field = field + '1️  '
                if j == 2:
                    field = field + '2️  '
                if j == 3:
                    field = field + '3️  '
                if j == 4:
                    field = field + '4️  '
                if j == 5:
                    field = field + '5️  '
                if j == 6:
                    field = field + '6️  '
                if j == 7:
                    field = field + '7️  '
                if j == 8:
                    field = field + '8️  '
            field = field + '\n'
        text = ''
        for i in range(0, len(self.fieldd)):
            for j in self.fieldd[i]:
                if j == -1:
                    text = text + '||:bomb:||'
                if j == 0:
                    text = text + '||:zero:||'
                if j == 1:
                    text = text + '||:one:||'
                if j == 2:
                    text = text + '||:two:||'
                if j == 3:
                    text = text + '||:three:||'
                if j == 4:
                    text = text + '||:four:||'
                if j == 5:
                    text = text + '||:five:||'
                if j == 6:
                    text = text + '||:six:||'
                if j == 7:
                    text = text + '||:seven:||'
                if j == 8:
                    text = text + '||:eight:||'
            text = text + '\n'
        copy(text)
        self.tb.append(field)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())