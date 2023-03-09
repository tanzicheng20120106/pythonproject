from PyQt5.QtWidgets import *
import sys
import os
import functools
import configparser
from ui import (gui,datedata,setup,nine)
class window(gui.Ui_MainWindow):
    def __init__(self):
        self.window=QMainWindow()
        self.window.show()
        self.flag=True   #控制‘.’行为
        self.flag2=True   #控制运算结果行为
        self.listdate=['+','-','*','/']
        self.datedata=[]
        self.setupUi(self.window)
        super().__init__()
    def data(self,num):
        if (num in ['*','/']) and (self.lineEdit.text()==''):
            return
        if (not self.flag) and num=='.':
            return
        if num in self.listdate:
            self.flag=True
        if (not self.flag2) and (num not in self.listdate) or (self.lineEdit.text()=='输入错误'):
            self.lineEdit.clear()
            self.flag2=True
        else:
            self.flag2=True
        if (not self.lineEdit.text()=='') and ((num in ['*','/']) and (self.lineEdit.text()[-1] in self.listdate)):
            return
        if ((self.flag and num=='.') and (self.lineEdit.text()=='')) or ((self.flag and num=='.') and (self.lineEdit.text()[-1] in self.listdate)):
            self.lineEdit.insert('0')
        if num=='.':
            self.flag=False
        self.lineEdit.insert(num)
    def line(self,num):
        return functools.partial(self.data,str(num))
    def qt(self):
        QMessageBox.aboutQt(self.window)
    def enter(self):
        self.t1=self.lineEdit.text()
        self.t3=self.t1
        self.cfg=configparser.ConfigParser()
        self.cfg.read(r".\setup\setup.ini")
        if self.t1=='':
            return
        for i in self.listdate:
            self.t1=self.t1.strip(i)
        try:
            self.t2=str(round(eval(self.t1),self.cfg.getint('round',"precision")))
        except ZeroDivisionError:
            self.lineEdit.setText('输入错误')
            self.datedata.append('{} = {}'.format(self.t3,'输入错误'))
            self.flag2=False
            self.flag=True
            return
        if self.t2=='0.0' or self.t2=='0':
            self.t2='0'
        else:
            if 0<eval(self.t2)<1:
                pass
            else:
                if eval(self.t2)/int(eval(self.t2))==1.0:
                    self.t2=str(int(eval(self.t2)))
        self.datedata.append('{} = {}'.format(self.t3,self.t2))
        self.lineEdit.setText(self.t2)
        self.flag2=False
        self.flag=True
    def ce(self):
        self.lineEdit.setText('')
        self.flag=True
    def backspace(self):
        if (not self.flag) and self.lineEdit.text()[-1]=='.':
            self.flag=True
        if self.lineEdit.text()=='输入错误':
            self.ce()
            return
        self.lineEdit.setText(self.lineEdit.text()[:-1])
    def historical(self):
        self.win2=datedatawindow(self.datedata)
    def setup(self):
        self.win3=setupwindow()
    def nine(self):
        self.win4=ninewindow()
    def retranslateUi(self, MainWindow):
        super().retranslateUi(self.window)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText('请按键输入')
        self.pushButton.clicked.connect(self.line(0))
        self.pushButton_2.clicked.connect(self.line(1))
        self.pushButton_3.clicked.connect(self.line(2))
        self.pushButton_4.clicked.connect(self.line(3))
        self.pushButton_5.clicked.connect(self.line(4))
        self.pushButton_6.clicked.connect(self.line(5))
        self.pushButton_7.clicked.connect(self.line(6))
        self.pushButton_8.clicked.connect(self.line(7))
        self.pushButton_9.clicked.connect(self.line(8))
        self.pushButton_10.clicked.connect(self.line(9))
        self.pushButton_11.clicked.connect(self.line('.'))
        self.pushButton_12.clicked.connect(self.line('+'))
        self.pushButton_13.clicked.connect(self.line('-'))
        self.pushButton_14.clicked.connect(self.line('*'))
        self.pushButton_15.clicked.connect(self.line('/'))
        self.pushButton_16.clicked.connect(self.ce)
        self.pushButton_17.clicked.connect(self.enter)
        self.pushButton_18.clicked.connect(self.backspace)
        self.action.triggered.connect(self.window.close)
        self.actiona_2.triggered.connect(self.qt)
        self.action_2.triggered.connect(self.nine)
        self.action_Qt.triggered.connect(self.historical)
        self.actiona.triggered.connect(self.setup)
class datedatawindow(datedata.Ui_MainWindow):
    def __init__(self,data):
        self.window=QMainWindow()
        self.window.show()
        self.data=data
        self.setupUi(self.window)
        super().__init__()
    def qt(self):
        QMessageBox.aboutQt(self.window)
    def infile(self):
        self.fileinurl,_=QFileDialog.getOpenFileName(self.window,'导入文件',os.getcwd(),"The historical record Files (*.hr);;All Files (*)")
        if self.fileinurl=='':
            return
        self.listWidget.clear()
        with open(self.fileinurl) as f:
            for i in f:
                self.listWidget.addItem(QListWidgetItem(i.strip()))
    def outfile(self):
        self.fileouturl,_=QFileDialog.getSaveFileName(self.window,'导出文件',os.getcwd(),"The historical record Files (*.hr);;All Files (*)")
        if self.fileouturl=='':
            return
        with open(self.fileouturl,'w') as f:
            for i in self.data:
                f.write(i+'\n')
    def retranslateUi(self, MainWindow):
        super().retranslateUi(self.window)
        self.actiona.triggered.connect(self.window.close)
        self.actiona_2.triggered.connect(self.qt)
        self.pushButton.clicked.connect(self.infile)
        self.pushButton_2.clicked.connect(self.outfile)
        for i in self.data:
            self.listWidget.addItem(QListWidgetItem(i))
class setupwindow(setup.Ui_MainWindow):
    def __init__(self):
        self.window=QMainWindow()
        self.window.show()
        self.cfg=configparser.ConfigParser()
        self.cfg.read(r".\setup\setup.ini")
        self.setupUi(self.window)
        super().__init__()
    def qt(self):
        QMessageBox.aboutQt(self.window)
    def save(self):
        self.cfg.set("round", "precision", str(self.spinBox.value()))  
        self.cfg.write(open(r".\setup\setup.ini", "w"))
        self.window.close()
    def retranslateUi(self, MainWindow):
        super().retranslateUi(self.window)
        self.actiona.triggered.connect(self.window.close)
        self.actiona_2.triggered.connect(self.qt)
        self.pushButton.clicked.connect(self.window.close)
        self.pushButton_2.clicked.connect(self.save)
        self.spinBox.setValue(self.cfg.getint('round',"precision"))
class ninewindow(nine.Ui_MainWindow):
    def __init__(self):
        self.window=QMainWindow()
        self.window.show()
        self.setupUi(self.window)
        super().__init__()
    def qt(self):
        QMessageBox.aboutQt(self.window)
    def retranslateUi(self, MainWindow):
        super().retranslateUi(self.window)
        self.actiona.triggered.connect(self.window.close)
        self.actiona_2.triggered.connect(self.qt)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=window()
    sys.exit(app.exec())
