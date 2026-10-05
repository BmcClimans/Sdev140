import sys

from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox

from mcclimansBreeanna_dialogue import Ui_DialogBree

class DialogBree(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogBree()
        self.ui.setupUi(self)

        #Make buttons attributes
        self.ok_button = self.ui.ButtonBoxBree.button(QDialogButtonBox.StandardButton.Ok)
        self.ok_button.clicked.connect(self.on_ok_clicked)

    def on_ok_clicked(self):
        print(self.ui.LineEditName.text())
        self.ui.LineEditName.clear()
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DialogBree()
    dialog.exec()