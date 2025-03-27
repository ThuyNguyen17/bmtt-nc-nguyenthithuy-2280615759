import base64

def main():
    input_string = input("Enter information to be encrypted: ")

    # Mã hóa Base64
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")

    # Ghi vào file
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(encoded_string)

    print("Encoded and written to data.txt file")
    print("Encoded string:", encoded_string)

if __name__ == "__main__":
    main()
