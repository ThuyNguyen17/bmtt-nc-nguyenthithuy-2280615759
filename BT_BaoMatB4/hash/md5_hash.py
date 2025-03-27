import struct

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5(message):
    # Khởi tạo giá trị hash
    a, b, c, d = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Hằng số MD5 (T[i] = int(2^32 * abs(sin(i + 1))))
    T = [
        int(abs(2**32 * (abs(__import__('math').sin(i + 1))))) & 0xFFFFFFFF for i in range(64)
    ]

    # Shift values
    S = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
    ]

    # Bổ sung padding
    original_length = len(message) * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += struct.pack('<Q', original_length)

    # Xử lý từng khối 512-bit (64 byte)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        M = list(struct.unpack('<16I', chunk))

        A, B, C, D = a, b, c, d

        for j in range(64):
            if j < 16:
                F = (B & C) | (~B & D)
                g = j
            elif j < 32:
                F = (D & B) | (~D & C)
                g = (5 * j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                g = (3 * j + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * j) % 16

            temp = D
            D = C
            C = B
            B = (B + left_rotate(A + F + T[j] + M[g], S[j])) & 0xFFFFFFFF
            A = temp

        # Cộng dồn kết quả
        a = (a + A) & 0xFFFFFFFF
        b = (b + B) & 0xFFFFFFFF
        c = (c + C) & 0xFFFFFFFF
        d = (d + D) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Nhập chuỗi và tính MD5
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print(f"MD5 của '{input_string}' là: {md5_hash}")
