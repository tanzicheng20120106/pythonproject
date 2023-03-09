from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName(u"actiona")
        self.actiona_2 = QAction(MainWindow)
        self.actiona_2.setObjectName(u"actiona_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(000, 000, 4096, 2048))
        self.label.setPixmap(QPixmap(u"C:/Users/Lenovo/Desktop/\u4f5c\u54c1/data/th.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(1000, 1000))
        self.menu.setMaximumSize(QSize(1000, 1000))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actiona)
        self.menu.addAction(self.actiona_2)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e5d\u4e5d\u4e58\u6cd5\u8868", None))
        self.actiona.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actiona.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
        self.actiona_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8eQt", None))
        self.label.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
