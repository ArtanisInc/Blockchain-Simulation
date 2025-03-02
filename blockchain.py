import datetime
import hashlib
import json
import argparse

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0', miner='Genesis')

    def create_block(self, proof, previous_hash, miner):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'miner': miner
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        proof = 1
        while hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()[:5] != '00000':
            proof += 1
        return proof

    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            prev, curr = self.chain[i-1], self.chain[i]
            if curr['previous_hash'] != self.hash(prev):
                return False
            if hashlib.sha256(str(curr['proof']**2 - prev['proof']**2).encode()).hexdigest()[:5] != '00000':
                return False
        return True

    def corrupt_chain(self, block_index, new_proof):
        if 0 <= block_index < len(self.chain):
            self.chain[block_index]['proof'] = new_proof

def main():
    parser = argparse.ArgumentParser(description="Blockchain simulation with optional corruption.")
    parser.add_argument('-corrupt', nargs=2, type=int, metavar=('PEER_INDEX', 'BLOCK_INDEX'), help="Corrupt the blockchain for a specific peer and block.")
    args = parser.parse_args()

    blockchain = Blockchain()
    peers = ["Peer A", "Peer B", "Peer C"]

    for _ in range(5):
        for peer in peers:
            prev_block = blockchain.get_previous_block()
            proof = blockchain.proof_of_work(prev_block['proof'])
            blockchain.create_block(proof, blockchain.hash(prev_block), peer)

    print("Blockchain before corruption:")
    print(json.dumps(blockchain.chain, indent=4))

    if args.corrupt:
        peer_index, block_index = args.corrupt
        if 0 <= peer_index < len(peers):
            print(f"Corrupting blockchain for {peers[peer_index]} at block {block_index}.")
            blockchain.corrupt_chain(block_index, 12345)
        else:
            print("Invalid peer index.")

        print("\nBlockchain after corruption:")
        print(json.dumps(blockchain.chain, indent=4))

    print("Blockchain valid:", blockchain.is_chain_valid())

if __name__ == "__main__":
    main()
