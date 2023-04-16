from PyQt6.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from add_articles_function import AddArticle
from delete_article import DeleteArticle

class ArticleManagement(QDialog):
    def __init__(self):
        super(ArticleManagement, self).__init__()
        loadUi('article_management.ui', self)
        #finding the summit button and adding summit function to it
        self.add_articles_button.clicked.connect(lambda: self.add_articles())
        self.delete_articles_button.clicked.connect(lambda: self.delete_articles())
    def add_articles(self):
        self.window = AddArticle()
        if self.window.isVisible():
            self.window.hide()
        else:
            self.window.show()
        print('Adding Article!')
    
    def delete_articles(self) -> None:
        self.window = DeleteArticle()
        if self.window.isVisible():
            self.window.hide()
        else:
            self.window.show()
        print('Article Deleted!')
        QtCore.QCoreApplication.instance().quit()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArticleManagement()
    window.show()
    sys.exit(app.exec())