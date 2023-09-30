import sys
from PyQt5 import QtWidgets
def Pencere():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QApplication
    pencere.setWindowTitle("PyQt5 ders 1")
    pencere.show()
    sys.exit(app.exec_())

Pencere()