# 🔗 Blockchain Simulation

## Overview
The **Blockchain Simulation**  is a Python-based project developed as part of a course. This project demonstrates the fundamentals of a blockchain, implementing a simple version with a Proof of Work mechanism, the ability to add blocks, and basic chain validation. It serves as an educational tool for understanding how decentralized and immutable systems work.

Key features of this simulation include:
- **Block creation** with a Proof of Work algorithm.
- **Blockchain validation** to ensure the integrity of the chain.
- **Optional corruption simulation** to observe how the system detects tampering.
- **Peer-based mining simulation**, where each peer can contribute blocks to the chain.


## ✨ Features

- **Proof of Work (PoW)**: Implements a mining process where a valid proof is found by solving a computational puzzle.
- **Blockchain Integrity Validation**: Ensures that any tampered block is detected, reinforcing the immutability of the chain.
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

You can also simulate corruption in the blockchain using the `-corrupt` argument, followed by the peer index and block index:

```bash
python blockchain.py -corrupt <peer_index> <block_index>
```

Replace `<peer_index>` with the index of the peer (0, 1, 2...) and `<block_index>` with the index of the block to corrupt.

### Example:

```bash
python blockchain.py -corrupt 0 2
```



## 🖥️ Expected Output

When executed, the script will display the blockchain structure before and after potential corruption, as well as whether the blockchain is still valid.

### Sample Output:

```
Blockchain before corruption:
[
    {
        "index": 1,
        "timestamp": "2025-03-02 10:23:42.456789",
        "proof": 12345,
        "previous_hash": "0",
        "miner": "Genesis"
    },
    {
        "index": 2,
        "timestamp": "2025-03-02 10:24:10.789123",
        "proof": 23456,
        "previous_hash": "abcdef12345...",
        "miner": "Peer A"
    }
]
Corrupting blockchain for Peer A at block 1.

Blockchain after corruption:
[
    {
        "index": 1,
        "timestamp": "2025-03-02 10:23:42.456789",
        "proof": 12345,
        "previous_hash": "0",
        "miner": "Genesis"
    },
    {
        "index": 2,
        "timestamp": "2025-03-02 10:24:10.789123",
        "proof": 12345,
        "previous_hash": "abcdef12345...",
        "miner": "Peer A"
    }
]

Blockchain valid: False
```


## ⚙️ Customization

- **Adjust Proof of Work Difficulty**: Modify the `proof_of_work` function to change the number of leading zeros required for a valid proof (currently set to 5).
- **Add More Peers**: Expand the list of peers in the simulation by adding more entries to the `peers` list in the script.


## 🤝 Contributing

Contributions are welcome! If you'd like to improve or expand the project, feel free to fork the repository and submit a pull request with your changes.


## 📧 Contact

For any questions or suggestions, feel free to open an issue or contact via GitHub.


## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
