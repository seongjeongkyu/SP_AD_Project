import sys
from PyQt5.QtWidgets import (QPushButton,
    QApplication, QLineEdit, QDialog, QSizePolicy, QGridLayout, QToolButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from keyList import keyList
import papagoApi


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class TransBot(QDialog):


    def __init__(self):
        super().__init__()
        self.initUI()
        self.result = '번역할 문장을 적어줘'

    def initUI(self):
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.textbox = QLineEdit()

        keyLayout = QGridLayout()
        buttonGroups = {'buttons' : keyList, 'layout': keyLayout, 'columns' : 7}
        r = 0; c = 0
        for btnText in buttonGroups['buttons']:
            button = Button(btnText, self.buttonClicked)
            buttonGroups['layout'].addWidget(button, r, c)
            c += 1
            if c >= buttonGroups['columns']:
                c = 0; r += 1

        sendButton = QPushButton('번역')
        sendButton.clicked.connect(self.buttonClicked)

        vbox = QVBoxLayout()
        vbox.addLayout(keyLayout)
        vbox.addWidget(self.textbox)
        keyLayout.addWidget(sendButton)
        self.setLayout(vbox)
        self.setWindowTitle('뽕순이 번역기')
        self.setGeometry(800, 300, 500, 150)

    def buttonClicked(self):
        try:
            button = self.sender()
            key = button.text()
            if key in keyList:
                global outputKey
                outputKey = keyList[key]
            if key == '번역':
                text = self.textbox.text()
                self.result = papagoApi.papago(text, outputKey)
                self.hide()
        except:
            self.result = "지원하지 않는 번역이야. 다시 입력해줘"
            self.hide()


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    t = TransBot()
    t.show()
    sys.exit(app.exec_())

def run():
    t = TransBot()
    t.exec_()
    return t.result