from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.Qt import *
from API.Login import validateLogin
import time
from API.Swift import swiftFusion


class loginThread(QThread):
    trigger = QtCore.pyqtSignal(str)
    def __init__(self, UI):
        super(loginThread, self).__init__()
        self.account = UI.account
        self.passwd = UI.passwd

    def run(self):
        try:
            validate = validateLogin()
            result = validate.verification(self.account, self.passwd)[1]
            self.trigger.emit(result)
        except Exception as e:
            print(e)
            self.trigger.emit("E")

        time.sleep(3)
        self.trigger.emit("C")

class swiftThread(QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, UI):
        super(swiftThread, self).__init__()

    def run(self):
        result = ""
        try:
            swift = swiftFusion()
            result = swift.download("paas/", "inpaas.txt")
        except:
            self.trigger.emit("erro2")

        self.trigger.emit(result)

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(567, 424)
        self.background = QtWidgets.QLabel(Login)
        self.background.setGeometry(QtCore.QRect(0, 0, 567, 424))
        self.background.setObjectName("background")
        self.background.setText("")
        self.accountLine = QtWidgets.QLineEdit(self.background)
        self.accountLine.setGeometry(QtCore.QRect(70, 180, 431, 51))
        self.accountLine.setObjectName("accountLine")
        self.passwdLine = QtWidgets.QLineEdit(self.background)
        self.passwdLine.setGeometry(QtCore.QRect(70, 240, 431, 51))
        self.passwdLine.setObjectName("passwdLine")
        self.checkBox = QtWidgets.QCheckBox(self.background)
        self.checkBox.setGeometry(QtCore.QRect(70, 310, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.loginButton = QtWidgets.QPushButton(self.background)
        self.loginButton.setGeometry(QtCore.QRect(120, 342, 331, 45))
        self.loginButton.setObjectName("loginButton")
        self.bcLabel = QtWidgets.QLabel(self.background)
        self.bcLabel.setGeometry(QtCore.QRect(0, 0, 567, 155))
        self.bcLabel.setText("")
        self.bcLabel.setObjectName("bcLabel")
        self.logoLabel = QtWidgets.QLabel(self.bcLabel)
        self.logoLabel.setGeometry(QtCore.QRect(140, 5, 291, 161))
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.minButton = QtWidgets.QPushButton(self.bcLabel)
        self.minButton.setGeometry(QtCore.QRect(505, 10, 31, 31))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QPushButton(self.bcLabel)
        self.closeButton.setGeometry(QtCore.QRect(530, 10, 31, 31))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.popupLabel = QtWidgets.QLabel(self.background)
        self.popupLabel.setGeometry(QtCore.QRect(220, 160, 131, 41))
        self.popupLabel.setObjectName("popupLabel")
        self.popupLabel.setText("密码错误")
        self.popupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel.close()
        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "学会云"))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.accountLine.setPlaceholderText(_translate("Login", "请输入账号"))
        self.accountLine.setStyleSheet(
            '''#accountLine{
                border:1px solid gray;
                border-radius:20px;
                font-size:15px;
                padding-left:10px;
                font-family:"幼圆";
        }''')
        self.checkBox.setStyleSheet(
            '''#checkBox{
               font-family:"幼圆"; 

        }''')
        self.passwdLine.setStyleSheet(
            '''#passwdLine{
                border:1px solid gray;
                border-radius:20px;
                font-size:15px;
                padding-left:10px;
                font-family:"幼圆";
        }''')
        self.passwdLine.setEchoMode(QLineEdit.Password)
        self.passwdLine.setPlaceholderText(_translate("Login", "请输入密码"))
        self.checkBox.setText(_translate("Login", "记住密码"))
        self.loginButton.setText(_translate("Login", "登录"))
        self.loginButton.setStyleSheet(
            '''#loginButton{
                border-radius:20px;
                background-color:#3ca8ff;
                color:white;
                font-size:20px;
                font-family:"幼圆";
        }''')
        self.closeButton.setIcon(QIcon("icon/close.png"))
        self.closeButton.setStyleSheet(
            '''#closeButton{
                border-radius:20px;
            }''')
        self.minButton.setStyleSheet(
            '''#minButton{
                border-radius:20px;
            }''')
        self.minButton.setIcon(QIcon("icon/subtract.png"))
        self.bcLabel.setStyleSheet(
            '''#bcLabel{
                border-top:1px solid #e5e5e5;
                border-left:1px solid #e5e5e5;
                border-right:1px solid #e5e5e5;
                background-color:#4cb3ff;
            }''')
        pix = QPixmap('icon/logo.png')
        self.logoLabel.setPixmap(pix)
        self.logoLabel.setScaledContents(True)
        self.popupLabel.setStyleSheet(
            '''#popupLabel{
                border-radius:20px;
                background-color:rgb(0, 0, 0,50);
                font-size:15px;
                font-family:"幼圆";
                color:white;
            }''')
        self.background.setStyleSheet(
            '''#background{
                border:1px solid #e5e5e5;
                background-color:rgb(255, 255, 255);

            }''')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))





