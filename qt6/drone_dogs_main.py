import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
)

from drone_dogs_main_ui import Ui_MainWindow


#constants
SALES_TAX_RATE: float = 0.07
HOT_DOG_PRICE: float = 2.99
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #button setup
        self.calc_button = self.ui.PushButtonCalcOrder
        self.submit_order_button = self.ui.PushButtonSubmitOrder
        self.exit_button = self.ui.PushButtonExit

        self.calc_button.clicked.connect(self.on_calc_button_clicked)
        self.submit_order_button.clicked.connect(self.on_submit_order_button_clicked)
        self.exit_button.clicked.connect(self.on_exit_button_clicked)

    def on_calc_button_clicked(self):
        #get the number of hot dogs from the spin boxes
        num_beef_dogs = self.ui.SpinBoxBeefDogs.value()
        num_pork_dogs = self.ui.SpinBoxPorkDogs.value()
        num_turkey_dogs = self.ui.SpinBoxTurkeyDogs.value()

        #calculate the total number of hot dogs
        total_hot_dogs = num_beef_dogs + num_pork_dogs + num_turkey_dogs

        #validate the input
        if total_hot_dogs == 0:
            QMessageBox.warning(self, "Input Error", "Please order at least one hot dog.")
            return

        #calculate the subtotal, sales tax, and total cost
        order_subtotal: float = total_hot_dogs * HOT_DOG_PRICE
        sales_tax: float = order_subtotal * SALES_TAX_RATE
        total_cost: float = order_subtotal + sales_tax

        #display the results
        self.ui.LineEditSubtotal.setText(f"${order_subtotal:.2f}")
        self.ui.LineEditSalesTax.setText(f"${sales_tax:.2f}")
        self.ui.LineEditTotalCost.setText(f"${total_cost:.2f}")

    def on_submit_order_button_clicked(self):
        QMessageBox.information(self, "Order Submitted", "Thank you for ordering your meal from DroneDogs!")

    def on_exit_button_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())