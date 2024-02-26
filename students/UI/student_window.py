# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledmNbrIv.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys,os
sys.path.append('\\'.join(os.getcwd().split('\\')[:-1]))
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from resource import student_resource_rc

class Ui_student_window(object):
    def setupUi(self, student_window):
        if student_window.objectName():
            student_window.setObjectName(u"student_window")
        student_window.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/.svg/student_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        student_window.setWindowIcon(icon)
        self.new_file = QAction(student_window)
        self.new_file.setObjectName(u"new_file")
        self.open_file = QAction(student_window)
        self.open_file.setObjectName(u"open_file")
        self.save_file = QAction(student_window)
        self.save_file.setObjectName(u"save_file")
        self.rsave_file = QAction(student_window)
        self.rsave_file.setObjectName(u"rsave_file")
        self.time_file = QAction(student_window)
        self.time_file.setObjectName(u"time_file")
        self.actionbb_2 = QAction(student_window)
        self.actionbb_2.setObjectName(u"actionbb_2")
        self.actionbb_3 = QAction(student_window)
        self.actionbb_3.setObjectName(u"actionbb_3")
        self.edit_www = QAction(student_window)
        self.edit_www.setObjectName(u"edit_www")
        self.actionaa = QAction(student_window)
        self.actionaa.setObjectName(u"actionaa")
        self.setup = QAction(student_window)
        self.setup.setObjectName(u"setup")
        self.file_only_read_set = QAction(student_window)
        self.file_only_read_set.setObjectName(u"file_only_read_set")
        self.actionaa_2 = QAction(student_window)
        self.actionaa_2.setObjectName(u"actionaa_2")
        self.actionss = QAction(student_window)
        self.actionss.setObjectName(u"actionss")
        self.actionss_2 = QAction(student_window)
        self.actionss_2.setObjectName(u"actionss_2")
        self.save = QAction(student_window)
        self.save.setObjectName(u"save")
        self.exit_pro = QAction(student_window)
        self.exit_pro.setObjectName(u"exit_pro")
        self.centralwidget = QWidget(student_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.studets_table = QTableWidget(self.centralwidget)
        self.studets_table.setObjectName(u"studets_table")

        self.gridLayout.addWidget(self.studets_table, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.find_button = QPushButton(self.centralwidget)
        self.find_button.setObjectName(u"find_button")

        self.horizontalLayout.addWidget(self.find_button)

        self.find_edit = QLineEdit(self.centralwidget)
        self.find_edit.setObjectName(u"find_edit")

        self.horizontalLayout.addWidget(self.find_edit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        student_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(student_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        student_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(student_window)
        self.statusbar.setObjectName(u"statusbar")
        student_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.new_file)
        self.menu.addAction(self.open_file)
        self.menu.addAction(self.save_file)
        self.menu.addAction(self.rsave_file)
        self.menu.addAction(self.time_file)
        self.menu.addAction(self.actionbb_2)
        self.menu.addAction(self.actionbb_3)
        self.menu.addSeparator()
        self.menu.addAction(self.edit_www)
        self.menu.addAction(self.actionaa)
        self.menu.addSeparator()
        self.menu.addAction(self.setup)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionaa_2)
        self.menu.addAction(self.actionss)
        self.menu.addAction(self.actionss_2)
        self.menu.addSeparator()
        self.menu.addAction(self.save)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_pro)
        self.menu_2.addAction(self.file_only_read_set)

        self.retranslateUi(student_window)

        QMetaObject.connectSlotsByName(student_window)
    # setupUi

    def retranslateUi(self, student_window):
        student_window.setWindowTitle(QCoreApplication.translate("student_window", u"\u5b66\u751f\u4fe1\u606f\u7ba1\u7406\u7cfb\u7edf", None))
        self.new_file.setText(QCoreApplication.translate("student_window", u"\u65b0\u5efa", None))
#if QT_CONFIG(shortcut)
        self.new_file.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.open_file.setText(QCoreApplication.translate("student_window", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.open_file.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.save_file.setText(QCoreApplication.translate("student_window", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.save_file.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.rsave_file.setText(QCoreApplication.translate("student_window", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(shortcut)
        self.rsave_file.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.time_file.setText(QCoreApplication.translate("student_window", u"\u6700\u8fd1\u7684\u6587\u4ef6", None))
        self.actionbb_2.setText(QCoreApplication.translate("student_window", u"bb", None))
        self.actionbb_3.setText(QCoreApplication.translate("student_window", u"bb", None))
        self.edit_www.setText(QCoreApplication.translate("student_window", u"\u8fdc\u7a0b\u7f16\u8f91", None))
        self.actionaa.setText(QCoreApplication.translate("student_window", u"aa", None))
        self.setup.setText(QCoreApplication.translate("student_window", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(shortcut)
        self.setup.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.file_only_read_set.setText(QCoreApplication.translate("student_window", u"\u8bbe\u7f6e\u6587\u4ef6\u53ea\u8bfb", None))
        self.actionaa_2.setText(QCoreApplication.translate("student_window", u"aa", None))
        self.actionss.setText(QCoreApplication.translate("student_window", u"ss", None))
        self.actionss_2.setText(QCoreApplication.translate("student_window", u"ss", None))
        self.save.setText(QCoreApplication.translate("student_window", u"\u8282\u7535\u6a21\u5f0f", None))
#if QT_CONFIG(shortcut)
        self.save.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+.", None))
#endif // QT_CONFIG(shortcut)
        self.exit_pro.setText(QCoreApplication.translate("student_window", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.exit_pro.setShortcut(QCoreApplication.translate("student_window", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.find_button.setText(QCoreApplication.translate("student_window", u"\u641c\u7d22", None))
        self.menu.setTitle(QCoreApplication.translate("student_window", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("student_window", u"\u6587\u4ef6\u8bbe\u7f6e", None))
    # retranslateUi

