from PyQt6.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt6.uic import loadUi
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
        
class DeleteConfirm(QDialog):
    def __init__(self):
        super(DeleteConfirm, self).__init__()
        loadUi('delete_articles_confirm.ui', self)
        #finding the summit button and adding summit function to it
        self.delete_confirmation.accepted.connect(lambda: self.yes())
        self.delete_confirmation.rejected.connect(lambda: self.no())        
    def yes(self):
        print('Articles Deleted!')
    def no(self) -> None:
        print('Cancelled!')
        QtCore.QCoreApplication.instance().quit()
        

class DeleteArticle(QDialog):
    def __init__(self):
        super(DeleteArticle, self).__init__()
        loadUi('delete_articles.ui', self)
        
        #clicking the checkbox
        self.choosing_checkbox.stateChanged.connect(self.checkbox_clicked)
        self.confirm_button.accepted.connect(lambda: self.submit())
        self.confirm_button.rejected.connect(lambda: self.reject())
        self.delete_confirmation.accepted.connect(lambda: self.delete())
    def checkbox_clicked(self):
        if self.choosing_checkbox.isChecked() == True:
            self.window = DeleteConfirm()
            if self.window.isVisible():
                self.window.hide()
            else:
                self.window.show()
        else:
            print('Article Not Chose!')
    def submit(self):
        print('yeah i know its ok')
    def reject(self) -> None:
        print('Closing window...')
        QtCore.QCoreApplication.instance().quit()
    def delete(self):
        self.article.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeleteArticle()
    window.show()
    sys.exit(app.exec())