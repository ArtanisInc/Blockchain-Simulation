import datetime
import hashlib
import json
import argparse

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty
        self.create_block(proof=1, previous_hash='0', miner='Genesis', transactions=["Genesis Block"])

    def create_block(self, proof, previous_hash, miner, transactions):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'miner': miner,
            'transactions': transactions,
            'merkle_root': self.merkle_root(transactions)
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        proof = 1
        while hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()[:self.difficulty] != '0' * self.difficulty:
            proof += 1
        return proof

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    @staticmethod
    def merkle_root(transactions):
        if not transactions:
            return ""
        tx_hashes = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])
            tx_hashes = [hashlib.sha256((tx_hashes[i] + tx_hashes[i + 1]).encode()).hexdigest()
                         for i in range(0, len(tx_hashes), 2)]
        return tx_hashes[0]

    def is_chain_valid(self):
        invalid_blocks = []
        for i in range(1, len(self.chain)):
            prev, curr = self.chain[i-1], self.chain[i]
            if curr['previous_hash'] != self.hash(prev):
                invalid_blocks.append(i)
            if hashlib.sha256(str(curr['proof']**2 - prev['proof']**2).encode()).hexdigest()[:self.difficulty] != '0' * self.difficulty:
                invalid_blocks.append(i)
            if curr['merkle_root'] != self.merkle_root(curr['transactions']):
                invalid_blocks.append(i)
        
        if invalid_blocks:
            print("Blockchain is invalid. Corruption detected at block(s):", invalid_blocks)
            return False
        
        return True

    def corrupt_chain(self, block_index, new_proof, new_transactions):
        if 0 <= block_index < len(self.chain):
            self.chain[block_index]['proof'] = new_proof
            self.chain[block_index]['transactions'] = new_transactions
            self.chain[block_index]['merkle_root'] = self.merkle_root(new_transactions)

    def get_chain_with_current_hash(self):
        """Retourne une copie de la chaîne avec le hash actuel de chaque bloc."""
        chain_with_hash = []
        for block in self.chain:
            block_copy = block.copy()
            block_copy['current_hash'] = self.hash(block)
            chain_with_hash.append(block_copy)
        return chain_with_hash

def main():
    parser = argparse.ArgumentParser(description="Blockchain simulation with optional corruption.")
    parser.add_argument('-corrupt', nargs=3, metavar=('PEER_INDEX', 'BLOCK_INDEX', 'NEW_PROOF'), help="Corrupt the blockchain for a specific peer and block.")
    args = parser.parse_args()

    blockchain = Blockchain(difficulty=3)
    peers = ["Peer A", "Peer B", "Peer C"]
    transactions = [
        ["Alice pays Bob 5 BTC"],
        ["Bob pays Charlie 2 BTC"],
        ["Charlie pays Dave 1 BTC"],
        ["Dave pays Eve 0.5 BTC"],
        ["Eve pays Frank 0.3 BTC"]
    ]

    for _ in range(5):
        for peer in peers:
            prev_block = blockchain.get_previous_block()
            proof = blockchain.proof_of_work(prev_block['proof'])
            blockchain.create_block(proof, blockchain.hash(prev_block), peer, transactions[_ % len(transactions)])

    print("Blockchain before corruption:")
    print(json.dumps(blockchain.get_chain_with_current_hash(), indent=4))

    if args.corrupt:
        peer_index, block_index, new_proof = map(int, args.corrupt)
        if 0 <= peer_index < len(peers):
            print(f"Corrupting blockchain for {peers[peer_index]} at block {block_index}.")
            blockchain.corrupt_chain(block_index, new_proof, ["Tampered Transaction"])
        else:
            print("Invalid peer index.")

        print("\nBlockchain after corruption:")
        print(json.dumps(blockchain.get_chain_with_current_hash(), indent=4))

    print("Blockchain valid:", blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
