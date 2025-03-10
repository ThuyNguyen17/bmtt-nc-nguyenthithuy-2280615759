  
# ===========================
# Example: "plain_text" : "HUTECH","key": "ABC"
# mã hóa và giải mã văn bản bằng cách sử dụng một khóa (key) lặp lại, dịch chuyển các ký tự của văn bản theo giá trị của các ký tự trong khóa
# H => key_shift=0, encrypted_text= H ((72-65+0)%26+65=72)
# U => key_shift=1, encrypted_text= HV ((85-65+1)%26+65=86)
# Cipher Text: HVVEDJ
# ===========================

class VigenereCipher:
    def __init__(self):
        pass
    def vigenere_encrypt(self,plain_text,key):
        encrypted_text =""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) -ord('A')+key_shift)%26+ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a')+key_shift)%26+ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt (self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift)%26+ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift)%26+ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text