from flask import Flask, render_template, request
from caesar import CaesarCipher
from vigenere import VigenereCipher
from playfair import PlayFairCipher
from RailFence import RailFenceCipher
from transposition import TranspositionCipher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=['POST'])  # Đúng đường dẫn
def caesar_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    Caesar = CaesarCipher()
    encrypt_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/decrypt", methods=['POST'])  # Đổi route decrypt
def caesar_decrypt():
    text = request.form['InputCipherText']
    key =int(request.form['InputKeyCipher'])
    Caesar = CaesarCipher()
    decrypt_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"

@app.route("/vigenerel")
def vigenerel():
    return render_template("vigenerel.html")


@app.route("/vigenerel/encrypt", methods=['POST']) 
def vigenerel_encrypt():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    vin = VigenereCipher()
    encrypt_text = vin.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/vigenerel/decrypt", methods=['POST']) 
def vigenerel_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyCipher']
    vin = VigenereCipher()
    decrypt_text = vin.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=['POST']) 
def playfair_encrypt():
    text = request.form["InputPlainText"]
    key = request.form["InputKeyPlain"]
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key) 
    encrypt_text = playfair.playfair_encrypt(text, matrix)  
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/playfair/decrypt", methods=['POST'])  
def playfair_decrypt():
    text = request.form['InputCipherText']
    key = request.form['InputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)  
    decrypt_text = playfair.playfair_decrypt(text, matrix) 
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"


@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=['POST']) 
def railfence_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    rail = RailFenceCipher()
    encrypt_text = rail.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/railfence/decrypt", methods=['POST']) 
def railfence_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyCipher'])
    rail = RailFenceCipher()
    decrypt_text = rail.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"



@app.route("/transposition")
def tranposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=['POST']) 
def tranposition_encrypt():
    text = request.form["InputPlainText"]
    key = int(request.form["InputKeyPlain"])
    tranposition = TranspositionCipher()
    encrypt_text =tranposition.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted_text: {encrypt_text}"

@app.route("/transposition/decrypt", methods=['POST']) 
def tranposition_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyCipher'])
    tranposition = TranspositionCipher()
    decrypt_text = tranposition.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypt_text: {decrypt_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

