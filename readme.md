# 🔗 Blockchain Simulation

## Overview
The **Blockchain Simulation** is a Python-based project developed to demonstrate the fundamentals of a blockchain. This project implements a simple blockchain with a Proof of Work mechanism, the ability to add blocks, Merkle root validation, and basic chain validation. It serves as an educational tool for understanding decentralized and immutable systems.

## ✨ Features

- **Proof of Work (PoW)**: Implements a mining process where a valid proof is found by solving a computational puzzle.
- **Blockchain Integrity Validation**: Ensures that any tampered block is detected, reinforcing the immutability of the chain.
- **Merkle Root Calculation**: Ensures transaction integrity by using a hierarchical hash structure.
- **Blockchain Simulation**: Supports multiple peers contributing to the chain with simulated mining.
- **Corruption Simulation**: Allows for testing the blockchain's response when a block is corrupted manually.

## 📦 Requirements

Ensure you have Python 3 installed.

## 🚀 Usage

### Running the Script

1. Clone or download the repository to your local machine.
2. Run the script from the command line to simulate a blockchain and observe its behavior:

```bash
python blockchain.py
```

You can also simulate corruption in the blockchain using the `-corrupt` argument, followed by the peer index, block index, and new proof:

```bash
python blockchain.py -corrupt <peer_index> <block_index> <new_proof>
```

Replace `<peer_index>` with the index of the peer (0, 1, 2...), `<block_index>` with the index of the block to corrupt, and `<new_proof>` with a new proof value.

### Example:

```bash
python blockchain.py -corrupt 0 2 9999
```

## 🖥️ Expected Output

When executed, the script will display the blockchain structure before and after potential corruption, as well as whether the blockchain is still valid.

### Sample Output:

```json
Blockchain before corruption:
[
    {
        "index": 1,
        "timestamp": "2025-03-19 09:59:39.462860",
        "proof": 1,
        "previous_hash": "0",
        "miner": "Genesis",
        "current_hash": "859f948f6a87fa683a5f3347b058a6217970465cb1a7926cdb5e1afd156ce1ff"
    },
    {
        "index": 2,
        "timestamp": "2025-03-19 09:59:41.103788",
        "proof": 632238,
        "previous_hash": "859f948f6a87fa683a5f3347b058a6217970465cb1a7926cdb5e1afd156ce1ff",
        "miner": "Peer A",
        "current_hash": "920e9dacd99126a3de7c2277566ee799005d54b3ede4921c7f94776a014f2fe9"
        "transactions": ["Genesis Block"],
        "merkle_root": "abcdef12345..."
    },
    {
        "index": 3,
        "timestamp": "2025-03-02 10:24:10.789123",
        "proof": 23456,
        "previous_hash": "abcdef12345...",
        "miner": "Peer A",
        "transactions": ["Alice pays Bob 5 BTC"],
        "merkle_root": "xyz12345..."
    }
]
Corrupting blockchain for Peer A at block 2.

Blockchain after corruption:
[
    {
        "index": 1,
        "timestamp": "2025-03-19 09:59:39.462860",
        "proof": 1,
        "previous_hash": "0",
        "miner": "Genesis",
        "current_hash": "859f948f6a87fa683a5f3347b058a6217970465cb1a7926cdb5e1afd156ce1ff"
    },
    {
        "index": 2,
        "timestamp": "2025-03-19 09:59:41.103788",
        "proof": 12345,
        "previous_hash": "859f948f6a87fa683a5f3347b058a6217970465cb1a7926cdb5e1afd156ce1ff",
        "miner": "Peer A",
        "current_hash": "03479147053e8f6192096c60632276fdc0b81168305e408891d0629dc40a36b5"
        "transactions": ["Genesis Block"],
        "merkle_root": "abcdef12345..."
    },
    {
        "index": 3,
        "timestamp": "2025-03-02 10:24:10.789123",
        "proof": 9999,
        "previous_hash": "abcdef12345...",
        "miner": "Peer A",
        "transactions": ["Tampered Transaction"],
        "merkle_root": "tampered12345..."
    }
]
Blockchain is invalid. Corruption detected at block(s): [2]
Blockchain valid: False
```

## ⚙️ Customization

- **Adjust Proof of Work Difficulty**: Modify the `difficulty` parameter in the `Blockchain` class to change the mining difficulty.
- **Add More Peers**: Expand the list of peers in the simulation by adding more entries to the `peers` list in the script.

## 🤝 Contributing

Contributions are welcome! If you'd like to improve or expand the project, feel free to fork the repository and submit a pull request with your changes.

## 💎 Contact

For any questions or suggestions, feel free to open an issue or contact via GitHub.

## 📚 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

