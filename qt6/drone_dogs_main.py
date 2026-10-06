import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from drone_dogs_main_ui import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__TAX_RATE = 0.07

        #button setup
        self.calc_button = self.ui.PushButtonCalcOrder
        self.submit_order_button = self.ui.PushButtonSubmitOrder
        self.exit_button = self.ui.PushButtonExit

        self.calc_button.clicked.connect(self.on_calcc_button_clicked)
        self.submit_order_button.clicked.connect(self.on_submit_order_button_clicked)
        self.exit_button.clicked.connect(self.on_exit_button_clicked)

    def on_calcc_button_clicked(self):
        self.ui.LineEditSalesTax.setText(""
    def on_submit_order_button_clicked(self):
        pass

    def on_exit_button_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())