# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imgView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgView.sizePolicy().hasHeightForWidth())
        self.imgView.setSizePolicy(sizePolicy)
        self.imgView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imgView.setMouseTracking(True)
        self.imgView.setObjectName("imgView")
        self.horizontalLayout_4.addWidget(self.imgView)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.colorBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBox.sizePolicy().hasHeightForWidth())
        self.colorBox.setSizePolicy(sizePolicy)
        self.colorBox.setObjectName("colorBox")
        self.horizontalLayout.addWidget(self.colorBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.actionBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionBox.sizePolicy().hasHeightForWidth())
        self.actionBox.setSizePolicy(sizePolicy)
        self.actionBox.setObjectName("actionBox")
        self.horizontalLayout_2.addWidget(self.actionBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imgSizeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgSizeLabel.sizePolicy().hasHeightForWidth())
        self.imgSizeLabel.setSizePolicy(sizePolicy)
        self.imgSizeLabel.setMinimumSize(QtCore.QSize(77, 0))
        self.imgSizeLabel.setObjectName("imgSizeLabel")
        self.horizontalLayout_3.addWidget(self.imgSizeLabel)
        self.imgSizeSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgSizeSlider.sizePolicy().hasHeightForWidth())
        self.imgSizeSlider.setSizePolicy(sizePolicy)
        self.imgSizeSlider.setMinimumSize(QtCore.QSize(172, 0))
        self.imgSizeSlider.setMinimum(50)
        self.imgSizeSlider.setMaximum(200)
        self.imgSizeSlider.setSingleStep(1)
        self.imgSizeSlider.setPageStep(10)
        self.imgSizeSlider.setProperty("value", 100)
        self.imgSizeSlider.setTracking(True)
        self.imgSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imgSizeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.imgSizeSlider.setObjectName("imgSizeSlider")
        self.horizontalLayout_3.addWidget(self.imgSizeSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.patientInfo = QtWidgets.QTextEdit(self.centralwidget)
        self.patientInfo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patientInfo.sizePolicy().hasHeightForWidth())
        self.patientInfo.setSizePolicy(sizePolicy)
        self.patientInfo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.patientInfo.setObjectName("patientInfo")
        self.verticalLayout.addWidget(self.patientInfo)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pivotsInfo = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pivotsInfo.sizePolicy().hasHeightForWidth())
        self.pivotsInfo.setSizePolicy(sizePolicy)
        self.pivotsInfo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pivotsInfo.setObjectName("pivotsInfo")
        self.verticalLayout.addWidget(self.pivotsInfo)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Form)
        self.toolBar.setObjectName("toolBar")
        Form.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.loadImgBtn = QtWidgets.QAction(Form)
        self.loadImgBtn.setObjectName("loadImgBtn")
        self.deleteImgBtn = QtWidgets.QAction(Form)
        self.deleteImgBtn.setObjectName("deleteImgBtn")
        self.saveImgBtn = QtWidgets.QAction(Form)
        self.saveImgBtn.setObjectName("saveImgBtn")
        self.quitAppBtn = QtWidgets.QAction(Form)
        self.quitAppBtn.setObjectName("quitAppBtn")
        self.clearAllBtn = QtWidgets.QAction(Form)
        self.clearAllBtn.setObjectName("clearAllBtn")
        self.incSizeBtn = QtWidgets.QAction(Form)
        self.incSizeBtn.setObjectName("incSizeBtn")
        self.decSizeBtn = QtWidgets.QAction(Form)
        self.decSizeBtn.setObjectName("decSizeBtn")
        self.resetSizeBtn = QtWidgets.QAction(Form)
        self.resetSizeBtn.setObjectName("resetSizeBtn")
        self.autoAddPtsBtn = QtWidgets.QAction(Form)
        self.autoAddPtsBtn.setObjectName("autoAddPtsBtn")
        self.menu.addAction(self.loadImgBtn)
        self.menu.addAction(self.deleteImgBtn)
        self.menu.addAction(self.saveImgBtn)
        self.menu.addSeparator()
        self.menu.addAction(self.quitAppBtn)
        self.menu_2.addAction(self.incSizeBtn)
        self.menu_2.addAction(self.decSizeBtn)
        self.menu_2.addAction(self.resetSizeBtn)
        self.menu_2.addAction(self.clearAllBtn)
        self.menu_2.addAction(self.autoAddPtsBtn)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.incSizeBtn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.decSizeBtn)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.resetSizeBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Label Dcm"))
        self.label_3.setText(_translate("Form", "颜色"))
        self.label_4.setText(_translate("Form", "操作"))
        self.imgSizeLabel.setText(_translate("Form", "大小：100%"))
        self.label.setText(_translate("Form", "病人信息"))
        self.label_2.setText(_translate("Form", "关键点信息"))
        self.menu.setTitle(_translate("Form", "文件"))
        self.menu_2.setTitle(_translate("Form", "编辑"))
        self.toolBar.setWindowTitle(_translate("Form", "toolBar"))
        self.loadImgBtn.setText(_translate("Form", "新建"))
        self.loadImgBtn.setShortcut(_translate("Form", "Ctrl+N"))
        self.deleteImgBtn.setText(_translate("Form", "删除"))
        self.deleteImgBtn.setShortcut(_translate("Form", "Ctrl+Z"))
        self.saveImgBtn.setText(_translate("Form", "保存"))
        self.saveImgBtn.setShortcut(_translate("Form", "Ctrl+S"))
        self.quitAppBtn.setText(_translate("Form", "退出"))
        self.quitAppBtn.setShortcut(_translate("Form", "Ctrl+F4"))
        self.clearAllBtn.setText(_translate("Form", "清除全部"))
        self.incSizeBtn.setText(_translate("Form", "放大"))
        self.decSizeBtn.setText(_translate("Form", "缩小"))
        self.resetSizeBtn.setText(_translate("Form", "还原"))
        self.autoAddPtsBtn.setText(_translate("Form", "自动判断"))
