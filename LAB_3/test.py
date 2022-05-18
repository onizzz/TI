import sys
from os import getcwd
import numpy as np
from PIL import Image

from PyQt5.QtGui     import QIcon, QPixmap
from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QFileDialog

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()

class mostrarImagen(QDialog):
    def __init__(self, parent=None):
        super(mostrarImagen, self).__init__(parent)

        self.setWindowTitle("Выбор картинки")
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 400)

        self.initUI()

    def initUI(self):

        self.labelImage = QLabelClickable(self)
        self.labelImage.setGeometry(15, 15, 118, 130)
        self.labelImage.setToolTip("Картинка")
        self.labelImage.setCursor(Qt.PointingHandCursor)

        self.labelImage.setStyleSheet(
            "QLabel {background-color: write; border: 1px solid "
            "#0DFFD7; border-radius: 5px;}")
        self.labelImage.setAlignment(Qt.AlignCenter)

        # ... по нажатии кнопки выходило окно, в котором пользователь указывает где находиться картинка.
        buttonSelect = QPushButton("Выбрать картинку", self)
        buttonSelect.setToolTip("buttonSelect")
        buttonSelect.setCursor(Qt.PointingHandCursor)
        buttonSelect.setGeometry(143, 15, 120, 25)

        buttonRemove = QPushButton("Удалить картинку", self)
        buttonRemove.setToolTip("buttonRemove")
        buttonRemove.setCursor(Qt.PointingHandCursor)
        buttonRemove.setGeometry(143, 45, 120, 25)

        ButtonReading = QPushButton("Считать картинку", self)
        buttonRemove.setToolTip("buttonRemove")
        buttonRemove.setCursor(Qt.PointingHandCursor)
        buttonRemove.setGeometry(143, 45, 120, 25)

        self.labelImage.clicked.connect(self.FileExplorer)
        buttonSelect.clicked.connect(self.FileExplorer)
        buttonRemove.clicked.connect(lambda: self.labelImage.clear())
        ButtonReading.clicked.connect(self.Reading)

    def FileExplorer(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file, _ = QFileDialog.getOpenFileNames(self, "Файловый менеджер", getcwd(),
                                                    "Image (*.jpg *.png *.bmp *.eps *.im *.jpeg *.msp *.pcx *.ppm *.tiff *.webp *.ico *.psd )",
                                                    options=options)
        self.file = " ".join(self.file)

        if self.file:
            # Функции QPixmap.scaled() возвращают масштабированные копии pixmap
            pixmapImagen = QPixmap(self.file).scaled(112, 128,
                               Qt.KeepAspectRatio,
                               Qt.SmoothTransformation)
            self.labelImage.setPixmap(pixmapImagen)           # После эта картинка вставляется в QLablе.


    def Reading(self):
        img = Image.open(self.file)
        print (img)
        # if self.file
        arr = np.asarray(img, dtype='uint8')
        print(self.file)

        print(arr)


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    main = mostrarImagen()
    main.show()
    sys.exit(app.exec_())