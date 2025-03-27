     print("✅ Hàm call_api_verify được gọi")
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        print(f"📩 Dữ liệu gửi đi: {payload}")

        try:
            response = requests.post(url, json=payload)
            print(f"📥 Nhận response: {response.status_code}, {response.text}")

            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    QMessageBox.information(self, "Thông báo", "Verified Successfully")
                else:
                    QMessageBox.warning(self, "Thông báo", "Verified Fail")
            else:
                print("❌ Lỗi: API không trả về thành công")
        except requests.exceptions.RequestException as e:
            print(f"❌ Request Exception: {str(e)}")