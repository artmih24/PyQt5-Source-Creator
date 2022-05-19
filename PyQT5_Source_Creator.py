from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQT5_Source_Creator_window import Ui_MainWindow
from PyQT5_Source_Creator_about import about_window
import sys
import PyQT5_Source_creator_Icon as icon


class mywindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # настройка значка окна
        self.icon_data = icon.Get_icon(icon.icon_str)
        self.setWindowIcon(self.icon_data)
        # настройка свойств окна
        self.setGeometry(815, 400, 295, 314)
        self.setMinimumSize(295, 314)
        self.setStyleSheet('QMainWindow {background-color: white;}')
        self.ui.pushButton.setEnabled(False)
        self.ui.lineEdit.setFocus()
        # настройка полей ввода
        self.ui.lineEdit.setFixedWidth(self.width() - 19)
        self.ui.lineEdit_2.setFixedWidth(self.width() - 19)
        self.ui.lineEdit_3.setFixedWidth(self.width() - 19)
        self.ui.lineEdit_4.setFixedWidth(self.width() - 97)
        self.ui.lineEdit_5.setFixedWidth(self.width() - 97)
        self.resized.connect(self.FormResized)
        # инициализация других окон
        self.about_window = about_window()
        # добавление пунктов меню
        m = self.menuBar().addMenu("Меню")
        a = m.addAction("О программе")
        # подключение сигналов к элементам формы
        a.triggered.connect(self.aboutClicked)
        self.ui.pushButton.clicked.connect(self.CreatePyFileButtonClicked)
        self.ui.lineEdit.textChanged.connect(self.FormFilled)
        self.ui.lineEdit_2.textChanged.connect(self.FormFilled)
        self.ui.lineEdit_3.textChanged.connect(self.FormFilled)
        self.ui.lineEdit_4.textChanged.connect(self.FormFilled)
        self.ui.lineEdit_5.textChanged.connect(self.FormFilled)

    def CreatePyFileButtonClicked(self):
        q = QMessageBox()
        q.setWindowIcon(self.icon_data)
        ImportFileName = self.ui.lineEdit.text()
        ImportWindowName = self.ui.lineEdit_2.text()
        WindowClassName = self.ui.lineEdit_3.text()
        ShortAppName = 'app_' + self.ui.lineEdit_4.text()
        LongAppName = 'application_' + self.ui.lineEdit_5.text()
        try:
            SaveSourceFileName = QFileDialog.getSaveFileName(self, "Сохранить файл", '', "Файл исходного кода Python (*.py)")[0]
        except:
            QMessageBox.critical(q, "PyQT5 Source  Creator", f"Не выбран путь для сохранения файла.\nОперация прервана", QMessageBox.Ok)
        else:
            ShortSourceFileName = SaveSourceFileName.split('/')[-1]
            PyFileContent = f'''# auto-generated source-code file {ShortSourceFileName} with PyQT5 Source Creator
# PyQT5 Source Creator developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtWidgets
from {ImportFileName} import Ui_{ImportWindowName}
import sys


class {WindowClassName}(QtWidgets.QMainWindow):
    def __init__(self):
        super({WindowClassName}, self).__init__()
        self.ui = Ui_{ImportWindowName}()
        self.ui.setupUi(self)


if __name__ == '__main__':
    {ShortAppName} = QtWidgets.QApplication([])
    {LongAppName} = {WindowClassName}()
    {LongAppName}.show()
    
    sys.exit({ShortAppName}.exec())'''
            try:
                with open(SaveSourceFileName, "w") as PyFile:
                    PyFile.write(PyFileContent)
                PyFile.close()
            except:
                QMessageBox.critical(q, "PyQT5 Source  Creator", f"Возникла ошибка при записи файла {SaveSourceFileName}.\nОперация прервана", QMessageBox.Ok)
                PyFile.close()
            else:
                QMessageBox.information(q, "Pycture", f"Файл {SaveSourceFileName} успешно создан!", QMessageBox.Ok)

    def FormFilled(self):
        if self.ui.lineEdit.text() != '' \
                and self.ui.lineEdit_2.text() != '' \
                and self.ui.lineEdit_3.text() != '' \
                and self.ui.lineEdit_4.text() != '' \
                and self.ui.lineEdit_5.text() != '':
            self.ui.pushButton.setEnabled(True)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(mywindow, self).resizeEvent(event)

    def FormResized(self):
        w = self.width()
        self.ui.lineEdit.setFixedWidth(w - 19)
        self.ui.lineEdit_2.setFixedWidth(w - 19)
        self.ui.lineEdit_3.setFixedWidth(w - 19)
        self.ui.lineEdit_4.setFixedWidth(w - 97)
        self.ui.lineEdit_5.setFixedWidth(w - 97)

    def aboutClicked(self):
        self.about_window.show()

    def closeEvent(self, e) -> None:
        self.about_window.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())