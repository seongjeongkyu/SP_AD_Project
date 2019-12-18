from PyQt5.QtGui import *
import sys
import chatResponse
import transUI
from PyQt5 import QtTest
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QTextEdit, QLineEdit, QScrollArea, QGroupBox, QFormLayout)

class ChatBot(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = QLabel()
        pixmap = ("Image.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))
        self.initUI()

    def initUI(self):
        self.lineLayOut = QFormLayout()
        self.lineLayOut.addRow(self.lbl, self.makeTextBox('뽕순이랑 얘기하자 ㅎㅎ 번역을 원하면 "번역해줘" 라고 보내~'))
        self.chatbox = QGroupBox()
        self.chatbox.setLayout(self.lineLayOut)
        self.chatscroll = QScrollArea()
        self.chatscroll.setWidget(self.chatbox)
        self.chatscroll.setWidgetResizable(True)
        self.textbox = QLineEdit()
        self.sendButton = QPushButton('Send')
        self.sendButton.clicked.connect(self.buttonClicked)

        oImage = QImage("./Image1.JPG")
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))
        self.setPalette(palette)

        hbox = QHBoxLayout()
        hbox.addWidget(self.textbox)
        hbox.addWidget(self.sendButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.chatscroll)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('♥뽕순이와의 채팅방♥')
        self.setGeometry(300, 300, 500, 600)

    def makeTextBox(self, t):
        text = QTextEdit(t)
        text.setMaximumHeight(60)
        return text

    def buttonClicked(self):
        self.lbl = QLabel(self)
        pixmap = ("Image.jpg")
        self.lbl.setPixmap(QPixmap(pixmap))
        mytext = self.textbox.text()
        mytextedit = QLineEdit(mytext)
        self.lineLayOut.addRow(QLabel("나"), mytextedit)
        self.textbox.clear()

        QtTest.QTest.qWait(300)

        if mytext == '번역해줘' :
            self.lineLayOut.addRow(self.lbl, self.makeTextBox("번역을 시작할게! 문장을 적고 원하는 언어를 클릭한     후, 번역 버튼을 눌러!"))
            self.lbl = QLabel(self)
            pixmap = ("Image.jpg")
            self.lbl.setPixmap(QPixmap(pixmap))
            self.lineLayOut.addRow(self.lbl, self.makeTextBox(transUI.run()))
        else :
            response = chatResponse.chatRecognizing(mytext)
            self.lineLayOut.addRow(self.lbl, self.makeTextBox(response))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatBot()
    ex.show()
    sys.exit(app.exec_())