import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_gen_keys)
        self.ui.pushButton_2.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_3.clicked.connect(self.call_api_decrypt)
        self.ui.pushButton_4.clicked.connect(self.call_api_sign)
        self.ui.pushButton_5.clicked.connect(self.call_api_verify)

    def show_error(self, error_msg):
        """ Hiển thị lỗi trong hộp thoại QMessageBox """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(f"Error: {error_msg}")
        msg.exec_()
        print(f"Error: {error_msg}")

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                QMessageBox.information(self, "Success", data["message"])
            else:
                self.show_error("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_error(str(e))

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {"message": self.ui.txt_plain_text.toPlainText(), "key_type": "public"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
                QMessageBox.information(self, "Success", "Encrypted successfully!!")
            else:
                self.show_error("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_error(str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {"cipher": self.ui.txt_cipher_text.toPlainText(), "key_type": "private"}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                QMessageBox.information(self, "Success", "Decrypted successfully!!")
            else:
                self.show_error("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_error(str(e))

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {"message": self.ui.txt_info.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data["signature"])
                QMessageBox.information(self, "Success", "Signed successfully!!")
            else:
                self.show_error("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_error(str(e))

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {"message": self.ui.txt_info.toPlainText(), "signature": self.ui.txt_sign.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg_text = "Verified successfully!!" if data["is_verified"] else "Verified failed!!"
                QMessageBox.information(self, "Verification", msg_text)
            else:
                self.show_error("Error while calling API")
        except requests.exceptions.RequestException as e:
            self.show_error(str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
