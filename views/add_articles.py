# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_articles.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_articles_window(object):
    def setupUi(self, add_articles_window):
        add_articles_window.setObjectName("add_articles_window")
        add_articles_window.resize(480, 640)
        add_articles_window.setMinimumSize(QtCore.QSize(4, 0))
        add_articles_window.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.497537, y1:1, x2:0.468443, y2:0.301, stop:0 rgba(209, 243, 252, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(add_articles_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.banner_frame = QtWidgets.QFrame(add_articles_window)
        self.banner_frame.setStyleSheet("QFrame{\n"
"border-style: outset;\n"
"border-radius: 20px;\n"
"border-color: rgb(0, 240, 255);\n"
"border-width: 0.5px;\n"
"padding: 1px;\n"
"background-color: rgba(102, 255, 255, 50)\n"
"}\n"
"QLabel{\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0)\n"
"}\n"
"QPushButton{\n"
"border: none;\n"
"background-color: rgba(0, 0, 0, 0)\n"
"}")
        self.banner_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.banner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.banner_frame.setObjectName("banner_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.banner_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_articles_title = QtWidgets.QLabel(self.banner_frame)
        self.add_articles_title.setStyleSheet("font: 30pt \".AppleSystemUIFont\";")
        self.add_articles_title.setObjectName("add_articles_title")
        self.horizontalLayout.addWidget(self.add_articles_title, 0, QtCore.Qt.AlignLeft)
        self.add_articles_logo = QtWidgets.QPushButton(self.banner_frame)
        self.add_articles_logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/add_article_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_articles_logo.setIcon(icon)
        self.add_articles_logo.setIconSize(QtCore.QSize(64, 64))
        self.add_articles_logo.setObjectName("add_articles_logo")
        self.horizontalLayout.addWidget(self.add_articles_logo, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.banner_frame, 0, QtCore.Qt.AlignTop)
        self.title_label = QtWidgets.QLabel(add_articles_window)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.title_edit = QtWidgets.QPlainTextEdit(add_articles_window)
        self.title_edit.setMinimumSize(QtCore.QSize(0, 27))
        self.title_edit.setMaximumSize(QtCore.QSize(16777215, 27))
        self.title_edit.setObjectName("title_edit")
        self.verticalLayout.addWidget(self.title_edit)
        self.description_label = QtWidgets.QLabel(add_articles_window)
        self.description_label.setObjectName("description_label")
        self.verticalLayout.addWidget(self.description_label)
        self.description_edit = QtWidgets.QPlainTextEdit(add_articles_window)
        self.description_edit.setMinimumSize(QtCore.QSize(0, 100))
        self.description_edit.setMaximumSize(QtCore.QSize(16777215, 110))
        self.description_edit.setObjectName("description_edit")
        self.verticalLayout.addWidget(self.description_edit)
        self.content_label = QtWidgets.QLabel(add_articles_window)
        self.content_label.setObjectName("content_label")
        self.verticalLayout.addWidget(self.content_label)
        self.content_edit = QtWidgets.QPlainTextEdit(add_articles_window)
        self.content_edit.setPlainText("")
        self.content_edit.setOverwriteMode(True)
        self.content_edit.setPlaceholderText("")
        self.content_edit.setObjectName("content_edit")
        self.verticalLayout.addWidget(self.content_edit)
        self.category_label = QtWidgets.QLabel(add_articles_window)
        self.category_label.setObjectName("category_label")
        self.verticalLayout.addWidget(self.category_label)
        self.category_edit = QtWidgets.QComboBox(add_articles_window)
        self.category_edit.setObjectName("category_edit")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.category_edit.addItem("")
        self.verticalLayout.addWidget(self.category_edit, 0, QtCore.Qt.AlignLeft)
        self.confirm_button = QtWidgets.QDialogButtonBox(add_articles_window)
        self.confirm_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirm_button.setObjectName("confirm_button")
        self.verticalLayout.addWidget(self.confirm_button)

        self.retranslateUi(add_articles_window)
        QtCore.QMetaObject.connectSlotsByName(add_articles_window)

    def retranslateUi(self, add_articles_window):
        _translate = QtCore.QCoreApplication.translate
        add_articles_window.setWindowTitle(_translate("add_articles_window", "Add articles"))
        self.add_articles_title.setText(_translate("add_articles_window", "Add Articles"))
        self.title_label.setText(_translate("add_articles_window", "Title:"))
        self.title_edit.setDocumentTitle(_translate("add_articles_window", "sddd"))
        self.description_label.setText(_translate("add_articles_window", "Description:"))
        self.content_label.setText(_translate("add_articles_window", "Contents:"))
        self.category_label.setText(_translate("add_articles_window", "Category:"))
        self.category_edit.setItemText(0, _translate("add_articles_window", "Economy"))
        self.category_edit.setItemText(1, _translate("add_articles_window", "Politics"))
        self.category_edit.setItemText(2, _translate("add_articles_window", "Traffic"))
        self.category_edit.setItemText(3, _translate("add_articles_window", "Medical"))
        self.category_edit.setItemText(4, _translate("add_articles_window", "Sport"))
        self.category_edit.setItemText(5, _translate("add_articles_window", "Travel"))
        self.category_edit.setItemText(6, _translate("add_articles_window", "Entertain"))
        self.category_edit.setItemText(7, _translate("add_articles_window", "Science and Technology"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_articles_window = QtWidgets.QDialog()
    ui = Ui_add_articles_window()
    ui.setupUi(add_articles_window)
    add_articles_window.show()
    sys.exit(app.exec_())