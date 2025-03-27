# ===========================
# Example: "HELLO"  num_rails = 3
# di chuyển lên xuống theo mô hình zigzag
# H    O   L
#   E L W R D
#    L   O  
# Cipher Text: HOLELWRDLO
# ===========================
class RailFenceCipher:
    def __init__(self):
        pass
    def rail_fence_encrypt(self,plain_text,num_rails):
        rails =[[] for _ in range(num_rails)] # rails = [[], [], []] 
        # _ là một quy ước đặt tên biến trong Python, thường được dùng khi biến không quan trọng và không cần sử dụng
        rails_index = 0
        direction = 1   # Biến để kiểm soát hướng di
        for char in plain_text:
            rails[rails_index].append(char)
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails -1:
                direction = -1
            rails_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails) # Lặp từng hàng ->  Ghép ký tự trong mỗi hàng thành chuỗi -> Ghép toàn bộ thành một chuỗi duy nhất
        return cipher_text
    # Cipher Text: HOLELWRDLO
    def rail_fence_decrypt(self,cipher_text,num_rails):
        rails_lengths = [0]*num_rails  # [0, 0, 0] một danh sách chứa một phần tử 0
        rails_index = 0
        direction = 1
        #  Xác định số lượng ký tự trên mỗi hàng
        for _ in range(len(cipher_text)):
            rails_lengths[rails_index]+=1
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails -1:
                direction = -1
            rails_index += direction
        # rails_lengths = [3,5,2]
        # Chia cipher_text thành các hàng
        rails=[]
        start = 0
        for length in rails_lengths:
            rails.append(cipher_text[start:start+length])
            start+=length

        # Lặp 1 (length = 3)
        # rails.append(cipher_text[0:3]) → Lấy "HOL"
        # rails = ["HOL"]
        # start = start + 3 = 3

        # Lặp 2 (length = 5)
        # rails.append(cipher_text[3:8]) → Lấy "ELWRD"
        # rails = ["HOL", "ELWRD"]
        # start = start + 5 = 8

        # Lặp 3 (length = 2)
        # rails.append(cipher_text[8:10]) → Lấy "LO"
        # rails = ["HOL", "ELWRD","LO"]
        # start = start + 2 = 10

        plain_text =""
        rails_index=0
        direction=1
        for _ in range (len(cipher_text)):
            plain_text += rails[rails_index][0] # Lấy ký tự đầu tiên của hàng hiện tại
            rails[rails_index] = rails[rails_index][1:] # Phần rails[1][1:] lấy danh sách rails[1] nhưng loại bỏ phần tử đầu tiên, nghĩa là lấy từ index 1 trở đi.
            if rails_index == 0:
                direction = 1
            elif rails_index ==num_rails -1:
                direction = -1
            rails_index += direction
        return plain_text