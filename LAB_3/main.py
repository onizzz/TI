import numpy
import PIL

import random
import numpy as np
from PIL import Image
from os import getcwd
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'yfyfvfjfjy'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.FileExplorer()
        self.Reading()

        self.show()

    def FileExplorer(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file, _ = QFileDialog.getOpenFileNames(self, "Файловый менеджер", getcwd() ,
                                                "Image (*.jpg *.png *.bmp *.eps *.im *.jpeg *.msp *.pcx *.ppm *.tiff *.webp *.ico *.psd )", options=QFileDialog.Options())
        self.file = " ".join(self.file)

        # return self.file


    def Reading(self):
        img = Image.open(self.file)
        # if (type(img)) !=
        print (img)
        # if self.file
        arr = np.asarray(img, dtype='uint8')

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j])

        # print(arr)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


