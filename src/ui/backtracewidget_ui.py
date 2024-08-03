# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lingmo/project/nx_pkg/LingmoOS/shell/frameworks/drkonqi/src/ui/backtracewidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 476)
        Form.setWindowTitle("GetBacktraceWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.m_statusWidget = StatusWidget(Form)
        self.m_statusWidget.setObjectName("m_statusWidget")
        self.verticalLayout.addWidget(self.m_statusWidget)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.m_backtraceStack = QtWidgets.QStackedWidget(Form)
        self.m_backtraceStack.setObjectName("m_backtraceStack")
        self.backtracePage = QtWidgets.QWidget()
        self.backtracePage.setObjectName("backtracePage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.backtracePage)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.m_backtraceEdit = QtWidgets.QTextBrowser(self.backtracePage)
        self.m_backtraceEdit.setObjectName("m_backtraceEdit")
        self.horizontalLayout.addWidget(self.m_backtraceEdit)
        self.m_backtraceStack.addWidget(self.backtracePage)
        self.backtraceHelpPage = QtWidgets.QWidget()
        self.backtraceHelpPage.setObjectName("backtraceHelpPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.backtraceHelpPage)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.m_backtraceHelpIcon = QtWidgets.QLabel(self.backtraceHelpPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_backtraceHelpIcon.sizePolicy().hasHeightForWidth())
        self.m_backtraceHelpIcon.setSizePolicy(sizePolicy)
        self.m_backtraceHelpIcon.setMaximumSize(QtCore.QSize(48, 48))
        self.m_backtraceHelpIcon.setScaledContents(True)
        self.m_backtraceHelpIcon.setObjectName("m_backtraceHelpIcon")
        self.horizontalLayout_3.addWidget(self.m_backtraceHelpIcon)
        self.m_backtraceHelpLabel = QtWidgets.QLabel(self.backtraceHelpPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_backtraceHelpLabel.sizePolicy().hasHeightForWidth())
        self.m_backtraceHelpLabel.setSizePolicy(sizePolicy)
        self.m_backtraceHelpLabel.setWordWrap(True)
        self.m_backtraceHelpLabel.setObjectName("m_backtraceHelpLabel")
        self.horizontalLayout_3.addWidget(self.m_backtraceHelpLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.m_backtraceStack.addWidget(self.backtraceHelpPage)
        self.mainLayout.addWidget(self.m_backtraceStack)
        self.m_toggleBacktraceCheckBox = QtWidgets.QCheckBox(Form)
        self.m_toggleBacktraceCheckBox.setObjectName("m_toggleBacktraceCheckBox")
        self.mainLayout.addWidget(self.m_toggleBacktraceCheckBox)
        self.verticalLayout.addLayout(self.mainLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.m_reloadBacktraceButton = QtWidgets.QPushButton(Form)
        self.m_reloadBacktraceButton.setProperty("isDragEnabled", False)
        self.m_reloadBacktraceButton.setObjectName("m_reloadBacktraceButton")
        self.horizontalLayout_2.addWidget(self.m_reloadBacktraceButton)
        self.m_installDebugButton = QtWidgets.QPushButton(Form)
        self.m_installDebugButton.setObjectName("m_installDebugButton")
        self.horizontalLayout_2.addWidget(self.m_installDebugButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.m_copyButton = QtWidgets.QPushButton(Form)
        self.m_copyButton.setObjectName("m_copyButton")
        self.horizontalLayout_2.addWidget(self.m_copyButton)
        self.m_saveButton = QtWidgets.QPushButton(Form)
        self.m_saveButton.setObjectName("m_saveButton")
        self.horizontalLayout_2.addWidget(self.m_saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.m_extraDetailsLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_extraDetailsLabel.sizePolicy().hasHeightForWidth())
        self.m_extraDetailsLabel.setSizePolicy(sizePolicy)
        self.m_extraDetailsLabel.setTextFormat(QtCore.Qt.RichText)
        self.m_extraDetailsLabel.setWordWrap(True)
        self.m_extraDetailsLabel.setOpenExternalLinks(False)
        self.m_extraDetailsLabel.setObjectName("m_extraDetailsLabel")
        self.verticalLayout_2.addWidget(self.m_extraDetailsLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.m_backtraceStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.m_toggleBacktraceCheckBox.setText(_translate("Form", "Show backtrace content (advanced)"))
from statuswidget import StatusWidget
