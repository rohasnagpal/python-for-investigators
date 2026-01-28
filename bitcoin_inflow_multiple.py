# Investigate inflows across multiple addresses to identify funding patterns.

import requests
import time

BASE_URL = "https://blockstream.info/api"

# Returns total confirmed inflow (in satoshis) for a Bitcoin address
def get_total_inflow(address):
    r = requests.get(f"{BASE_URL}/address/{address}", timeout=10)
    r.raise_for_status()
    data = r.json()
    return data["chain_stats"]["funded_txo_sum"]

wallets = [
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
    "1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp",
    "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY",
    "1Ez69SnzzmePmZX3WpEzMKTrcBF2gpNQ55",
    "1dice97ECuByXAvqXpaYzSaQuPVvrtmz6",
    "1CounterpartyXXXXXXXXXXXXXXXUWLpVr",
    "1BitcoinEaterAddressDontSendf59kuE"
]

for wallet in wallets:
    try:
        inflow = get_total_inflow(wallet)
        print(wallet, "→ total inflow:", inflow, "sats")
    except Exception as e:
        print(wallet, "→ ERROR")
    time.sleep(0.4)