import requests

BASE_URL = "https://blockstream.info/api"

print("Fetching latest Bitcoin block...")

# Step 1: Get latest block hash
latest_hash = requests.get(f"{BASE_URL}/blocks/tip/hash").text

# Step 2: Get full block details using hash
block_data = requests.get(f"{BASE_URL}/block/{latest_hash}").json()

print("\n--- BITCOIN LATEST BLOCK REPORT ---")
print("Block Hash:", latest_hash)
print("Block Height:", block_data["height"])
print("Timestamp:", block_data["timestamp"])
print("Transaction Count:", block_data["tx_count"])
print("Block Size (bytes):", block_data["size"])