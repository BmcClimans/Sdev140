import sys
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog

from fancy_drone_dogs_main_ui_pt3 import Ui_MainWindow
from dialog_pt3_ui import Ui_Dialog


#constants
SALES_TAX_RATE: float = 0.07
HOT_DOG_PRICE: float = 2.99
first_name: str = ""
last_name: str = ""
email: str = ""

customer_list: list = []
customer_list.append({"first_name": 'John', "last_name": 'Doe', "email": 'john.doe@example.com'})
customer_list.append({"first_name": 'Jane', "last_name": 'Smith', "email": 'jane.smith@example.com'})

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #setup buttons and connect them to their respective functions
        self.customer_list = self.ui.ListWidgetCustomerList
        self.first_name = self.ui.LineEditFirstName
        self.last_name = self.ui.LineEditLastName
        self.email = self.ui.LineEditEmail

        self.add_customer_button = self.ui.PushButtonAddCustomer
        self.add_customer_button.clicked.connect(self.add_customer_on_button_clicked)
        self.select_customer_button = self.ui.PushButtonSelectCustomer
        self.select_customer_button.clicked.connect(self.select_customer_on_button_clicked)
        self.load_customer_list()

    def add_customer_on_button_clicked(self):
        global customer_list

        #get customer information 
        first_name = self.first_name.text().strip().title()
        last_name = self.last_name.text().strip().title()
        email = self.email.text().strip()

        #validate that all fields are filled in before adding the customer
        if first_name == "" or last_name == "" or email == "":
            QMessageBox.warning(self, "Input Error", "Please fill in all fields before adding a customer.")
            return

        #create a new customer dictionary and add it to the customer list
        new_customer = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }

        customer_list.append(new_customer)
        self.load_customer_list()

    def select_customer_on_button_clicked(self):
        selected_items = self.customer_list.selectedItems()
        if not selected_items:
            return

        selected_text = selected_items[0].text()
        for customer in customer_list:
            if f"{customer['first_name']} {customer['last_name']} - {customer['email']}" == selected_text:
                global first_name, last_name, email
                first_name = customer['first_name']
                last_name = customer['last_name']
                email = customer['email']
                self.accept()
                break

    def load_customer_list(self):
        self.customer_list.clear()
        for customer in customer_list:
            self.customer_list.addItem(f"{customer['first_name']} {customer['last_name']} - {customer['email']}")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the folder containing this Python file
        #using these because the images kept not showing up and i nneeded a fix for that
        BASE_DIR = Path(__file__).resolve().parent

        # Load DroneDogs logo
        self.ui.LabelLogo.setPixmap(
            QPixmap(str(BASE_DIR / "DroneDogsLogo.png"))
        )

        # Load DroneDogs title image
        self.ui.LabelTitle.setPixmap(
            QPixmap(str(BASE_DIR / "dronedogs_order_form_title_text.png"))
        )

        #button setup
        self.calc_button = self.ui.PushButtonCalcOrder
        self.submit_order_button = self.ui.PushButtonSubmitOrder
        self.exit_button = self.ui.PushButtonExit
        self.customer_dialog_button = self.ui.PushButtonGetCustInfo
        self.clear_form_button = self.ui.PushButtonClearForm
        self.give_permission_button = self.ui.CheckBoxPermission

        self.calc_button.clicked.connect(self.on_calc_button_clicked)
        self.submit_order_button.clicked.connect(self.on_submit_order_button_clicked)
        self.exit_button.clicked.connect(self.on_exit_button_clicked)
        self.customer_dialog_button.clicked.connect(self.on_customer_dialog_button_clicked)
        self.clear_form_button.clicked.connect(self.on_clear_form_button_clicked)
        self.give_permission_button.clicked.connect(self.on_permission_checkbox_clicked)

    def on_permission_checkbox_clicked(self):
        print("Permission granted")

    def on_customer_dialog_button_clicked(self):
        dialog = MyDialog()
        ret_val: int = dialog.exec()
        if ret_val == QDialog.Accepted:
            self.ui.LineEditFirstName.setText(first_name)
            self.ui.LineEditLastName.setText(last_name)
            self.ui.LineEditEmail.setText(email)
        
    def on_clear_form_button_clicked(self):
        #clear all the spin boxes and line edits in the form
        self.ui.SpinBoxBeefDogs.setValue(0)
        self.ui.SpinBoxPorkDogs.setValue(0)
        self.ui.SpinBoxTurkeyDogs.setValue(0)
        self.ui.LineEditSubtotal.clear()
        self.ui.LineEditSalesTax.clear()
        self.ui.LineEditTotal.clear()
        self.ui.LineEditFirstName.clear()
        self.ui.LineEditLastName.clear()
        self.ui.LineEditEmail.clear()

    def on_calc_button_clicked(self):
        #get the number of hot dogs from the spin boxes, using the value() method to retrieve the integer value
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
        self.ui.LineEditTotal.setText(f"${total_cost:.2f}")

    def on_submit_order_button_clicked(self):
        #validate that at least one hot dog has been ordered before submitting the order
        num_beef_dogs = self.ui.SpinBoxBeefDogs.value()
        num_pork_dogs = self.ui.SpinBoxPorkDogs.value()
        num_turkey_dogs = self.ui.SpinBoxTurkeyDogs.value()

        total_hot_dogs = num_beef_dogs + num_pork_dogs + num_turkey_dogs

        if total_hot_dogs == 0:
            QMessageBox.warning(self, "Input Error", "Please order at least one hot dog before submitting.")
            return

        #validate location permission checkbox is checked before submitting the order
        if not self.give_permission_button.isChecked():
            QMessageBox.warning(self, "Permission Error", "Please grant location permission before submitting your order.")
            return
        
        QMessageBox.information(self, "Order Submitted", "Thank you for ordering your meal from DroneDogs!")

    def on_exit_button_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())