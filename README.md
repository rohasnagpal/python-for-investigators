# Python for Investigators 🕵️‍♂️🐍

A growing collection of Python scripts built for cryptocurrency and digital investigators.

📌 This repo currently contains the following scripts:

- **`bitcoin_balance.py`**  
  Check the balance of a single Bitcoin address.
  
- **`bitcoin_balance_multiple.py`**  
  Bulk balance checker for multiple Bitcoin addresses (useful for wallet cluster review).

- **`bitcoin_block.py`**  
  Fetch and inspect Bitcoin block-level data.
  
- **`bitcoin_inflow_multiple.py`**  
  Investigate inflows across multiple addresses to identify funding patterns.

- **`dictionary.py`**  
  An example of a dictionary.

- **`seed_generator.py`**  
  Generates random BIP-39 English wallet seed phrases in all standard lengths (12–24 words).

- **`wallet_generator.py`**  
  Derives the first wallet (index 0) from a BIP-39 seed phrase for multiple blockchains (Bitcoin, Litecoin, Dogecoin, BCH, Ethereum and EVM chains) and prints each chain’s address, private key, and derivation path.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/rohasnagpal/python-for-investigators.git
cd python-for-investigators
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Run a script
```bash
python bitcoin_balance.py
```
