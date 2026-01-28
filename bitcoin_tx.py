# Fetches a Bitcoin transaction from the BlockCypher API and prints its inputs and outputs, handling coinbase transactions and invalid TXIDs safely. Example TXID: 3e6aa9282f16e27cbf2a417b260081a42ce884b826807f3e060f0eb3074aefbc

import requests

BASE_URL = "https://api.blockcypher.com/v1/btc/main"

def transaction_trace(txid: str):
    url = f"{BASE_URL}/txs/{txid}"
    r = requests.get(url)
    data = r.json()

    # Handle invalid TXID or API error
    if "error" in data:
        print("\n❌ API ERROR:", data["error"])
        return

    print("\nTRANSACTION TRACE")
    print("=" * 50)
    print("TXID:", data["hash"])
    print("Confirmations:", data["confirmations"])

    print("\nINPUTS:")
    for inp in data["inputs"]:
        value = inp.get("output_value")
        if value is None:
            print(" - Coinbase Input")
        else:
            print(" - From:", inp.get("addresses"))
            print("   Value:", value, "sats")

    print("\nOUTPUTS:")
    for out in data["outputs"]:
        print(" - To:", out.get("addresses"))
        print("   Value:", out["value"], "sats")


if __name__ == "__main__":
    txid = input("Enter TXID: ").strip()
    transaction_trace(txid)
