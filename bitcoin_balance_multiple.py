import requests

BASE_URL = "https://blockstream.info/api"

def get_btc_balance(address):
    response = requests.get(f"{BASE_URL}/address/{address}", timeout=10)
    data = response.json()
    return data["chain_stats"]["funded_txo_sum"] - data["chain_stats"]["spent_txo_sum"]


suspect_addresses = [
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"
]

for address in suspect_addresses:
    balance = get_btc_balance(address)
    print(address, "→", balance, "sats")