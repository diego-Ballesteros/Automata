from automataValidator import AutomataValidator
from automata import Automata
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,QPen)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStatusBar, QLineEdit,
    QWidget)
from customwidget import CustomWidget
from PySide6.QtAxContainer import QAxWidget
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 550)
        self.actionEspa_ol = QAction(MainWindow)
        self.actionEspa_ol.setObjectName(u"actionEspa_ol")
        self.actionIngles = QAction(MainWindow)
        self.actionIngles.setObjectName(u"actionIngles")
        self.actionAdicionar_Idioma = QAction(MainWindow)
        self.actionAdicionar_Idioma.setObjectName(u"actionAdicionar_Idioma")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 21))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(20, 70, 131, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 110, 131, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.validatePushButton = QPushButton(self.centralwidget)
        self.validatePushButton.setObjectName(u"pushButton")
        self.validatePushButton.setGeometry(QRect(20, 140, 131, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 131, 21))	
        self.widget = CustomWidget(self.centralwidget)	
        self.widget.setObjectName(u"widget")	
        self.widget.setGeometry(QRect(190, 60, 701, 561))	
        self.widget.setAutoFillBackground(True)
        self.textEdit = QLineEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 10, 651, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 131, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(767, 10, 111, 22))
        self.comboBox.setEditable(True)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menuIdioma = QMenu(self.menubar)
        self.menuIdioma.setObjectName(u"menuIdioma")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuIdioma.menuAction())
        self.menuIdioma.addAction(self.actionEspa_ol)
        self.menuIdioma.addAction(self.actionIngles)
        self.menuIdioma.addAction(self.actionAdicionar_Idioma)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.addValidateButtonListener()
    # setupUi

    # def paintEvent(self,event):
    #     painter = QPainter(self)
    #     painter.setPen(QPen(Qt.green,  8, Qt.SolidLine))
    #     painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
    #     painter.drawEllipse(200, 200, 70, 70)

    def addValidateButtonListener(self):
        self.validatePushButton.clicked.connect(self.validateAutomata)

    def validateAutomata(self):
        input = self.textEdit.text()
        self.automataValidator = AutomataValidator(Automata(),list(input))
        if self.automataValidator.isInputStringValidate():
            self.label_2.setText(f'\nEl caracter "{input}" SI es Aceptado')
        else:
            self.label_2.setText(f'\nEl caracter "{input}" NO es Aceptado')

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEspa_ol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.actionIngles.setText(QCoreApplication.translate("MainWindow", u"Ingles", None))
        self.actionAdicionar_Idioma.setText(QCoreApplication.translate("MainWindow", u"Adicionar Idioma", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Palabra:</span></p></body></html>", None))
        self.spinBox.setPrefix("")
        self.validatePushButton.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estas onfire", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad de ejecuci\u00f3n:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingles", None))

        self.menuIdioma.setTitle(QCoreApplication.translate("MainWindow", u"Idioma", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())