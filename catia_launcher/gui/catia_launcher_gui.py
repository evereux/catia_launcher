# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catia_launcher_gui.ui',
# licensing of 'catia_launcher_gui.ui' applies.
#
# Created: Sun Mar 17 18:04:14 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 302)
        MainWindow.setMaximumSize(QtCore.QSize(430, 445))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.combo_select_catia = QtWidgets.QComboBox(self.centralwidget)
        self.combo_select_catia.setObjectName("combo_select_catia")
        self.combo_select_catia.addItem("")
        self.verticalLayout.addWidget(self.combo_select_catia)
        self.horizontalLayout_01 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_01.setObjectName("horizontalLayout_01")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_01.addItem(spacerItem1)
        self.btn_start_catia = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_catia.setObjectName("btn_start_catia")
        self.horizontalLayout_01.addWidget(self.btn_start_catia)
        self.verticalLayout.addLayout(self.horizontalLayout_01)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_02 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_02.setObjectName("horizontalLayout_02")
        self.checkbox_user_files = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_user_files.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkbox_user_files.setObjectName("checkbox_user_files")
        self.horizontalLayout_02.addWidget(self.checkbox_user_files)
        self.checkbox_temp_files = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_temp_files.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkbox_temp_files.setObjectName("checkbox_temp_files")
        self.horizontalLayout_02.addWidget(self.checkbox_temp_files)
        self.verticalLayout.addLayout(self.horizontalLayout_02)
        self.horizontalLayout_03 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_03.setObjectName("horizontalLayout_03")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_03.addItem(spacerItem3)
        self.btn_open_folders = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_folders.setObjectName("btn_open_folders")
        self.horizontalLayout_03.addWidget(self.btn_open_folders)
        self.verticalLayout.addLayout(self.horizontalLayout_03)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_04 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_04.setObjectName("horizontalLayout_04")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_04.addItem(spacerItem5)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setStyleSheet("")
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_04.addWidget(self.btn_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_04)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 243, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "CATIA V5 Launcher", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "CATIA V5 Launcher", None, -1))
        self.combo_select_catia.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Select Application", None, -1))
        self.btn_start_catia.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.btn_start_catia.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.checkbox_user_files.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Opens folder containing the user specific CATIA settings folder.<br/><br/>Deletion of all the files in this folder resets CATIA to it\'s default configuration.</p></body></html>", None, -1))
        self.checkbox_user_files.setText(QtWidgets.QApplication.translate("MainWindow", "Open User Files", None, -1))
        self.checkbox_temp_files.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Opens the users CATIA temporary files folder.", None, -1))
        self.checkbox_temp_files.setText(QtWidgets.QApplication.translate("MainWindow", "Open Temp Files", None, -1))
        self.btn_open_folders.setText(QtWidgets.QApplication.translate("MainWindow", "Open Folder(s)", None, -1))
        self.btn_exit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.menuHelp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))

