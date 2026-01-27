"""
Wallet Generator from Seed Phrase

Derives exactly ONE wallet (index 0) per supported blockchain
and displays it directly in the terminal.
"""

from mnemonic import Mnemonic
from bip32 import BIP32
from eth_keys import keys
import hashlib
import base58


# -------------------------------------------------------------------
# Chain configurations
# -------------------------------------------------------------------
CHAIN_CONFIG = {
    'bitcoin': {
        'coin_type': 0,
        'bip': 84,
        'prefix': 'bc1',
        'name': 'Bitcoin (BIP-84 Native SegWit)'
    },
    'litecoin': {
        'coin_type': 2,
        'bip': 84,
        'prefix': 'ltc1',
        'name': 'Litecoin (BIP-84 Native SegWit)'
    },
    'dogecoin': {
        'coin_type': 3,
        'bip': 44,
        'prefix': 'D',
        'name': 'Dogecoin (BIP-44)'
    },
    'bitcoin_cash': {
        'coin_type': 145,
        'bip': 44,
        'prefix': 'bitcoincash:q',
        'name': 'Bitcoin Cash (BIP-44)'
    },
    'ethereum': {
        'coin_type': 60,
        'bip': 44,
        'prefix': '0x',
        'name': 'Ethereum (BIP-44)'
    },
    'polygon': {
        'coin_type': 60,
        'bip': 44,
        'prefix': '0x',
        'name': 'Polygon (ETH derivation)'
    },
    'bnb': {
        'coin_type': 60,
        'bip': 44,
        'prefix': '0x',
        'name': 'BNB Chain (ETH derivation)'
    },
    'avalanche': {
        'coin_type': 60,
        'bip': 44,
        'prefix': '0x',
        'name': 'Avalanche C-Chain (ETH derivation)'
    }
}


# -------------------------------------------------------------------
# UTXO wallet derivation (BTC, LTC, DOGE, BCH)
# -------------------------------------------------------------------
def derive_utxo_wallet(seed: bytes, config: dict) -> dict:
    bip32 = BIP32.from_seed(seed)
    coin_type = config['coin_type']
    bip = config['bip']
    prefix = config['prefix']

    path = f"m/{bip}'/{coin_type}'/0'/0/0"
    private_key = bip32.get_privkey_from_path(path)
    public_key = bip32.get_pubkey_from_path(path)

    pubkey_hash = hashlib.new(
        'ripemd160',
        hashlib.sha256(public_key).digest()
    ).digest()

    if prefix.startswith(('bc1', 'ltc1')):
        address = f"{prefix}q{pubkey_hash.hex()[:40]}"
    else:
        if prefix == 'D':
            versioned = b'\x1e' + pubkey_hash
        elif prefix.startswith('bitcoincash'):
            address = f"{prefix}{pubkey_hash.hex()[:40]}"
            return {
                'address': address,
                'private_key': private_key.hex(),
                'derivation_path': path
            }
        else:
            versioned = b'\x00' + pubkey_hash

        checksum = hashlib.sha256(
            hashlib.sha256(versioned).digest()
        ).digest()[:4]

        address = base58.b58encode(versioned + checksum).decode()

    return {
        'address': address,
        'private_key': private_key.hex(),
        'derivation_path': path
    }


# -------------------------------------------------------------------
# Ethereum / EVM wallet derivation
# -------------------------------------------------------------------
def derive_evm_wallet(seed: bytes, config: dict) -> dict:
    bip32 = BIP32.from_seed(seed)
    coin_type = config['coin_type']

    path = f"m/44'/{coin_type}'/0'/0/0"
    private_key = bip32.get_privkey_from_path(path)

    eth_private_key = keys.PrivateKey(private_key)
    address = eth_private_key.public_key.to_checksum_address()

    return {
        'address': address,
        'private_key': private_key.hex(),
        'derivation_path': path
    }


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main():
    print("\n" + "=" * 80)
    print("MULTI-CHAIN WALLET GENERATOR (1 WALLET PER CHAIN)")
    print("=" * 80 + "\n")

    print("Supported chains:")
    for cfg in CHAIN_CONFIG.values():
        print(f" - {cfg['name']}")
    print()

    seed_phrase = input("Enter seed phrase: ").strip()

    mnemo = Mnemonic("english")
    if not mnemo.check(seed_phrase):
        print("\n❌ Invalid seed phrase\n")
        return

    seed = mnemo.to_seed(seed_phrase)

    print("\n" + "=" * 80)
    print("DERIVED WALLETS")
    print("=" * 80 + "\n")

    for chain_key, config in CHAIN_CONFIG.items():
        if chain_key in ['bitcoin', 'litecoin', 'dogecoin', 'bitcoin_cash']:
            wallet = derive_utxo_wallet(seed, config)
        else:
            wallet = derive_evm_wallet(seed, config)

        print(config['name'])
        print("-" * len(config['name']))
        print(f"Derivation Path : {wallet['derivation_path']}")
        print(f"Address         : {wallet['address']}")
        print(f"Private Key     : {wallet['private_key']}")
        print()

    print("⚠️  Private keys control funds. Handle securely.\n")


if __name__ == "__main__":
    main()
