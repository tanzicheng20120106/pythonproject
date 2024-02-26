import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import student_window
class Main_UI(student_window.Ui_student_window):
    def __init__(self):
        self.window=QMainWindow()
        self.window.show()
        self.setupUi(self.window)
        super().__init__()
    def retranslateUi(self, MainWindow):
        super().retranslateUi(self.window)
        self.exit_pro.triggered.connect(self.window.close)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=Main_UI()
    sys.exit(app.exec())