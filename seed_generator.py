from mnemonic import Mnemonic
from datetime import datetime

def generate_all_mnemonics() -> dict:
    strength_map = {
        12: 128,
        15: 160,
        18: 192,
        21: 224,
        24: 256
    }

    mnemo = Mnemonic("english")
    mnemonics = {}

    for words, strength in strength_map.items():
        mnemonics[words] = mnemo.generate(strength=strength)

    return mnemonics

def main():
    mnemonics = generate_all_mnemonics()

    print("\nBIP-39 SEED PHRASE GENERATOR")
    print("=" * 40)
    print(f"Generated at (UTC): {datetime.utcnow()}\n")

    for word_count in sorted(mnemonics.keys()):
        print(f"{word_count} WORD SEED")
        print("-" * 40)
        print(mnemonics[word_count])
        print()

    print("⚠️ WARNING:")
    print("Anyone with access to these seed phrases controls the wallets.\n")


if __name__ == "__main__":
    main()