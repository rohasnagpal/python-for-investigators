# Check the balance of a single Bitcoin address.

import requests

BASE_URL = "https://blockstream.info/api"

def get_btc_balance(address):
    response = requests.get(f"{BASE_URL}/address/{address}")
    data = response.json()
    return data["chain_stats"]["funded_txo_sum"] - data["chain_stats"]["spent_txo_sum"]

address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

balance = get_btc_balance(address)
print("Balance (sats):", balance)