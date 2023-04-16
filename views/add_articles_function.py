from PyQt6.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from delete_article import DeleteArticle

class AddArticle(QDialog):
    def __init__(self):
        super(AddArticle, self).__init__()
        loadUi('add_articles.ui', self)
        #finding the summit button and adding summit function to it
        self.confirm_button.accepted.connect(lambda: self.submit())
        self.confirm_button.rejected.connect(lambda: self.reject())
    def submit(self):
        print('Article Submitted!')
    def reject(self) -> None:
        print('Article Rejected!')
        QtCore.QCoreApplication.instance().quit()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddArticle()
    window.show()
    sys.exit(app.exec())