"""
Bitcoin Wallet Generator (bitcoinlib)

Creates:
1. Legacy address (P2PKH)
2. Native SegWit address (Bech32)

Prints address + private key.
"""

from bitcoinlib.wallets import Wallet
from datetime import datetime


suffix = datetime.utcnow().strftime("%Y%m%d%H%M%S")


# ---------------------------------------------------------
# 1. Legacy Wallet (P2PKH)
# ---------------------------------------------------------
legacy_wallet = Wallet.create(
    f"LegacyWallet_{suffix}",
    witness_type="legacy"
)

legacy_key = legacy_wallet.get_key()

print("\nLEGACY WALLET (P2PKH)")
print("=" * 40)
print("Address       :", legacy_key.address)
print("Private Key   :", legacy_key.wif)


# ---------------------------------------------------------
# 2. Native SegWit Wallet (Bech32)
# ---------------------------------------------------------
segwit_wallet = Wallet.create(
    f"SegWitWallet_{suffix}",
    witness_type="segwit"
)

segwit_key = segwit_wallet.get_key()

print("\nNATIVE SEGWIT WALLET (Bech32)")
print("=" * 40)
print("Address       :", segwit_key.address)
print("Private Key   :", segwit_key.wif)

print("\n⚠️ Handle private keys securely.\n")
