# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow ,QTableWidgetItem

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(236, 236, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 108, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(218, 217, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(470, 50, 361, 531))

        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")

        self.SummList = QtWidgets.QTableWidget(self.centralwidget)
        self.SummList.setGeometry(QtCore.QRect(487, 280, 250, 265))
        self.SummList.setRowCount(1)
        self.SummList.setColumnCount(1)
        self.SummList.setObjectName("SummList")
        self.SummList.setColumnWidth(0, 280)
        self.SummList.setHorizontalHeaderLabels(["Сумматоры"])

        self.layoutbox = QtWidgets.QWidget(self.centralwidget)
        self.layoutbox.setGeometry(QtCore.QRect(475, 220, 350, 350))
        self.layoutbox.setObjectName("layoutbox")
        self.layout = QtWidgets.QHBoxLayout(self.layoutbox)
        self.layout.setObjectName("layout")
        self.layout.addWidget(self.SummList)


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 491, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.RegValue = QtWidgets.QSpinBox(self.frame)
        self.RegValue.setGeometry(QtCore.QRect(40, 50, 61, 31))
        self.RegValue.setObjectName("RegValue")

        self.RegValueLabel = QtWidgets.QLabel(self.frame)
        self.RegValueLabel.setGeometry(QtCore.QRect(25, 20, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RegValueLabel.setFont(font)
        self.RegValueLabel.setObjectName("label_4")

        self.SummValue = QtWidgets.QSpinBox(self.frame)
        self.SummValue.setGeometry(QtCore.QRect(150, 50, 61, 31))
        self.SummValue.setObjectName("SummValue")

        self.SummValueLabel = QtWidgets.QLabel(self.frame)
        self.SummValueLabel.setGeometry(QtCore.QRect(125, 15, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SummValueLabel.setFont(font)
        self.SummValueLabel.setObjectName("label_5")

        self.SummCount = QtWidgets.QLineEdit(self.frame)
        self.SummCount.setGeometry(QtCore.QRect(40, 115, 51, 41))
        self.SummCount.setObjectName("SummCount")

        self.NumSummLabel = QtWidgets.QLabel(self.frame)
        self.NumSummLabel.setGeometry(QtCore.QRect(6, 90, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NumSummLabel.setFont(font)
        self.NumSummLabel.setObjectName("NumSumm")

        self.SummInputLabel = QtWidgets.QLabel(self.frame)
        self.SummInputLabel.setGeometry(QtCore.QRect(175, 90, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SummInputLabel.setFont(font)
        self.SummInputLabel.setObjectName("SummInputLabel")

        self.SummInputLine = QtWidgets.QLineEdit(self.frame)
        self.SummInputLine.setGeometry(QtCore.QRect(140, 120, 120, 31))
        self.SummInputLine.setObjectName("lineEdit_4")

        self.ChangeSummButton = QtWidgets.QPushButton(self.frame)
        self.ChangeSummButton.setGeometry(QtCore.QRect(270, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ChangeSummButton.setFont(font)
        self.ChangeSummButton.setObjectName("ChangeSummButton")

        self.CleanButton = QtWidgets.QPushButton(self.frame)
        self.CleanButton.setGeometry(QtCore.QRect(120, 130, 5, 5))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CleanButton.setFont(font)
        self.CleanButton.setObjectName("CleanButton")

        self.HelpButton = QtWidgets.QPushButton(self.frame)
        self.HelpButton.setGeometry(QtCore.QRect(120, 140, 5, 5))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.HelpButton.setFont(font)
        self.HelpButton.setObjectName("HelpButton")

        self.ParamInputButton = QtWidgets.QPushButton(self.frame)
        self.ParamInputButton.setGeometry(QtCore.QRect(260, 45, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ParamInputButton.setFont(font)
        self.ParamInputButton.setObjectName("ParamInputButton")

        self.EncodeData = QtWidgets.QTextEdit(self.centralwidget)
        self.EncodeData.setGeometry(QtCore.QRect(40, 420, 401, 87))
        self.EncodeData.setObjectName("EncodeData")

        self.InpStrLabel = QtWidgets.QLabel(self.centralwidget)
        self.InpStrLabel.setGeometry(QtCore.QRect(180, 50, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InpStrLabel.setFont(font)
        self.InpStrLabel.setObjectName("label")

        self.EncodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.EncodeLabel.setGeometry(QtCore.QRect(130, 390, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EncodeLabel.setFont(font)
        self.EncodeLabel.setObjectName("label_2")

        self.DecodeData = QtWidgets.QTextEdit(self.centralwidget)
        self.DecodeData.setGeometry(QtCore.QRect(40, 550, 401, 87))
        self.DecodeData.setObjectName("DecodeData")

        self.DecodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.DecodeLabel.setGeometry(QtCore.QRect(130, 520, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DecodeLabel.setFont(font)
        self.DecodeLabel.setObjectName("label_3")

        self.CodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.CodeButton.setGeometry(QtCore.QRect(550, 590, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CodeButton.setFont(font)
        self.CodeButton.setObjectName("pushButton")

        self.InputSrting = QtWidgets.QTextEdit(self.centralwidget)
        self.InputSrting.setGeometry(QtCore.QRect(60, 80, 361, 301))
        self.InputSrting.setObjectName("InputSrting")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.set_text(self.output)
        # self.register()
        self.Functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coding - Decoding"))
        self.RegValueLabel.setText(_translate("MainWindow", "Регистры"))
        self.SummValueLabel.setText(_translate("MainWindow", "Сумматоры"))
        self.NumSummLabel.setText(_translate("MainWindow", "№ сумматора"))
        self.ChangeSummButton.setText(_translate("MainWindow", "ВВОД"))
        self.ParamInputButton.setText(_translate("MainWindow", "ИЗМ"))
        self.SummInputLabel.setText(_translate("MainWindow", "СУММ"))
        self.InpStrLabel.setText(_translate("MainWindow", "Входная строка"))
        self.EncodeLabel.setText(_translate("MainWindow", "Закодированные данные"))
        self.DecodeLabel.setText(_translate("MainWindow", "Декодированные данные"))
        self.CodeButton.setText(_translate("MainWindow", "ПУСК"))

    def Clean(self):
        self.InputSrting.clear()
        self.EncodeData.clear()
        self.DecodeData.clear()
        self.RegValue.setValue(0)
        self.SummValue.setValue(0)
        self.SummList.setRowCount(0)
        self.SummList.setColumnCount(1)
        return 0

    def Help(self):
        self.InputSrting.setText("Stroka, к0т0рую над0 3акодир0в4ть")
        self.RegValue.setValue(3)
        self.SummValue.setValue(4)
        RegVal = self.RegValue.value()
        SummVal = self.SummValue.value()
        self.SummList.setRowCount(SummVal)
        self.SummList.setColumnCount(1)
        print(RegVal)

        self.SummList.setItem(0, 0, QTableWidgetItem("011"))
        self.SummList.setItem(1, 0, QTableWidgetItem("110"))
        self.SummList.setItem(2, 0, QTableWidgetItem("101"))
        self.SummList.setItem(3, 0, QTableWidgetItem("111"))

        self.PullOutData()

        self.layout.addWidget(self.SummList)

        return 0

    def zero(self):
        return 0

    def Coding(self):

        InputString = self.InputSrting.toPlainText()
        EncodeText = ""
        OutputText = ""
        RegVal = self.RegValue.value()
        SummVal = self.SummValue.value()
        SummMass = self.PullOutData()
        print("Входная строка - ",InputString, EncodeText, OutputText, RegVal, SummVal, SummMass)

        def ToBits(InputString, Encoding='utf-8', Errors='surrogatepass'):
            Bits = bin(int.from_bytes(InputString.encode(Encoding, Errors), 'big'))[2:]
            return Bits.zfill(8 * ((len(Bits) + 7) // 8))

        # Преобразование двоичнго кода (utf-8) в строку
        def ToText(Bits, encoding='utf-8', errors='surrogatepass'):
            n = int(Bits, 2)
            return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

        def Encode(RegVal, BitsChain, Tabel):
            Out = ""
            Reg = "0" * RegVal                                                 # регистр для сравнения длиной RegVal (число регистров)
            for i in range(0, len(BitsChain), 1):
                temp = BitsChain[i]                                            # сравниваемый бит
                Reg = Disp(list(Reg), 1)                                       # смещение битов
                Reg[0] = temp                                                  # на вход поступает бит
                for j in range(0, len(Tabel), 1):                              #
                    if Tabel[j][2] == temp and "".join(Reg) == Tabel[j][0]:    # сравнение с элементами Tabel
                        Out += Tabel[j][1]                                     #
                        Reg = Tabel[j][0]                                      #
            return Out

        def Disp(ListReg, n):                                                   # функция для смещения битов
            y = ListReg.copy()
            for i in range(len(y) - 1, n - 1, -1):
                y[i] = y[i - n]
            for i in range(len(y) - (len(y) - n), 0, -1):
                y[i - 1] = 0
            return y

        def Tabel(RegVal, SumMass):
            Tab = []  # mass[i] = [cостояние регистров],[значение сумматоров],[поступивший бит],[последние k-1 регистры],[первые k-1 регистры]

            for i in range(2 ** RegVal):
                a = format(i, 'b').rjust(RegVal, '0')
                Tab.append([a, Summ(a, SumMass), a[0], a[1:], a[:-1]])

            return Tab

        def TabelPrint(k, SumMass):
            Tab = []  # mass[i] = [cостояние регистров],[значение сумматоров],[поступивший бит],[последние k-1 регистры],[первые k-1 регистры]

            for i in range(2 ** k):
                a = format(i, 'b').rjust(k, '0')
                Tab.append([a, Summ(a, SumMass), a[0], a[1:], a[:-1]])

            print("Таблица связей")
            for i in range(0, 2 ** k, 1):
                print(Tab[i])
            print (type(Tab))
            return Tab

        def Summ(s, g):
            out = ""

            for i in range(len(g)):
                x = 0
                for j in range(len(g[i])):
                    if g[i][j] == 1:
                        x = x ^ int(s[j])
                out = out + str(x)

            return out

        def Decode(EncodeChain, SummVal, RegVal ,Tabel ):
            out = ""
            chek = "0" * (RegVal - 1) # проверка
            for i in range(0, len(EncodeChain), SummVal):
                buf = ""
                for k in range(0, SummVal, 1):
                    buf = buf + str(EncodeChain[i + k])
                for j in range(0, len(Tabel), 1):
                    if buf == Tabel[j][1] and chek == Tabel[j][3]:
                        out += Tabel[j][2]
                        chek = Tabel[j][4]
                        break
            print("34113",out)
            return out



        BitsChain = ToBits(InputString)
        print("Входные биты - ",BitsChain)  # цепочка битов
        TabelPrint(RegVal, SummMass)
        EncodeChain = Encode(RegVal, BitsChain, Tabel(RegVal, SummMass))
        print ("Закодированная последовательность - ",EncodeChain)  #
        self.EncodeData.setText(EncodeChain)
        DecodeChain = Decode(EncodeChain, SummVal, RegVal ,Tabel(RegVal, SummMass) )
        print("Декодированная последовательность - ", DecodeChain)
        FinalyOutput = ToText(DecodeChain)
        print("Обратно в текст - ", FinalyOutput)
        self.DecodeData.setText(FinalyOutput)

        return 0

    def ChangeSumm(self):

        Count = self.SummCount.text()
        ChangeValue = self.SummInputLine.text()
        print(ChangeValue)
        self.SummList.setItem(int(Count) - 1, 0, QTableWidgetItem(ChangeValue))


    def ParamInput(self):

        RegVal = self.RegValue.value()
        SummVal = self.SummValue.value()

        self.SummList.setRowCount(SummVal)
        self.SummList.setColumnCount(1)

        for x in range(0, SummVal, 1):
            self.SummList.setItem(int(x), 0, QTableWidgetItem("0"*RegVal))
            print(RegVal)

        self.layout.addWidget(self.SummList)

        return 0

    massofsum = []

    def PullOutData(self):
        self.massofsum = []
        for i in range(self.SummList.rowCount()):
            self.massofsum.append(self.SummList.item(i, 0).text())
            print(self.SummList.item(i, 0).text())
        for i in range(len(self.massofsum)):
            self.massofsum[i] = list(map(int, list(self.massofsum[i])))
        print( self.massofsum)
        return self.massofsum

    def Functions(self):
        self.CleanButton.clicked.connect(self.Clean)
        self.CodeButton.clicked.connect(self.Coding)
        self.HelpButton.clicked.connect(self.Help)
        self.ParamInputButton.clicked.connect(self.ParamInput)
        self.ChangeSummButton.clicked.connect(self.ChangeSumm)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

