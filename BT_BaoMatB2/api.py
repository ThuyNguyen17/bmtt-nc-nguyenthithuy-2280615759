from flask import Flask, request, jsonify
# from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)
# caesar_cipher = CaesarCipher()
# @app.route("/api/caesar/encrypt", methods = ["POST"])
# def caesar_encypt():
#     data = request.json
#     plain_text = data['plain_text']
#     key = int(data['key'])
#     encypted_text = caesar_cipher.encrypt_text(plain_text,key)
#     return jsonify({'encrypt_message': encypted_text})

# @app.route("/api/caesar/decrypt", methods = ["POST"])
# def caesar_decypt():
#     data = request.json
#     cipher_text = data['cipher_text']
#     key = int(data['key'])
#     decypted_text = caesar_cipher.decrypt_text(cipher_text,key)
#     return jsonify({'decrypt_message': decypted_text})

vigenere_cipher = VigenereCipher()
@app.route("/api/vigenere/encrypt", methods = ["POST"])
def vigenere_encypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encypted_text = vigenere_cipher.vigenere_encrypt(plain_text,key)
    return jsonify({'encrypt_message': encypted_text})

@app.route("/api/vigenere/decrypt", methods = ["POST"])
def vigenere_decypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decypted_text = vigenere_cipher.vigenere_decrypt(cipher_text,key)
    return jsonify({'decrypt_message': decypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)