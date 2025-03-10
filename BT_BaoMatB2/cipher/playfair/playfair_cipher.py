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


class PlayFairCipher:
    def __init__(self):
        pass   

    def create_playfair_matrix(self, key):
        key = key.replace("J","I")
        key = key.upper()
        key_set = set(key) # loại bỏ chữ cái trùng lặp
        alphabet= "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # bảng chữ không có J
        # list comprehension: new_list = [expression for item in iterable if condition]. Tương đương
        # remaining_letters = []
        # for letter in alphabet:
        #     if letter not in key_set:
        #         remaining_letters.append(letter)
        remaining_letters=[
            letter for letter in alphabet if letter not in key_set
        ]
        matrix = list(key)
        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix)== 25:
                break
        # list comprehension dùng để chia danh sách matrix thành một ma trận 5x5
        # Tương đương:
        # playfair_matrix = []
        # for i in range(0, len(matrix), 5):
        #     playfair_matrix.append(matrix[i:i+5])

        # Cú pháp cắt (slice) a[start:end], nó sẽ lấy từ start đến end - 1, nghĩa là không bao gồm end
        # matrix[i:i+5] là cắt (slice) một đoạn con gồm 5 phần tử, bắt đầu từ vị trí i đến i+4.
        # range(0, len(matrix), 5) tạo ra một dãy số bắt đầu từ 0, tăng dần theo bước nhảy 5, và kết thúc trước len(matrix).
        playfair_matrix = [matrix[i:i+5] for i in range (0,len(matrix),5)]
        return playfair_matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):              # len(matrix) lấy số hàng của ma trận
            for col in range(len(matrix[row])):     # len(matrix[row]): số cột của một hàng trong ma trận.
                if matrix[row][col] == letter:
                    return row,col
    
    def playfair_encrypt (self,plain_text,matrix):
        plain_text = plain_text.replace("J","I")
        plain_text = plain_text.upper()
        encrypted_text=""
        for i in range(0,len(plain_text),2):    
            pair = plain_text[i:i+2]    # Duyệt từng cặp 2 ký tự một trong plain_text
            if len(pair) == 1:
                pair += 'X'     # Nếu còn lại 1 ký tự cuối cùng, thêm X để đảm bảo có đủ cặp
            row1, col1 = self.find_letter_coords(matrix,pair[0])
            row2, col2 = self.find_letter_coords(matrix,pair[1])
            if row1 == row2:
                encrypted_text+= matrix[row1][(col1+1)%5]+ matrix[row2][(col2+1)%5] # chia %5 để nếu ở col 4 thì quay về 0
            elif col1 == col2:
                encrypted_text+= matrix[(row1+1)%5][col1]+ matrix[(row2+1)%5][col2]
            else:
                encrypted_text += matrix[row1][col2]+ matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self,cipher_text,matrix):
        cipher_text = cipher_text.upper()
        decrypted_text  =""

        for i in range(0,len(cipher_text),2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix,pair[0])
            row2, col2 = self.find_letter_coords(matrix,pair[1])
            if row1 == row2:
                decrypted_text+= matrix[row1][(col1-1)%5]+ matrix[row2][(col2-1)%5]
            elif col1 == col2:
                decrypted_text+= matrix[(row1-1)%5][col1]+ matrix[(row2-1)%5][col2]
            else:
                decrypted_text += matrix[row1][col2]+ matrix[row2][col1]
        banro =""
        for i in range (0,len(decrypted_text)-2,2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro+= decrypted_text[i]
            else:
                banro +=decrypted_text[i]+""+decrypted_text[i+1]
        if decrypted_text[-1]=="X":
            banro += decrypted_text[-2]
        else:
            banro+=decrypted_text[-2]
            banro+=decrypted_text[-1]
        return banro

