# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SNPConvert_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SNPConvert(object):
    def setupUi(self, SNPConvert):
        SNPConvert.setObjectName(_fromUtf8("SNPConvert"))
        SNPConvert.resize(1153, 620)
        self.centralwidget = QtGui.QWidget(SNPConvert)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_ROW = QtGui.QWidget()
        self.tab_ROW.setObjectName(_fromUtf8("tab_ROW"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_ROW)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1121, 511))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout_tab2 = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout_tab2.setMargin(10)
        self.gridLayout_tab2.setObjectName(_fromUtf8("gridLayout_tab2"))
        self.Output_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output_lbl_tab2.sizePolicy().hasHeightForWidth())
        self.Output_lbl_tab2.setSizePolicy(sizePolicy)
        self.Output_lbl_tab2.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Output_lbl_tab2.setFont(font)
        self.Output_lbl_tab2.setObjectName(_fromUtf8("Output_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.Output_lbl_tab2, 5, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.SnpMap_tab2 = QtGui.QPushButton(self.layoutWidget_2)
        self.SnpMap_tab2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SnpMap_tab2.setObjectName(_fromUtf8("SnpMap_tab2"))
        self.gridLayout_tab2.addWidget(self.SnpMap_tab2, 4, 1, 1, 2)
        self.Input_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input_lbl_tab2.sizePolicy().hasHeightForWidth())
        self.Input_lbl_tab2.setSizePolicy(sizePolicy)
        self.Input_lbl_tab2.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Input_lbl_tab2.setFont(font)
        self.Input_lbl_tab2.setObjectName(_fromUtf8("Input_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.Input_lbl_tab2, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.AlleleCod_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AlleleCod_lbl_tab2.sizePolicy().hasHeightForWidth())
        self.AlleleCod_lbl_tab2.setSizePolicy(sizePolicy)
        self.AlleleCod_lbl_tab2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.AlleleCod_lbl_tab2.setObjectName(_fromUtf8("AlleleCod_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.AlleleCod_lbl_tab2, 6, 0, 1, 1)
        self.FinRep_tab2 = QtGui.QPushButton(self.layoutWidget_2)
        self.FinRep_tab2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.FinRep_tab2.setObjectName(_fromUtf8("FinRep_tab2"))
        self.gridLayout_tab2.addWidget(self.FinRep_tab2, 3, 1, 1, 2)
        self.ConvertFile_tab2 = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvertFile_tab2.sizePolicy().hasHeightForWidth())
        self.ConvertFile_tab2.setSizePolicy(sizePolicy)
        self.ConvertFile_tab2.setMinimumSize(QtCore.QSize(110, 0))
        self.ConvertFile_tab2.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConvertFile_tab2.setFont(font)
        self.ConvertFile_tab2.setObjectName(_fromUtf8("ConvertFile_tab2"))
        self.gridLayout_tab2.addWidget(self.ConvertFile_tab2, 10, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_tab2.addItem(spacerItem, 9, 0, 1, 3)
        self.Title_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_lbl_tab2.sizePolicy().hasHeightForWidth())
        self.Title_lbl_tab2.setSizePolicy(sizePolicy)
        self.Title_lbl_tab2.setStyleSheet(_fromUtf8(""))
        self.Title_lbl_tab2.setObjectName(_fromUtf8("Title_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.Title_lbl_tab2, 0, 0, 1, 4)
        self.outname_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        self.outname_lbl_tab2.setObjectName(_fromUtf8("outname_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.outname_lbl_tab2, 8, 0, 1, 1)
        self.OutName_tab2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.OutName_tab2.setMaximumSize(QtCore.QSize(145, 16777215))
        self.OutName_tab2.setObjectName(_fromUtf8("OutName_tab2"))
        self.gridLayout_tab2.addWidget(self.OutName_tab2, 8, 1, 1, 2)
        self.BrdCode_tab2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.BrdCode_tab2.setMaximumSize(QtCore.QSize(145, 16777215))
        self.BrdCode_tab2.setObjectName(_fromUtf8("BrdCode_tab2"))
        self.gridLayout_tab2.addWidget(self.BrdCode_tab2, 7, 1, 1, 2)
        self.FinalReport_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        self.FinalReport_lbl_tab2.setAccessibleName(_fromUtf8(""))
        self.FinalReport_lbl_tab2.setObjectName(_fromUtf8("FinalReport_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.FinalReport_lbl_tab2, 3, 0, 1, 1)
        self.AlleleCod_box_tab2 = QtGui.QComboBox(self.layoutWidget_2)
        self.AlleleCod_box_tab2.setMaximumSize(QtCore.QSize(145, 16777215))
        self.AlleleCod_box_tab2.setObjectName(_fromUtf8("AlleleCod_box_tab2"))
        self.gridLayout_tab2.addWidget(self.AlleleCod_box_tab2, 6, 1, 1, 2)
        self.SnpMap_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        self.SnpMap_lbl_tab2.setObjectName(_fromUtf8("SnpMap_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.SnpMap_lbl_tab2, 4, 0, 1, 1)
        self.Log_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Log_lbl_tab2.sizePolicy().hasHeightForWidth())
        self.Log_lbl_tab2.setSizePolicy(sizePolicy)
        self.Log_lbl_tab2.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Log_lbl_tab2.setFont(font)
        self.Log_lbl_tab2.setObjectName(_fromUtf8("Log_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.Log_lbl_tab2, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.Log_wdg_tab2 = QtGui.QTextEdit(self.layoutWidget_2)
        self.Log_wdg_tab2.setObjectName(_fromUtf8("Log_wdg_tab2"))
        self.gridLayout_tab2.addWidget(self.Log_wdg_tab2, 3, 3, 8, 1)
        self.BrdCode_lbl_tab2 = QtGui.QLabel(self.layoutWidget_2)
        self.BrdCode_lbl_tab2.setObjectName(_fromUtf8("BrdCode_lbl_tab2"))
        self.gridLayout_tab2.addWidget(self.BrdCode_lbl_tab2, 7, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.layoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_tab2.addWidget(self.line_2, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab_ROW, _fromUtf8(""))
        self.tab_MATRIX = QtGui.QWidget()
        self.tab_MATRIX.setObjectName(_fromUtf8("tab_MATRIX"))
        self.layoutWidget = QtGui.QWidget(self.tab_MATRIX)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1121, 511))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_tab1 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_tab1.setMargin(10)
        self.gridLayout_tab1.setObjectName(_fromUtf8("gridLayout_tab1"))
        self.BrdCode_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        self.BrdCode_lbl_tab1.setObjectName(_fromUtf8("BrdCode_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.BrdCode_lbl_tab1, 6, 0, 1, 1)
        self.SnpMap_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        self.SnpMap_lbl_tab1.setObjectName(_fromUtf8("SnpMap_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.SnpMap_lbl_tab1, 4, 0, 1, 1)
        self.Log_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Log_lbl_tab1.sizePolicy().hasHeightForWidth())
        self.Log_lbl_tab1.setSizePolicy(sizePolicy)
        self.Log_lbl_tab1.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Log_lbl_tab1.setFont(font)
        self.Log_lbl_tab1.setObjectName(_fromUtf8("Log_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.Log_lbl_tab1, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.BrdCode_tab1 = QtGui.QLineEdit(self.layoutWidget)
        self.BrdCode_tab1.setMaximumSize(QtCore.QSize(145, 16777215))
        self.BrdCode_tab1.setObjectName(_fromUtf8("BrdCode_tab1"))
        self.gridLayout_tab1.addWidget(self.BrdCode_tab1, 6, 1, 1, 2)
        self.Output_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Output_lbl_tab1.setFont(font)
        self.Output_lbl_tab1.setObjectName(_fromUtf8("Output_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.Output_lbl_tab1, 5, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.Title_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title_lbl_tab1.sizePolicy().hasHeightForWidth())
        self.Title_lbl_tab1.setSizePolicy(sizePolicy)
        self.Title_lbl_tab1.setStyleSheet(_fromUtf8(""))
        self.Title_lbl_tab1.setObjectName(_fromUtf8("Title_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.Title_lbl_tab1, 0, 0, 1, 4)
        self.ConvertFile_tab1 = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConvertFile_tab1.sizePolicy().hasHeightForWidth())
        self.ConvertFile_tab1.setSizePolicy(sizePolicy)
        self.ConvertFile_tab1.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConvertFile_tab1.setFont(font)
        self.ConvertFile_tab1.setObjectName(_fromUtf8("ConvertFile_tab1"))
        self.gridLayout_tab1.addWidget(self.ConvertFile_tab1, 10, 0, 1, 3)
        self.OutName_tab1 = QtGui.QLineEdit(self.layoutWidget)
        self.OutName_tab1.setMaximumSize(QtCore.QSize(145, 16777215))
        self.OutName_tab1.setObjectName(_fromUtf8("OutName_tab1"))
        self.gridLayout_tab1.addWidget(self.OutName_tab1, 7, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_tab1.addItem(spacerItem1, 9, 0, 1, 3)
        self.SnpMap_tab1 = QtGui.QPushButton(self.layoutWidget)
        self.SnpMap_tab1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SnpMap_tab1.setObjectName(_fromUtf8("SnpMap_tab1"))
        self.gridLayout_tab1.addWidget(self.SnpMap_tab1, 4, 1, 1, 2)
        self.FinalReport_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        self.FinalReport_lbl_tab1.setAccessibleName(_fromUtf8(""))
        self.FinalReport_lbl_tab1.setObjectName(_fromUtf8("FinalReport_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.FinalReport_lbl_tab1, 3, 0, 1, 1)
        self.FinRep_tab1 = QtGui.QPushButton(self.layoutWidget)
        self.FinRep_tab1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.FinRep_tab1.setObjectName(_fromUtf8("FinRep_tab1"))
        self.gridLayout_tab1.addWidget(self.FinRep_tab1, 3, 1, 1, 2)
        self.Input_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Input_lbl_tab1.setFont(font)
        self.Input_lbl_tab1.setTextFormat(QtCore.Qt.AutoText)
        self.Input_lbl_tab1.setScaledContents(True)
        self.Input_lbl_tab1.setObjectName(_fromUtf8("Input_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.Input_lbl_tab1, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.outname_lbl_tab1 = QtGui.QLabel(self.layoutWidget)
        self.outname_lbl_tab1.setObjectName(_fromUtf8("outname_lbl_tab1"))
        self.gridLayout_tab1.addWidget(self.outname_lbl_tab1, 7, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_tab1.addWidget(self.line_3, 1, 0, 1, 4)
        self.Log_wdg_tab1 = QtGui.QTextEdit(self.layoutWidget)
        self.Log_wdg_tab1.setObjectName(_fromUtf8("Log_wdg_tab1"))
        self.gridLayout_tab1.addWidget(self.Log_wdg_tab1, 3, 3, 8, 1)
        self.widget = QtGui.QWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widget.setBaseSize(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_tab1.addWidget(self.widget, 8, 0, 1, 3)
        self.FinRep_tab1.raise_()
        self.SnpMap_lbl_tab1.raise_()
        self.SnpMap_tab1.raise_()
        self.FinalReport_lbl_tab1.raise_()
        self.ConvertFile_tab1.raise_()
        self.BrdCode_lbl_tab1.raise_()
        self.outname_lbl_tab1.raise_()
        self.OutName_tab1.raise_()
        self.BrdCode_tab1.raise_()
        self.Log_wdg_tab1.raise_()
        self.Input_lbl_tab1.raise_()
        self.Output_lbl_tab1.raise_()
        self.Log_lbl_tab1.raise_()
        self.Title_lbl_tab1.raise_()
        self.line_3.raise_()
        self.widget.raise_()
        self.tabWidget.addTab(self.tab_MATRIX, _fromUtf8(""))
        self.tab_iConvert = QtGui.QWidget()
        self.tab_iConvert.setObjectName(_fromUtf8("tab_iConvert"))
        self.layoutWidget_3 = QtGui.QWidget(self.tab_iConvert)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1121, 511))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_tab3 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_tab3.setMargin(10)
        self.gridLayout_tab3.setObjectName(_fromUtf8("gridLayout_tab3"))
        self.SnpChimp_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.SnpChimp_lbl_tab3.setObjectName(_fromUtf8("SnpChimp_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.SnpChimp_lbl_tab3, 5, 0, 1, 1)
        self.AlleleCodIn_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.AlleleCodIn_lbl_tab3.setObjectName(_fromUtf8("AlleleCodIn_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.AlleleCodIn_lbl_tab3, 6, 0, 1, 1)
        self.outname_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.outname_lbl_tab3.setObjectName(_fromUtf8("outname_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.outname_lbl_tab3, 10, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.YesRadioButton_tab3 = QtGui.QRadioButton(self.layoutWidget_3)
        self.YesRadioButton_tab3.setChecked(True)
        self.YesRadioButton_tab3.setObjectName(_fromUtf8("YesRadioButton_tab3"))
        self.horizontalLayout.addWidget(self.YesRadioButton_tab3)
        self.NoRadioButton_tab3 = QtGui.QRadioButton(self.layoutWidget_3)
        self.NoRadioButton_tab3.setObjectName(_fromUtf8("NoRadioButton_tab3"))
        self.horizontalLayout.addWidget(self.NoRadioButton_tab3)
        self.gridLayout_tab3.addLayout(self.horizontalLayout, 7, 1, 1, 2)
        self.Output_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Output_lbl_tab3.setFont(font)
        self.Output_lbl_tab3.setObjectName(_fromUtf8("Output_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.Output_lbl_tab3, 8, 0, 1, 3, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_tab3.addItem(spacerItem2, 11, 0, 1, 3)
        self.Title_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.Title_lbl_tab3.setStyleSheet(_fromUtf8(""))
        self.Title_lbl_tab3.setObjectName(_fromUtf8("Title_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.Title_lbl_tab3, 0, 0, 1, 4)
        self.PedFile_tab3 = QtGui.QPushButton(self.layoutWidget_3)
        self.PedFile_tab3.setObjectName(_fromUtf8("PedFile_tab3"))
        self.gridLayout_tab3.addWidget(self.PedFile_tab3, 3, 1, 1, 2)
        self.OutName_tab3 = QtGui.QLineEdit(self.layoutWidget_3)
        self.OutName_tab3.setObjectName(_fromUtf8("OutName_tab3"))
        self.gridLayout_tab3.addWidget(self.OutName_tab3, 10, 1, 1, 2)
        self.MapFile_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.MapFile_lbl_tab3.setObjectName(_fromUtf8("MapFile_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.MapFile_lbl_tab3, 4, 0, 1, 1)
        self.PedFile_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.PedFile_lbl_tab3.setAccessibleName(_fromUtf8(""))
        self.PedFile_lbl_tab3.setObjectName(_fromUtf8("PedFile_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.PedFile_lbl_tab3, 3, 0, 1, 1)
        self.AlleleCodIn_box_tab3 = QtGui.QComboBox(self.layoutWidget_3)
        self.AlleleCodIn_box_tab3.setObjectName(_fromUtf8("AlleleCodIn_box_tab3"))
        self.gridLayout_tab3.addWidget(self.AlleleCodIn_box_tab3, 6, 1, 1, 2)
        self.SnpChimp_tab3 = QtGui.QPushButton(self.layoutWidget_3)
        self.SnpChimp_tab3.setObjectName(_fromUtf8("SnpChimp_tab3"))
        self.gridLayout_tab3.addWidget(self.SnpChimp_tab3, 5, 1, 1, 2)
        self.Log_wdg_tab3 = QtGui.QTextEdit(self.layoutWidget_3)
        self.Log_wdg_tab3.setStyleSheet(_fromUtf8(""))
        self.Log_wdg_tab3.setObjectName(_fromUtf8("Log_wdg_tab3"))
        self.gridLayout_tab3.addWidget(self.Log_wdg_tab3, 3, 3, 10, 1)
        self.AlleleCodOut_box_tab3 = QtGui.QComboBox(self.layoutWidget_3)
        self.AlleleCodOut_box_tab3.setObjectName(_fromUtf8("AlleleCodOut_box_tab3"))
        self.gridLayout_tab3.addWidget(self.AlleleCodOut_box_tab3, 9, 1, 1, 2)
        self.Input_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Input_lbl_tab3.setFont(font)
        self.Input_lbl_tab3.setObjectName(_fromUtf8("Input_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.Input_lbl_tab3, 2, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.Log_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Log_lbl_tab3.setFont(font)
        self.Log_lbl_tab3.setObjectName(_fromUtf8("Log_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.Log_lbl_tab3, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.UpdateMap_lbl = QtGui.QLabel(self.layoutWidget_3)
        self.UpdateMap_lbl.setObjectName(_fromUtf8("UpdateMap_lbl"))
        self.gridLayout_tab3.addWidget(self.UpdateMap_lbl, 7, 0, 1, 1)
        self.AlleleCodOut_lbl_tab3 = QtGui.QLabel(self.layoutWidget_3)
        self.AlleleCodOut_lbl_tab3.setObjectName(_fromUtf8("AlleleCodOut_lbl_tab3"))
        self.gridLayout_tab3.addWidget(self.AlleleCodOut_lbl_tab3, 9, 0, 1, 1)
        self.ConvertFile_tab3 = QtGui.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ConvertFile_tab3.setFont(font)
        self.ConvertFile_tab3.setObjectName(_fromUtf8("ConvertFile_tab3"))
        self.gridLayout_tab3.addWidget(self.ConvertFile_tab3, 12, 0, 1, 3)
        self.MapFile_tab3 = QtGui.QPushButton(self.layoutWidget_3)
        self.MapFile_tab3.setObjectName(_fromUtf8("MapFile_tab3"))
        self.gridLayout_tab3.addWidget(self.MapFile_tab3, 4, 1, 1, 2)
        self.line = QtGui.QFrame(self.layoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_tab3.addWidget(self.line, 1, 0, 1, 4)
        self.tabWidget.addTab(self.tab_iConvert, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        SNPConvert.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SNPConvert)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SNPConvert.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SNPConvert)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SNPConvert.setStatusBar(self.statusbar)

        self.retranslateUi(SNPConvert)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SNPConvert)

    def retranslateUi(self, SNPConvert):
        SNPConvert.setWindowTitle(_translate("SNPConvert", "SNPConvert v1.0", None))
        self.Output_lbl_tab2.setText(_translate("SNPConvert", "Select output formats and filename", None))
        self.SnpMap_tab2.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select an Illumina <span style=\" font-weight:600;\">SnpMap</span> file.</p><p>Example:</p>\n"
"<p><span style=\" font-style:italic;\">Index Name Chromosome Position GenTrain Score SNP ILMN Strand Customer Strand NormID</span>\n"
"<br><span style=\" font-style:italic;\">1 snp1 1 10 0.9151 [A/C] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">2 snp2 1 100 0.8887 [A/G] TOP BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">3 snp3 1 335 0.8174 [A/G] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">4 snp4 1 467 0.8232 [A/G] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">5 snp5 1 652 0.7927 [T/C] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">6 snp6 2 12 0.7399 [T/C] BOT BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">7 snp7 2 259 0.7650 [T/G] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">8 snp8 2 366 0.9243 [T/C] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">9 snp9 2 411 0.8912 [T/C] BOT BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">10 snp10 2 545 0.9241 [T/C] BOT BOT 0</span></p></body></html>", None))
        self.SnpMap_tab2.setText(_translate("SNPConvert", "Select SnpMap", None))
        self.Input_lbl_tab2.setText(_translate("SNPConvert", "Select input files and formats", None))
        self.AlleleCod_lbl_tab2.setText(_translate("SNPConvert", "Output allele code", None))
        self.FinRep_tab2.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select an Illumina FinalReport file in <span style=\" font-weight:600;\">ROW </span>format.</p><p>Example: </p>\n"
"<p><span style=\" font-style:italic;\">[Header]</span>\n"
"<br><span style=\" font-style:italic;\">GSGT Version 1.1.1</span>\n"
"<br><span style=\" font-style:italic;\">Processing Date 1/1/1000 0:00 PM</span>\n"
"<br><span style=\" font-style:italic;\">Content testfile.bpm</span>\n"
"<br><span style=\" font-style:italic;\">Num SNPs 10</span>\n"
"<br><span style=\" font-style:italic;\">Total SNPs 10</span>\n"
"<br><span style=\" font-style:italic;\">Num Samples 2</span>\n"
"<br><span style=\" font-style:italic;\">Total Samples 2</span>\n"
"<br><span style=\" font-style:italic;\">[Data]</span>\n"
"<br><span style=\" font-style:italic;\">SNP Name Sample ID Allele1 - Top Allele2 - Top GC Score</span>\n"
"<br><span style=\" font-style:italic;\">snp1 ANIM_38 A C 0.8143</span>\n"
"<br><span style=\" font-style:italic;\">snp2 ANIM_38 A G 0.5647</span>\n"
"<br><span style=\" font-style:italic;\">snp3 ANIM_38 A A 0.5620</span>\n"
"<br><span style=\" font-style:italic;\">snp4 ANIM_38 A A 0.4777</span>\n"
"<br><span style=\" font-style:italic;\">snp5 ANIM_38 G G 0.7372</span>\n"
"<br><span style=\" font-style:italic;\">snp6 ANIM_38 A A 0.5613</span>\n"
"<br><span style=\" font-style:italic;\">snp7 ANIM_38 A C 0.6411</span>\n"
"<br><span style=\" font-style:italic;\">snp8 ANIM_38 A A 0.4614</span>\n"
"<br><span style=\" font-style:italic;\">snp9 ANIM_38 A G 0.6916</span>\n"
"<br><span style=\" font-style:italic;\">snp10 ANIM_38 A G 0.7925</span>\n"
"<br><span style=\" font-style:italic;\">snp1 ANIM_39 C C 0.8143</span>\n"
"<br><span style=\" font-style:italic;\">snp2 ANIM_39 A G 0.5647</span>\n"
"<br><span style=\" font-style:italic;\">snp3 ANIM_39 A A 0.5620</span>\n"
"<br><span style=\" font-style:italic;\">snp4 ANIM_39 A A 0.4777</span>\n"
"<br><span style=\" font-style:italic;\">snp5 ANIM_39 A G 0.7372</span>\n"
"<br><span style=\" font-style:italic;\">snp6 ANIM_39 A A 0.5613</span>\n"
"<br><span style=\" font-style:italic;\">snp7 ANIM_39 A C 0.6411</span>\n"
"<br><span style=\" font-style:italic;\">snp8 ANIM_39 A A 0.4614</span>\n"
"<br><span style=\" font-style:italic;\">snp9 ANIM_39 A G 0.6916</span>\n"
"<br><span style=\" font-style:italic;\">snp10 ANIM_39 A A 0.7925</span></p></body></html>", None))
        self.FinRep_tab2.setText(_translate("SNPConvert", "Select Final Report", None))
        self.ConvertFile_tab2.setText(_translate("SNPConvert", "Convert to PLINK", None))
        self.Title_lbl_tab2.setText(_translate("SNPConvert", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Pedda </span><span style=\" font-size:22pt; font-weight:600; font-style:italic; color:#0000ff;\">ROW</span><span style=\" font-size:22pt; font-weight:600;\"> software</span></p><p align=\"center\"><br/><span style=\" font-size:14pt; font-weight:600;\">Illumina ROW format files to PLINK (ped/map) converter</span></p></body></html>", None))
        self.outname_lbl_tab2.setText(_translate("SNPConvert", "Output name", None))
        self.OutName_tab2.setToolTip(_translate("SNPConvert", "<html><head/><body><p>PLINK output name (optional).</p><p>Example: <span style=\" font-style:italic;\">If user inputs &quot;PEDDA&quot; in this field, then he will obtain a PEDDA.ped and PEDDA.map file if conversion is successfu</span>l.</p></body></html>", None))
        self.BrdCode_tab2.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Population ID will be used as first column in the .ped file (optional)</p></body></html>", None))
        self.FinalReport_lbl_tab2.setText(_translate("SNPConvert", "Final Report file", None))
        self.SnpMap_lbl_tab2.setText(_translate("SNPConvert", "Illumina SnpMap", None))
        self.Log_lbl_tab2.setText(_translate("SNPConvert", "Runtime log", None))
        self.BrdCode_lbl_tab2.setText(_translate("SNPConvert", "Population ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ROW), _translate("SNPConvert", "Illumina ROW format", None))
        self.BrdCode_lbl_tab1.setText(_translate("SNPConvert", "Population ID", None))
        self.SnpMap_lbl_tab1.setText(_translate("SNPConvert", "Illumina SnpMap", None))
        self.Log_lbl_tab1.setText(_translate("SNPConvert", "Runtime log", None))
        self.BrdCode_tab1.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Population ID will be used as first column in the .ped file (optional)</p></body></html>", None))
        self.Output_lbl_tab1.setText(_translate("SNPConvert", "Select output formats and filename", None))
        self.Title_lbl_tab1.setText(_translate("SNPConvert", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Pedda </span><span style=\" font-size:22pt; font-weight:600; font-style:italic; color:#ff0000;\">MATRIX</span><span style=\" font-size:22pt; font-weight:600;\"> software</span></p><p align=\"center\"><br/><span style=\" font-size:14pt; font-weight:600;\">Illumina MATRIX format files to PLINK (ped/map) converter</span></p></body></html>", None))
        self.ConvertFile_tab1.setText(_translate("SNPConvert", "Convert to PLINK", None))
        self.OutName_tab1.setToolTip(_translate("SNPConvert", "<html><head/><body><p>PLINK output name (optional).</p><p>Example: <span style=\" font-style:italic;\">If user inputs &quot;PEDDA&quot; in this field, then he will obtain a PEDDA.ped and PEDDA.map file if conversion is successfu</span>l.</p></body></html>", None))
        self.SnpMap_tab1.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select an Illumina <span style=\" font-weight:600;\">SnpMap</span> file.</p><p>Example:</p>\n"
"<p><span style=\" font-style:italic;\">Index Name Chromosome Position GenTrain Score SNP ILMN Strand Customer Strand NormID</span>\n"
"<br><span style=\" font-style:italic;\">1 snp1 1 10 0.9151 [A/C] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">2 snp2 1 100 0.8887 [A/G] TOP BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">3 snp3 1 335 0.8174 [A/G] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">4 snp4 1 467 0.8232 [A/G] TOP TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">5 snp5 1 652 0.7927 [T/C] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">6 snp6 2 12 0.7399 [T/C] BOT BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">7 snp7 2 259 0.7650 [T/G] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">8 snp8 2 366 0.9243 [T/C] BOT TOP 0</span>\n"
"<br><span style=\" font-style:italic;\">9 snp9 2 411 0.8912 [T/C] BOT BOT 0</span>\n"
"<br><span style=\" font-style:italic;\">10 snp10 2 545 0.9241 [T/C] BOT BOT 0</span></p></body></html>", None))
        self.SnpMap_tab1.setText(_translate("SNPConvert", "Select SnpMap", None))
        self.FinalReport_lbl_tab1.setText(_translate("SNPConvert", "Final Report file", None))
        self.FinRep_tab1.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select an Illumina FinalReport file in <span style=\" font-weight:600;\">MATRIX </span>format.</p>\n"
"<p>Example:</p>\n"
"<p><span style=\" font-style:italic;\">[Header]</span>\n"
"<br><span style=\" font-style:italic;\">GSGT Version 1.1.1</span>\n"
"<br><span style=\" font-style:italic;\">Processing Date,1/1/1000 0:00 PM</span>\n"
"<br><span style=\" font-style:italic;\">Content testfile.bpm</span>\n"
"<br><span style=\" font-style:italic;\">Num SNPs,10</span>\n"
"<br><span style=\" font-style:italic;\">Total SNPs,10</span>\n"
"<br><span style=\" font-style:italic;\">Num Samples,2</span>\n"
"<br><span style=\" font-style:italic;\">Total Samples,2</span>\n"
"<br><span style=\" font-style:italic;\">[Data]</span>\n"
"<br><span style=\" font-style:italic;\">,ANIM_38,ANIM_39</span>\n"
"<br><span style=\" font-style:italic;\">snp1,AB,BB</span>\n"
"<br><span style=\" font-style:italic;\">snp2,AB,AB</span>\n"
"<br><span style=\" font-style:italic;\">snp3,AA,AA</span>\n"
"<br><span style=\" font-style:italic;\">snp4,AA,AA</span>\n"
"<br><span style=\" font-style:italic;\">snp5,BB,AB</span>\n"
"<br><span style=\" font-style:italic;\">snp6,AA,AA</span>\n"
"<br><span style=\" font-style:italic;\">snp7,AB,AA</span>\n"
"<br><span style=\" font-style:italic;\">snp8,AA,--</span>\n"
"<br><span style=\" font-style:italic;\">snp9,--,AB</span>\n"
"<br><span style=\" font-style:italic;\">snp10,AB,BB</span></p></body></html>", None))
        self.FinRep_tab1.setText(_translate("SNPConvert", "Select Final Report", None))
        self.Input_lbl_tab1.setText(_translate("SNPConvert", "Select input files and formats", None))
        self.outname_lbl_tab1.setText(_translate("SNPConvert", "Output name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_MATRIX), _translate("SNPConvert", "Illumina MATRIX format", None))
        self.SnpChimp_lbl_tab3.setText(_translate("SNPConvert", "SNPchimp file", None))
        self.AlleleCodIn_lbl_tab3.setText(_translate("SNPConvert", "Input allele coding", None))
        self.outname_lbl_tab3.setText(_translate("SNPConvert", "Output name", None))
        self.YesRadioButton_tab3.setText(_translate("SNPConvert", "Yes", None))
        self.NoRadioButton_tab3.setText(_translate("SNPConvert", "No", None))
        self.Output_lbl_tab3.setText(_translate("SNPConvert", "Select output formats and filename", None))
        self.Title_lbl_tab3.setText(_translate("SNPConvert", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#138f46;\">iConvert</span><span style=\" font-size:22pt; font-weight:600; color:#000000;\"> software</span></p><p align=\"center\"><span style=\" color:#000000;\"><br/></span><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Allele format and map converter for PLINK (ped/map) files</span></p></body></html>", None))
        self.PedFile_tab3.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select a valid .ped file (according to PLINK software specifics)</p></body></html>", None))
        self.PedFile_tab3.setText(_translate("SNPConvert", "Select PED file", None))
        self.MapFile_lbl_tab3.setText(_translate("SNPConvert", "PLINK format MAP file", None))
        self.PedFile_lbl_tab3.setText(_translate("SNPConvert", "PLINK format PED file", None))
        self.SnpChimp_tab3.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select a valid SNPchimp file - NOTE: the file <span style=\" font-style:italic;\">must</span> contain desired allele conversions! (e.g. select the appropriate options in the &quot;<span style=\" font-weight:600;\">Allele coding</span>&quot; section)</p><p><br/></p></body></html>", None))
        self.SnpChimp_tab3.setText(_translate("SNPConvert", "Select SNPchimp", None))
        self.Input_lbl_tab3.setText(_translate("SNPConvert", "Select input files and formats", None))
        self.Log_lbl_tab3.setText(_translate("SNPConvert", "Runtime log", None))
        self.UpdateMap_lbl.setText(_translate("SNPConvert", "Update map info", None))
        self.AlleleCodOut_lbl_tab3.setText(_translate("SNPConvert", "Output allele coding", None))
        self.ConvertFile_tab3.setText(_translate("SNPConvert", "Run iConvert", None))
        self.MapFile_tab3.setToolTip(_translate("SNPConvert", "<html><head/><body><p>Please select a valid .map file (according to PLINK software specifics)</p></body></html>", None))
        self.MapFile_tab3.setText(_translate("SNPConvert", "Select MAP file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_iConvert), _translate("SNPConvert", "iConvert software", None))

