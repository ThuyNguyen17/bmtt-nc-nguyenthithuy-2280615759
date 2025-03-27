import base64

def main():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            encoded_string = file.read().strip()

        if not encoded_string:
            print("Error: File is empty.")
            return

        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")

        print("String after decoding:", decoded_string)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
