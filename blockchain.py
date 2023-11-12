import hashlib
import time
import matplotlib.pyplot as plt
import random

class Transaction:
    def __init__(self, donor, recipient, amount):
        self.donor = donor
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.transactions) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Simulation
if __name__ == "__main__":
    blockchain = Blockchain()

    # Simulate transactions
    orphanages = ["Orphanage A", "Orphanage B", "Orphanage C", "Orphanage D"]
    donors = ["Donor 1", "Donor 2", "Donor 3", "Donor 4"]
    transactions = []

    for _ in range(20):
        donor = random.choice(donors)
        recipient = random.choice(orphanages)
        amount = random.randint(50, 200)
        tx = Transaction(donor, recipient, amount)
        transactions.append(tx)

    # Create blocks and add transactions
    for tx in transactions:
        new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, [tx])
        blockchain.add_block(new_block)

    # Analyze transactions to calculate total donations per orphanage
    donations_per_orphanage = {}
    for block in blockchain.chain:
        for tx in block.transactions:
            if tx.recipient not in donations_per_orphanage:
                donations_per_orphanage[tx.recipient] = []
            donations_per_orphanage[tx.recipient].append(tx.amount)

    # Calculate average donations per orphanage
    average_donations = {orphanage: sum(donations) / len(donations) for orphanage, donations in donations_per_orphanage.items()}

    # Create a bar chart for average donations
    plt.figure(figsize=(10, 6))
    plt.bar(average_donations.keys(), average_donations.values(), color='skyblue')
    plt.xlabel("Orphanage")
    plt.ylabel("Average Donations")
    plt.title("Average Rice Donations Received by Orphanages")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Create a pie chart for total donations distribution
    total_donations = [sum(donations) for donations in donations_per_orphanage.values()]
    plt.figure(figsize=(8, 8))
    plt.pie(total_donations, labels=donations_per_orphanage.keys(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Total Rice Donations Distribution among Orphanages")
    plt.axis('equal')
    plt.tight_layout()

    plt.show()
