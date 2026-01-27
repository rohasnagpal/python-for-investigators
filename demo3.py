# Example: dictionary storing investigation results for one Bitcoin address

address_result = {
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "balance_sats": 5451877840,
    "has_activity": True,
    "source": "blockstream_api",
    "checked_at": "2026-01-28 14:10:00 IST"
}

# Accessing values
print(address_result["address"])
print(address_result["balance_sats"])
print(address_result["has_activity"])