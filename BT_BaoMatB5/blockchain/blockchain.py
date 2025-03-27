import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=1, previous_hash='0')  # Tạo block đầu tiên (genesis block)

    def create_block(self, proof, previous_hash):
        """ Tạo một block mới và thêm vào blockchain """
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []  # Reset danh sách giao dịch
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """ Lấy block cuối cùng trong chuỗi """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """ Tìm số proof hợp lệ bằng thuật toán PoW """
        new_proof = 1
        check_proof = False

        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Điều kiện PoW: hash bắt đầu bằng '0000'
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def add_transaction(self, sender, receiver, amount):
        """ Thêm giao dịch vào danh sách chờ xác nhận """
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        return self.get_previous_block().index + 1  # Trả về index của block sẽ chứa giao dịch này

    def is_chain_valid(self, chain):
        """ Kiểm tra tính hợp lệ của blockchain """
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            # Kiểm tra hash của block hiện tại có khớp với previous_hash không
            if block.previous_hash != previous_block.hash:
                return False

            # Kiểm tra điều kiện PoW
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] != '0000':  # Nếu hash không bắt đầu bằng '0000', blockchain không hợp lệ
                return False

            previous_block = block
            block_index += 1

        return True
