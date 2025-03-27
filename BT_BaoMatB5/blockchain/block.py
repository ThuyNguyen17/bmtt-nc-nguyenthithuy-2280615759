import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        """Khởi tạo một khối trong blockchain"""
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()  # Tạo hash cho block ngay khi khởi tạo

    def calculate_hash(self):
        """Tính toán hash của block dựa trên dữ liệu bên trong"""
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()
