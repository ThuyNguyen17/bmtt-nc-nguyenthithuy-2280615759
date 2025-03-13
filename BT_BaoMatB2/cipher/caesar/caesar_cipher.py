from caesar.alphabet import ALPHABET
# ===========================
# Example: "HELLO"  key = 3
#         H  E L  L  O
#         7  4 11 11 14
# + key   10 7 14 14 17
# % 26    10 7 14 14 17
# KQ:     K  H O  O  R
# ===========================
class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, text:  str, key: int):
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text=[]
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text:  str, key: int):
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text=[]
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        return "".join(decrypted_text)