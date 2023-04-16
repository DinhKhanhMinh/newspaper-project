# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'article_management.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_articles_management(object):
    def setupUi(self, articles_management):
        articles_management.setObjectName("articles_management")
        articles_management.resize(619, 640)
        articles_management.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.497537, y1:1, x2:0.468443, y2:0.301, stop:0 rgba(209, 243, 252, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(articles_management)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(articles_management)
        self.header.setStyleSheet("QFrame{\n"
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
"")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.banner = QtWidgets.QFrame(self.header)
        self.banner.setStyleSheet("border: none")
        self.banner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.banner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.banner.setObjectName("banner")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.banner)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.articles_management_logo = QtWidgets.QPushButton(self.banner)
        self.articles_management_logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/articles_management_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.articles_management_logo.setIcon(icon)
        self.articles_management_logo.setIconSize(QtCore.QSize(64, 64))
        self.articles_management_logo.setObjectName("articles_management_logo")
        self.horizontalLayout_2.addWidget(self.articles_management_logo)
        self.articles_management_title = QtWidgets.QLabel(self.banner)
        self.articles_management_title.setStyleSheet("font: 24pt \".AppleSystemUIFont\";")
        self.articles_management_title.setObjectName("articles_management_title")
        self.horizontalLayout_2.addWidget(self.articles_management_title)
        self.horizontalLayout.addWidget(self.banner, 0, QtCore.Qt.AlignLeft)
        self.buttons = QtWidgets.QFrame(self.header)
        self.buttons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons.setObjectName("buttons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.buttons)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_articles_button = QtWidgets.QPushButton(self.buttons)
        self.add_articles_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/add_article.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_articles_button.setIcon(icon1)
        self.add_articles_button.setIconSize(QtCore.QSize(16, 16))
        self.add_articles_button.setObjectName("add_articles_button")
        self.verticalLayout_2.addWidget(self.add_articles_button)
        self.delete_articles_button = QtWidgets.QPushButton(self.buttons)
        self.delete_articles_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/delete_article.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_articles_button.setIcon(icon2)
        self.delete_articles_button.setObjectName("delete_articles_button")
        self.verticalLayout_2.addWidget(self.delete_articles_button)
        self.horizontalLayout.addWidget(self.buttons)
        self.verticalLayout.addWidget(self.header)
        self.articles_display = QtWidgets.QScrollArea(articles_management)
        self.articles_display.setWidgetResizable(True)
        self.articles_display.setObjectName("articles_display")
        self.articles_list = QtWidgets.QWidget()
        self.articles_list.setGeometry(QtCore.QRect(0, 0, 593, 480))
        self.articles_list.setStyleSheet("QFrame{\n"
"        border-radius: 1px;\n"
"        border-style: solid;\n"
"        border-color: rgb(179, 179, 179);\n"
"        border-width: 0.5px 0.5px 0.5px 0.5px;\n"
"}")
        self.articles_list.setObjectName("articles_list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.articles_list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.article = QtWidgets.QFrame(self.articles_list)
        self.article.setMinimumSize(QtCore.QSize(0, 140))
        self.article.setMaximumSize(QtCore.QSize(16777215, 150))
        self.article.setStyleSheet("QFrame{\n"
"        border-radius: 1px;\n"
"        border-style: solid;\n"
"        border-color: rgb(179, 179, 179);\n"
"        border-width: 0.5px 0.5px 0.5px 0.5px;\n"
"}")
        self.article.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.article.setFrameShadow(QtWidgets.QFrame.Raised)
        self.article.setObjectName("article")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.article)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.image_display = QtWidgets.QFrame(self.article)
        self.image_display.setMinimumSize(QtCore.QSize(190, 0))
        self.image_display.setMaximumSize(QtCore.QSize(200, 16777215))
        self.image_display.setStyleSheet("QFrame{\n"
"        border-radius: 1px;\n"
"        border-style: solid;\n"
"        border-color: rgb(179, 179, 179);\n"
"        border-width: 0.5px 0.5px 0.5px 0.5px;\n"
"}\n"
"QLabel{\n"
"    border: none\n"
"}")
        self.image_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_display.setObjectName("image_display")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.image_display)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.image = QtWidgets.QLabel(self.image_display)
        self.image.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.image.setObjectName("image")
        self.horizontalLayout_4.addWidget(self.image)
        self.horizontalLayout_3.addWidget(self.image_display)
        self.title_description_display = QtWidgets.QFrame(self.article)
        self.title_description_display.setStyleSheet("QLabel{\n"
"border: none\n"
"}")
        self.title_description_display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_description_display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_description_display.setObjectName("title_description_display")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.title_description_display)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.title = QtWidgets.QLabel(self.title_description_display)
        self.title.setStyleSheet("font: 18pt \".AppleSystemUIFont\";")
        self.title.setObjectName("title")
        self.verticalLayout_4.addWidget(self.title)
        self.description = QtWidgets.QLabel(self.title_description_display)
        self.description.setObjectName("description")
        self.verticalLayout_4.addWidget(self.description)
        self.horizontalLayout_3.addWidget(self.title_description_display)
        self.verticalLayout_3.addWidget(self.article, 0, QtCore.Qt.AlignTop)
        self.articles_display.setWidget(self.articles_list)
        self.verticalLayout.addWidget(self.articles_display)

        self.retranslateUi(articles_management)
        QtCore.QMetaObject.connectSlotsByName(articles_management)

    def retranslateUi(self, articles_management):
        _translate = QtCore.QCoreApplication.translate
        articles_management.setWindowTitle(_translate("articles_management", "Your Articles"))
        self.articles_management_title.setText(_translate("articles_management", "Your Articles"))
        self.add_articles_button.setText(_translate("articles_management", "Add"))
        self.delete_articles_button.setText(_translate("articles_management", "Delete"))
        self.image.setText(_translate("articles_management", "img"))
        self.title.setText(_translate("articles_management", "Title"))
        self.description.setText(_translate("articles_management", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    articles_management = QtWidgets.QDialog()
    ui = Ui_articles_management()
    ui.setupUi(articles_management)
    articles_management.show()
    sys.exit(app.exec_())
