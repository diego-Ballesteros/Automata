from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 140, 131, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 131, 21))
        self.openGLWidget = QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(170, 50, 711, 611))
        self.textEdit = QTextEdit(self.centralwidget)
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
        MainWindow.setCentralWidget(self.centralwidget)
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
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionEspa_ol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.actionIngles.setText(QCoreApplication.translate("MainWindow", u"Ingles", None))
        self.actionAdicionar_Idioma.setText(QCoreApplication.translate("MainWindow", u"Adicionar Idioma", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">Palabra:</span></p></body></html>", None))
        self.spinBox.setPrefix("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estas onfire", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad de ejecuci\u00f3n:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ingles", None))

        self.menuIdioma.setTitle(QCoreApplication.translate("MainWindow", u"Idioma", None))
    # retranslateUi