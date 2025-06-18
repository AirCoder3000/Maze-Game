from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
import random
from random import choice

# main window:
app = QApplication([])
window = QWidget()
window.setWindowTitle('Try your luck, friend!')
window.resize(600, 300)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')

btn1 = QPushButton('A')
btn2 = QPushButton('B')
btn3 = QPushButton('C')


layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()    

layoutH1.addWidget(button1, alignment = Qt.AlignLeft)
layoutH1.addWidget(button2, alignment = Qt.AlignRight)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button4, alignment = Qt.AlignLeft)
layoutH3.addWidget(button5, alignment = Qt.AlignRight)
layoutH4.addWidget(btn1, alignment= Qt.AlignCenter)
layoutH5.addWidget(btn2, alignment = Qt.AlignLeft)
layoutH5.addWidget(btn3, alignment = Qt.AlignRight)


layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
layoutV.addLayout(layoutH4)
layoutV.addLayout(layoutH5)
window.setLayout(layoutV)

buttons = [button1, button2, button3, button4, button5, btn1, btn2, btn3]
rng = random.choice(buttons)
#print(rng)

def button_clicked():
    win = QLabel('You Win !')
    layoutV.addWidget(win, alignment=Qt.AlignCenter)

rng.clicked.connect(button_clicked)

window.show()
app.exec_()
