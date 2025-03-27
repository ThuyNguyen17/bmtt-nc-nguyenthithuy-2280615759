import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Tạo đối tượng hash BLAKE2b
    blake2_hash.update(message)  # Cập nhật dữ liệu cần băm
    return blake2_hash.digest()  # Trả về kết quả dạng bytes

def main():
    text = input("Enter text string: ").encode('utf-8')
    hashed_text = blake2(text)

    print("Entered text string:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())  # Chuyển kết quả thành chuỗi hex

if __name__ == "__main__":
    main()
