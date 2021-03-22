import pip
import os

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Pip List
install("PyQt5")
# Code
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import webbrowser
import shutil

form_class = uic.loadUiType("main.ui")[0]

count = 0

def btn_clicked():
    webbrowser.open("https://github.com/misilelab")

def btn2_clicked():
    global count
    if count < 3:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        count = count + 1
    else:
        webbrowser.open("http://warning.or.kr/")

modpack = ""

# noinspection PyGlobalUndefined
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        global modpack
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(btn_clicked)
        self.pushButton_2.clicked.connect(btn2_clicked)
        self.setWindowTitle('QCheckBox')
        self.pushButton_3.clicked.connect(self.btn3_clicked)
        self.checkBox1 = QCheckBox("CreativeCraft+", self)
        self.checkBox1.move(10, 20)
    def closeEvent(self, event):
        self.deleteLater()
    def btn3_clicked(self):
        if self.checkBox1.isChecked():
            try:
                os.remove("CreativeCraft+ Mods")
                os.remove("CreativeCraft+.zip")
                os.remove("CreativeCraft--main")
            except FileNotFoundError or FileExistsError:
                pass
            os.system("curl https://codeload.github.com/MisileLab/CreativeCraft-/zip/main > CreativeCraft+.zip")
            os.system("unzip CreativeCraft+.zip")
            os.remove("CreativeCraft+.zip")
            os.makedirs("CreativeCraft+ Mods")
            shutil.move("CreativeCraft--main\overrides\mods", "CreativeCraft+ Mods")
            os.remove("./CreativeCraft--main")
        else:
            print("SANS")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()