class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(1159, 770)
        self.mainFrame = QtWidgets.QFrame(Home)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1159, 791))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.topFrame = QtWidgets.QFrame(self.mainFrame)
        self.topFrame.setGeometry(QtCore.QRect(0, 0, 1159, 81))
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.logoLabel = QtWidgets.QLabel(self.topFrame)
        self.logoLabel.setGeometry(QtCore.QRect(30, 0, 181, 81))
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.settingButton = QtWidgets.QPushButton(self.topFrame)
        self.settingButton.setGeometry(QtCore.QRect(1035, 10, 31, 31))
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.minButton = QtWidgets.QPushButton(self.topFrame)
        self.minButton.setGeometry(QtCore.QRect(1070, 10, 31, 31))
        self.minButton.setText("")
        self.minButton.setObjectName("minButton")
        self.closeButton = QtWidgets.QPushButton(self.topFrame)
        self.closeButton.setGeometry(QtCore.QRect(1105, 10, 31, 31))
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.funsionFrame = QtWidgets.QFrame(self.mainFrame)
        self.funsionFrame.setGeometry(QtCore.QRect(0, 80, 1159, 51))
        self.funsionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.funsionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.funsionFrame.setObjectName("funsionFrame")

        self.downloadButton = QtWidgets.QPushButton(self.funsionFrame)
        self.downloadButton.setGeometry(QtCore.QRect(170, 10, 61, 31))
        self.downloadButton.setObjectName("downloadButton")
        self.deleteButton = QtWidgets.QPushButton(self.funsionFrame)
        self.deleteButton.setGeometry(QtCore.QRect(240, 10, 61, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.crearDirButton = QtWidgets.QPushButton(self.funsionFrame)
        self.crearDirButton.setGeometry(QtCore.QRect(310, 10, 71, 31))
        self.crearDirButton.setObjectName("crearDirButton")
        self.uploadButton = QtWidgets.QPushButton(self.funsionFrame)
        self.uploadButton.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.uploadButton.setObjectName("uploadButton")
        self.comboFrame = QtWidgets.QFrame(self.topFrame)
        self.comboFrame.setGeometry(QtCore.QRect(934, 32, 91, 51))
        self.comboFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.comboFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comboFrame.setObjectName("comboFrame")
        self.comboFrame.close()
        self.usernameButton = QtWidgets.QPushButton(self.topFrame)
        self.usernameButton.setGeometry(QtCore.QRect(934, 10, 91, 23))
        self.usernameButton.setObjectName("usernameButton")
        self.informationButton = QtWidgets.QPushButton(self.comboFrame)
        self.informationButton.setGeometry(QtCore.QRect(0, 0, 91, 23))
        self.informationButton.setObjectName("informationButton")
        self.changeButton = QtWidgets.QPushButton(self.comboFrame)
        self.changeButton.setGeometry(QtCore.QRect(0, 20, 91, 23))
        self.changeButton.setObjectName("changeButton")
        self.leftFrame = QtWidgets.QFrame(self.mainFrame)
        self.leftFrame.setGeometry(QtCore.QRect(0, 130, 161, 640))
        self.leftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftFrame.setObjectName("leftFrame")
        self.resourcesButton = QtWidgets.QPushButton(self.leftFrame)
        self.resourcesButton.setGeometry(QtCore.QRect(1, 40, 163, 51))
        self.resourcesButton.setText("")
        self.resourcesButton.setObjectName("resourcesButton")
        self.transmissionButton = QtWidgets.QPushButton(self.leftFrame)
        self.transmissionButton.setGeometry(QtCore.QRect(1, 100, 163, 51))
        self.transmissionButton.setText("")
        self.transmissionButton.setObjectName("transmissionButton")
        self.resourcesIcon = QtWidgets.QLabel(self.resourcesButton)
        self.resourcesIcon.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.resourcesIcon.setText("")
        self.resourcesIcon.setObjectName("resourcesIcon")
        self.resourcesLabel = QtWidgets.QLabel(self.resourcesButton)
        self.resourcesLabel.setGeometry(QtCore.QRect(60, 10, 71, 31))
        self.resourcesLabel.setObjectName("resourcesLabel")

        self.transmissionIcon = QtWidgets.QLabel(self.transmissionButton)
        self.transmissionIcon.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.transmissionIcon.setText("")
        self.transmissionIcon.setObjectName("transmissionIcon")
        self.transmissionLabel = QtWidgets.QLabel(self.transmissionButton)
        self.transmissionLabel.setGeometry(QtCore.QRect(60, 10, 71, 31))
        self.transmissionLabel.setObjectName("transmissionLabel")
        self.comboIcon = QtWidgets.QLabel(self.usernameButton)
        self.comboIcon.setGeometry(QtCore.QRect(60, 0, 25, 25))
        self.comboIcon.setText("")
        self.comboIcon.setObjectName("comboIcon")

        self.usernameLabel = QtWidgets.QLabel(self.usernameButton)
        self.usernameLabel.setGeometry(QtCore.QRect(10, 0, 60, 25))
        self.usernameLabel.setText("孙俊捷")
        self.usernameLabel.setObjectName("usernameLabel")

        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label_8 = QtWidgets.QLabel(self.leftFrame)
        self.label_8.setGeometry(QtCore.QRect(30, 600, 101, 21))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.leftFrame)
        self.label_9.setGeometry(QtCore.QRect(30, 560, 101, 41))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setUnderline(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.frame_6 = QtWidgets.QFrame(self.mainFrame)
        self.frame_6.setGeometry(QtCore.QRect(160, 130, 999, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(130, 5, 70, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("幼圆")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.breakButton = QtWidgets.QPushButton(self.frame_6)
        self.breakButton.setGeometry(QtCore.QRect(10, 5, 31, 31))
        self.breakButton.setText("")
        self.breakButton.setObjectName("breakButton")
        self.forwardButton = QtWidgets.QPushButton(self.frame_6)
        self.forwardButton.setGeometry(QtCore.QRect(50, 5, 31, 31))
        self.forwardButton.setText("")
        self.forwardButton.setObjectName("forwardButton")
        self.refreshButton = QtWidgets.QPushButton(self.frame_6)
        self.refreshButton.setGeometry(QtCore.QRect(90, 5, 31, 31))
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("refreshButton")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(205, 5, 54, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("幼圆")
        self.label_7.setFont(font)
        self.label_7.setText("/")
        self.label_7.setObjectName("label_7")

        self.frame_7 = QtWidgets.QFrame(self.mainFrame)
        self.frame_7.setGeometry(QtCore.QRect(160, 169, 999, 601))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")

        self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
        self.tableWidget.setGeometry(QtCore.QRect(8, 1, 990, 599))

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置tableWidget不能被编辑
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置tableWidget选择整行
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏tableWidget列表头
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.allcheckBox = QtWidgets.QCheckBox(self.tableWidget)
        self.allcheckBox.setGeometry(QtCore.QRect(0, 5, 15, 15))
        self.allcheckBox.setObjectName("allcheckBox")
        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "学会云"))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.informationButton.setText(_translate("Home", "修改资料"))
        self.changeButton.setText(_translate("Home", "切换账号"))
        self.downloadButton.setText(_translate("Home", "下载"))
        self.deleteButton.setText(_translate("Home", "删除"))
        self.crearDirButton.setText(_translate("Home", "新建文件夹"))
        self.uploadButton.setText(_translate("Home", "上传到学会云"))

        self.resourcesLabel.setText(_translate("Home", "全部资源"))

        self.transmissionLabel.setText(_translate("Home", "传输列表"))
        self.label_8.setText(_translate("Home", "     by jonson"))
        self.label_9.setText(_translate("Home", "学会云V1.0"))
        self.label_6.setText(_translate("Home", "当前位置："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Home", ""))
        self.tableWidget.setColumnWidth(0, 15)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Home", ""))
        self.tableWidget.setColumnWidth(1, 20)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Home", "名称"))
        self.tableWidget.setColumnWidth(2, 400)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Home", "文件大小"))
        self.tableWidget.setColumnWidth(3, 150)
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Home", "修改时间"))
        self.tableWidget.setColumnWidth(4, 150)
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Home", "修改者"))
        self.tableWidget.setColumnWidth(5, 150)

        self.checkBox = QCheckBox()
        self.tableWidget.setCellWidget(0, 0, self.checkBox)
        icon = QTableWidgetItem(QIcon("icon/type/dir.png"), "")
        self.tableWidget.setItem(0, 1, icon)
        self.tableWidget.setItem(0, 2, QTableWidgetItem("云计算V2.2"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("1.28M"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("2018-10-28 20:10"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("jonson"))
        self.checkBox = QCheckBox()
        self.tableWidget.setCellWidget(1, 0, self.checkBox)
        icon = QTableWidgetItem(QIcon("icon/type/word.png"), "")
        self.tableWidget.setItem(1, 1, icon)
        self.tableWidget.setItem(1, 2, QTableWidgetItem("三国演义.doc"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("2.28M"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("2018-10-28 20:10"))
        self.tableWidget.setItem(1, 5, QTableWidgetItem("jonson"))

        self.mainFrame.setStyleSheet(
            '''#mainFrame{
                background-color:white;
            }''')
        self.topFrame.setStyleSheet(
            '''#topFrame{
                border:1px solid #e5e5e5;
            }
            QPushButton{
                border:1px solid #e5e5e5;
                background-color:white;
            }''')
        self.funsionFrame.setStyleSheet(
            '''#funsionFrame{
                border:1px solid #e5e5e5;
                background-color:#fbfcfd;
            }
            QPushButton{
                border:1px solid #e5e5e5;
                background-color:white;
            }''')
        self.leftFrame.setStyleSheet(
            '''#leftFrame{
                border:1px solid #e5e5e5;
                background-color:#f0f2f5;

            }
            QPushButton{
                border:none;
            }''')
        self.resourcesButton.setStyleSheet(
            '''#resourcesButton{
                background-color:#e0e5ea;
            }
            #resourcesLabel{
                color:#4cb3ff;

                font-size:15px;
                font-family:"幼圆";
            }''')
        self.transmissionButton.setStyleSheet(
            '''#transmissionLabel{
                font-size:15px;
                font-family:"幼圆";
            }''')

        self.frame_6.setStyleSheet(
            '''#frame_6{
                border:1px solid #e5e5e5;

            }
            QPushButton{
                border:none;
                background-color:black;
            }''')

        self.frame_7.setStyleSheet(
            '''#frame_7{
                border:1px solid #e5e5e5;
            }
            ''')

        self.tableWidget.setStyleSheet(
            '''QTableWidget::item:selected {
                background-color: rgb(236, 241, 255);
                color:black;
            }''')
        self.uploadButton.setStyleSheet(
            '''#uploadButton{
                border:none;
                border-radius:10px;
                background-color:#4cb3ff;
                font-size:14px;
                font-family:"幼圆";
                color:white;
                font-weight:bold;
            }''')

        self.label_8.setStyleSheet(
            '''#label_8{
                 border-top:1px solid black;
            }''')

        pix1 = QPixmap('icon/logo_blue.png')
        self.logoLabel.setPixmap(pix1)
        self.logoLabel.setScaledContents(True)

        pix2 = QPixmap('icon/all_files.png')
        self.resourcesIcon.setPixmap(pix2)
        self.resourcesIcon.setScaledContents(True)

        pix3 = QPixmap('icon/combo.png')
        self.comboIcon.setPixmap(pix3)
        self.comboIcon.setScaledContents(True)

        pix3 = QPixmap('icon/list.png')
        self.transmissionIcon.setPixmap(pix3)
        self.transmissionIcon.setScaledContents(True)

        pix4 = QPixmap('icon/')

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(Qt.ArrowCursor))


class Login(QtWidgets.QMainWindow, Ui_Login):  # 创建一个Qt对象
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_Login.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        self.closeButton.clicked.connect(self.close)
        self.minButton.clicked.connect(self.showMinimized)
        self.loginButton.clicked.connect(self.login)

    def login(self):

        self.account = self.accountLine.text()
        self.passwd = self.passwdLine.text()
        if self.account != "" and self.passwd != "":
            self.threads = loginThread(self)
            self.threads.trigger.connect(self.loginDone)
            self.threads.start()

    def loginDone(self, flag):
        if flag == "F":
            self.popupLabel.show()
            self.popupLabel.setText("密码错误")
        elif flag == "E":
            self.popupLabel.show()
            self.popupLabel.setText("请求错误")
        elif flag == "C":
            self.popupLabel.close()
        elif flag == "T":
            homeWin = Home()
            self.close()
            homeWin.show()
            homeWin.exec_()




class Home(QtWidgets.QDialog, Ui_Home):  # 创建一个Qt对象
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_Home.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象
        self.closeButton.clicked.connect(self.close)
        self.minButton.clicked.connect(self.showMinimized)
        self.usernameButton.clicked.connect(self.combobox)
        self.downloadButton.clicked.connect(self.download)

    def combobox(self):
        if self.comboFrame.isVisible() == True:
            self.comboFrame.close()
        else:
            self.comboFrame.show()

    def download(self):
        self.threads = swiftThread(self)
        self.threads.trigger.connect(self.swiftDone)
        self.threads.start()

    def swiftDone(self, result):
        print(result)
