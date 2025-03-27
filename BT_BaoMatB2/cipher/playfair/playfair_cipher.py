# ===================================================================================
# Ma trận 5x5 chứa 25 chữ cái (gộp 'I' và 'J' thành một).
# Nếu cặp ký tự giống nhau, chèn thêm 'X'.
# Nếu hai chữ cùng hàng, lấy chữ bên phải.
# Nếu hai chữ cùng cột, lấy chữ bên dưới.
# Nếu hai chữ khác hàng, khác cột, lấy chữ đối diện theo hình chữ nhật.
#
# Example: plain_text = "HELLO"     key ="PLAYFAIR EXAMPLE"
# matrix={
#       P L A Y F  
#       I R B C D 
#       E G H K M  
#       N O Q S T  
#       U V W X Z }
# Cặp:      HE LL OX
# encrypt:  KG AA SV
# ===================================================================================
# M O N A R
# C H Y B D 
# E F G I K 
# L P Q S T
# U V W X Y 

# HELLO 
# HE LX LO 
# CF SU PM


class PlayFairCipher:
    def __init__(self):
        pass   

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")
        key = key.upper()
        key_set = set()
        matrix = []
        
        for letter in key:
            if letter not in key_set and letter.isalpha():
                key_set.add(letter)
                matrix.append(letter)
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # bảng chữ không có J
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
          # list comprehension: new_list = [expression for item in iterable if condition]. Tương đương
        # remaining_letters = []
        # for letter in alphabet:
        #     if letter not in key_set:
        #         remaining_letters.append(letter)
        matrix.extend(remaining_letters)
        # Cú pháp cắt (slice) a[start:end], nó sẽ lấy từ start đến end - 1, nghĩa là không bao gồm end
        # matrix[i:i+5] là cắt (slice) một đoạn con gồm 5 phần tử, bắt đầu từ vị trí i đến i+4.
        # range(0, len(matrix), 5) tạo ra một dãy số bắt đầu từ 0, tăng dần theo bước nhảy 5, và kết thúc trước len(matrix).
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
    
    def process_text(self, text):
        text = text.replace("J", "I").upper()
        processed_text = ""
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                processed_text += text[i] + "X"
                break
            if text[i] == text[i+1]:
                processed_text += text[i] + "X"
                i += 1
            else:
                processed_text += text[i] + text[i+1]
                i += 2
        return processed_text
    
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.process_text(plain_text)
        encrypted_text = ""
        
        for i in range(0, len(plain_text), 2):    
            pair = plain_text[i:i+2]    # Duyệt từng cặp 2 ký tự một trong plain_text
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]# chia %5 để nếu ở col 4 thì quay về 0
            elif col1 == col2:
                encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
            elif col1 == col2:
                decrypted_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        return decrypted_text.replace("X", "")