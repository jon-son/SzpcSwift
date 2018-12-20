from PyQt5 import QtWidgets
import homeUI
import sys



app = QtWidgets.QApplication(sys.argv)
loginWin = homeUI.Home()#创建QT对象
loginWin.show()#QT对象显示
sys.exit(app.exec_())
