from PyQt5 import QtWidgets
import UI
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginWin = UI.Login()#创建QT对象
    loginWin.show()#QT对象显示
    sys.exit(app.exec_())
