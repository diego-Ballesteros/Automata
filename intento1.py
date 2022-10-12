from msilib.schema import Class
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
from automatawidget import AutomataWidget
from PySide6.QtAxContainer import QAxWidget
from mainwidget import MainWidget
from nodewidget import NodeWidget
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
        self.spinBox.setMaximum(3)
        self.horizontalSlider = QSlider(self.mainWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 110, 131, 16))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(3)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.validatePushButton = QPushButton(self.mainWidget)
        self.validatePushButton.setObjectName(u"pushButton")
        self.validatePushButton.setGeometry(QRect(20, 140, 131, 24))
        self.label_2 = QLabel(self.mainWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 131, 21))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estas onfire", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad de ejecuci\u00f3n:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingles", None))

        #Iniciamos el widget contenedor del automata
        self.automataWidget = AutomataWidget(self.mainWidget)
        self.automataWidget.setGeometry(QRect(170, 50, 700, 450))

        self.automata = Automata()
        self.automataDrawer = AutomataDrawer(self.automata, self.automataWidget)
        self.automataDrawer.drawAutomata()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())