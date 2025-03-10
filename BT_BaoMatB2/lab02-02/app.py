from flask import Flask, render_template, request
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cipher.caesar import CaesarCipher

app = Flask(__name__)  # Đổi "__name__" thành __name__

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/Lab02/encrypt", methods=['POST'])  # Đúng đường dẫn
def caesar_encrypt():
    text = request.form.get("InputPlainText", "")
    key = request.form.get("InputKeyPlain", 0, type=int)  
    Caesar = CaesarCipher()
    encrypt_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/Lab02/decrypt", methods=['POST'])  # Đổi route decrypt
def caesar_decrypt():
    text = request.form.get('InputCipherText', "")
    key = request.form.get('InputKeyCipher', 0, type=int)  
    Caesar = CaesarCipher()
    decrypt_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

