from PySide6.QtWidgets import QDialog
from searche_dialog import Ui_Dialog


class MyDialogCity(QDialog):
    def __init__(self):
        super(MyDialogCity, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_add.pressed.connect(self.add_favorite)
        self.ui.pushButton_delete.pressed.connect(self.remove_favorite)

    def add_favorite(self):
        self.ui.comboBox.addItem(self.ui.lineEdit.text())

    def remove_favorite(self):
        self.ui.comboBox.removeItem(0)
