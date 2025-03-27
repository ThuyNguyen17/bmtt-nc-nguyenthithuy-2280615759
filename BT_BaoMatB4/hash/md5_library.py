import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Nhập dữ liệu từ người dùng
input_string = input("Enter string to hash: ")

# Tính MD5
md5_hash = calculate_md5(input_string)

# In kết quả
print("The MD5 hash of string '{}' is: {}".format(input_string, md5_hash))
