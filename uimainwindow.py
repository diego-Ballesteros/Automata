from automataValidator import AutomataValidator
from automata import Automata
from PySide6.QtCore import (QCoreApplication, QRect,QTranslator,QLibraryInfo)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSpinBox, QLineEdit)
from automatawidget import AutomataWidget
from mainwidget import MainWidget
from automatadrawerwidget import AutomataDrawer
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(900, 550)
        self.setStyleSheet("QMainWindow{background-color: #D5d8d8}")
        self.mainWidget = MainWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.label = QLabel(self.mainWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 21))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Palabra:</span></p></body></html>", None))
        self.spinBox = QSpinBox(self.mainWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(20, 70, 131, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.validatePushButton = QPushButton(self.mainWidget)
        self.validatePushButton.setObjectName(u"pushButton")
        self.validatePushButton.setGeometry(QRect(20, 140, 131, 24))
        self.label_2 = QLabel(self.mainWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 488, 550, 50))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.textEdit = QLineEdit(self.mainWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 10, 651, 21))
        self.label_3 = QLabel(self.mainWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 131, 16))
        self.comboBox = QComboBox(self.mainWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(767, 10, 111, 22))
        self.comboBox.setEditable(True)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Palabra:</span></p></body></html>", None))
        self.spinBox.setPrefix("")
        self.validatePushButton.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estamos onfire", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad de ejecuci\u00f3n:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingles", None))

        #Iniciamos el widget contenedor del automata
        self.automataWidget = AutomataWidget(self.mainWidget)
        self.automataWidget.setGeometry(QRect(170, 50, 700, 450))

        #Inicializamos la Data del automata
        self.automata = Automata()
        speed = self.spinBox.value()

        #Instanciamos el objeto encargado de dibujar y actualizar la UI del automata
        self.automataDrawer = AutomataDrawer(self.automata, self.automataWidget, self.label_2,speed*1000)
        self.automataDrawer.drawAutomata()
        self.addValidateButtonListener()

    def addValidateButtonListener(self):
        self.validatePushButton.clicked.connect(self.validateAutomata)

    def validateAutomata(self):
        input = self.textEdit.text()
        self.automataDrawer.resetAutomata()
        self.automataDrawer.setTime(self.spinBox.value()*1000)
        self.automataValidator = AutomataValidator(Automata(),list(input), self.automataDrawer)
        if self.automataValidator.isInputStringValidate():
            self.label_2.setText(f'\nLa palabra "{input}" SI es Aceptada')
        else:
            self.label_2.setText(f'\nLa palabra "{input}" NO es Aceptada')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())