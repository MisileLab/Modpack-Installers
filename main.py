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
        self.CreativeCraftPlus = QCheckBox("CreativeCraft+", self)
        self.CreativeCraftPlus.move(10, 10)
        self.BasicCraft = QCheckBox("BasicCraft", self)
        self.BasicCraft.move(10, 30)
    def btn3_clicked(self):
        print("1234")
        if self.CreativeCraftPlus.isChecked():
            try:
                os.rmdir("CreativeCraft+ Mods")
                os.remove("CreativeCraft+.zip")
                os.rmdir("CreativeCraft--main")
            except FileNotFoundError or FileExistsError:
                pass
            os.system("curl https://codeload.github.com/MisileLab/CreativeCraft-/zip/main > CreativeCraft+.zip")
            os.system("unzip CreativeCraft+.zip")
            os.remove("CreativeCraft+.zip")
            os.makedirs("CreativeCraft+ Mods")
            shutil.move("CreativeCraft--main\overrides\mods", "CreativeCraft+ Mods")
            os.rmdir("CreativeCraft--main")
        if self.BasicCraft.isChecked():
            try:
                os.rmdir("BasicCraft Mods")
                os.remove("BasicCraft.zip")
                os.rmdir("Basiccraft-main")
            except FileNotFoundError or FileExistsError:
                pass
                print("2130")
            os.system("curl https://codeload.github.com/MisileLab/basiccraft/zip/main > BasicCraft.zip")
            os.system("unzip BasicCraft.zip")
            os.remove("BasicCraft.zip")
            os.makedirs("BasicCraft Mods")
            if self.plainTextEdit.toPlainText() == "1.16.5":
                shutil.move("Basiccraft-main\\1.16.5", "BasicCraft Mods")
                os.rmdir("Basiccraft-main")
            elif self.plainTextEdit.toPlainText() == "1.16.4":
                shutil.move("Basiccraft-main\\1.16.4", "BasicCraft Mods")
                os.rmdir("Basiccraft-main")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()