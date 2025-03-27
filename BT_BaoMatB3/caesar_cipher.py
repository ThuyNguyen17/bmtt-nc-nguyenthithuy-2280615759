import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.encryptButton.clicked.connect(self.call_api_encrypt)
        self.ui.DecryptButton.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plaintext.toPlainText(),  
            "key": self.ui.key.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json() 
            print("API Response:", data) 
            if response.status_code == 200:
                self.ui.ciphertext.setPlainText(data["encrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API:", response.text)

        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.ciphertext.toPlainText(),  # Sửa tên biến
            "key": self.ui.key.toPlainText()
        }

        try:
            response = requests.post(url, json=payload)
            data = response.json()
            print("API Response:", data) 
            if response.status_code == 200:
                self.ui.plaintext.setPlainText(data["decrypted_message"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API:", response.text)

        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
