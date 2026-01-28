"""
Etherscan Investigator Tool (v2 API)

Shows:
1. ETH Balance
2. Last 5 Normal Transactions
3. Last 5 ERC-20 Token Transfers
4. Contract Source Code Check (if address is a contract)

Install:
pip install requests

Test with Vitalik's address: 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

"""

import requests

API_KEY = "I2GE1SVZN5DJXS5PH564YJDMQZUD9XNWX5"
BASE_URL = "https://api.etherscan.io/v2/api"
CHAIN_ID = 1  # Ethereum Mainnet


# ---------------------------------------------------------
# Helper: API Call
# ---------------------------------------------------------
def call_etherscan(params: dict):
    params["chainid"] = CHAIN_ID
    params["apikey"] = API_KEY

    r = requests.get(BASE_URL, params=params)
    data = r.json()

    if data.get("status") != "1":
        print("\n❌ API Error:", data.get("result"))
        return None

    return data["result"]


# ---------------------------------------------------------
# 1. ETH Balance
# ---------------------------------------------------------
def get_balance(address: str):
    result = call_etherscan({
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest"
    })
    if result:
        eth = int(result) / 1e18
        print("\nETH BALANCE")
        print("=" * 50)
        print("Address:", address)
        print("Balance:", eth, "ETH")


# ---------------------------------------------------------
# 2. Last Normal Transactions
# ---------------------------------------------------------
def get_transactions(address: str):
    result = call_etherscan({
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc"
    })

    if not result:
        return

    print("\nLAST 5 NORMAL TRANSACTIONS")
    print("=" * 50)

    for tx in result[:5]:
        print("TX Hash :", tx["hash"])
        print("From    :", tx["from"])
        print("To      :", tx["to"])
        print("Value   :", int(tx["value"]) / 1e18, "ETH")
        print("Block   :", tx["blockNumber"])
        print("-" * 40)


# ---------------------------------------------------------
# 3. Last ERC-20 Token Transfers
# ---------------------------------------------------------
def get_token_transfers(address: str):
    result = call_etherscan({
        "module": "account",
        "action": "tokentx",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc"
    })

    if not result:
        return

    print("\nLAST 5 ERC-20 TOKEN TRANSFERS")
    print("=" * 50)

    for tx in result[:5]:
        amount = int(tx["value"]) / (10 ** int(tx["tokenDecimal"]))

        print("Token   :", tx["tokenSymbol"])
        print("From    :", tx["from"])
        print("To      :", tx["to"])
        print("Amount  :", amount)
        print("TX Hash :", tx["hash"])
        print("-" * 40)


# ---------------------------------------------------------
# 4. Contract Source Check
# ---------------------------------------------------------
def contract_source(address: str):
    result = call_etherscan({
        "module": "contract",
        "action": "getsourcecode",
        "address": address
    })

    if not result:
        return

    info = result[0]

    print("\nCONTRACT SOURCE CHECK")
    print("=" * 50)

    if info["ContractName"] == "":
        print("Not a verified smart contract.")
    else:
        print("Contract Name:", info["ContractName"])
        print("Compiler     :", info["CompilerVersion"])
        print("Verified ✅   : Yes")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
if __name__ == "__main__":
    print("\nETHERSCAN INVESTIGATOR TOOL")
    print("=" * 60)

    addr = input("Enter Ethereum address: ").strip()

    get_balance(addr)
    get_transactions(addr)
    get_token_transfers(addr)
    contract_source(addr)

    print("\n✅ Done.\n")
