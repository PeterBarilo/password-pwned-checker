from PyQt5.QtWidgets import *
import sys

class App(QDialog):

    def __init__(self):
        super(App, self).__init__()
        self.setGeometry(100, 100, 300, 400)
        self.formGroupBox = QGroupBox("Form 1")

        self.createForm()



app = QApplication([])
label = QLabel('Enter Password to Check')
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(QPushButton('Check'))
window.setLayout(layout)
window.show()
app.exec()
