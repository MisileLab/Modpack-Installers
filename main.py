import pip
import os

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Code
import sys
try:
    from PyQt5.QtWidgets import *
    from PyQt5 import uic
    from PyQt5.QtCore import Qt
    from typing import Optional
except ModuleNotFoundError:
    install("PyQt5")
    install("typing")
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import webbrowser
import shutil

form_class = uic.loadUiType("main.ui")[0]

count = 0

def btn_clicked():
    webbrowser.open("https://github.com/misilelab")

def Notice(self, modpackname:str):
    QMessageBox.question(
        self, 'Modpack Installer', f"{modpackname} Installed",
        QMessageBox.Ok
    )

modpack = ""
path = os.getcwd()

def deletetest(modfolder:str, repo:str, branch:str="main"):
    path1 = os.getcwd()
    repounzip = f"{repo}-{branch}"
    repozip = f"{repo}.zip"
    try:
        shutil.rmtree(rf"{path1}\{modfolder}")
        os.remove(repozip)
        shutil.rmtree(rf"{path1}\{repounzip}")
    except FileNotFoundError:
        raise FileNotFoundError

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        global modpack
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(btn_clicked)
        self.setWindowTitle('QCheckBox')
        self.pushButton_3.clicked.connect(self.btn3_clicked)
    def btn3_clicked(self):
        if self.CreativeCraftPlus.isChecked():
            try:
                shutil.rmtree(path + "\CreativeCraft+ Mods")
                os.remove("CreativeCraft+.zip")
                shutil.rmtree(path + "\CreativeCraft--main")
            except FileNotFoundError or FileExistsError:
                pass
            os.system("curl https://codeload.github.com/MisileLab/CreativeCraft-/zip/main > CreativeCraft+.zip")
            os.system("unzip CreativeCraft+.zip")
            os.remove("CreativeCraft+.zip")
            os.makedirs("CreativeCraft+ Mods")
            shutil.move("CreativeCraft--main\overrides\mods", "CreativeCraft+ Mods")
            shutil.rmtree(path + "\CreativeCraft--main")
            Notice(self, modpackname="CreativeCraft+")
        if self.BasicCraft.isChecked():
            try:
                shutil.rmtree(path + "\BasicCraft Mods")
                os.remove("BasicCraft.zip")
                shutil.rmtree(path + "\Basiccraft-main")
            except FileNotFoundError or FileExistsError:
                pass
            os.system("curl https://codeload.github.com/MisileLab/basiccraft/zip/main > BasicCraft.zip")
            os.system("unzip BasicCraft.zip")
            os.remove("BasicCraft.zip")
            os.makedirs("BasicCraft Mods")
            if self.plainTextEdit.toPlainText() == "1.16.5":
                shutil.move("Basiccraft-main\\1.16.5", "BasicCraft Mods")
            elif self.plainTextEdit.toPlainText() == "1.16.4":
                shutil.move("Basiccraft-main\\1.16.4", "BasicCraft Mods")
            shutil.rmtree(path + r"\basiccraft-main")
            Notice(self, modpackname="BasicCraft")
        if self.CreateModpack.isChecked():
            try:
                deletetest(modfolder="CreateModpack mods", repo="CreateModpack")
            except FileNotFoundError:
                pass
            os.system("curl https://codeload.github.com/MisileLab/CreateModpack/zip/main > CreateModpack.zip")
            os.system("unzip CreateModpack.zip")
            os.remove("CreateModpack.zip")
            os.makedirs("CreateModpack mods")
            shutil.move("CreateModpack-main\overrides\mods", "CreateModpack mods")
            shutil.rmtree(path + "\CreateModpack-main")
            Notice(self, modpackname="CreateModpack")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
