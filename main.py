# This Python file uses the following encoding: utf-8

import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from controller.newspaper import Newspapers
from views.interface import Interface
from controller.methods import get_instance



# Important:

# You need to run the following command to generate the ui_form.py file

#     pyside6-uic form.ui -o ui_form.py, or

#     pyside2-uic form.ui -o ui_form.py


assets = os.path.join(os.path.dirname(__file__), "assets")

class MainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.np_instance = get_instance()
        # image = self.np_instance.get_hot_articles()[0]
        self.ui = Interface()
        # self.ui.hot_news_image_2.setPixmap(QtGui.QPixmap(os.path.join(assets, image)))
        self.ui.setupUi(self)





if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MainWindow()

    widget.show()

    sys.exit(app.exec())

