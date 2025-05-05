__version__ = "1.0.0"

import os
from Crypto.Hash import RIPEMD160
import hashlib
import base58
from termcolor import colored

def compress_public_key(uncompressed_key):
    # Check if the public key is valid
    if not uncompressed_key.startswith("04") or len(uncompressed_key) != 130:
        return "Invalid uncompressed public key! It must start with '04' and be 130 characters long."

    # Remove "04" prefix
    x = uncompressed_key[2:66]
    y = int(uncompressed_key[66:], 16)

    # Determine prefix based on Y parity
    prefix = '02' if y % 2 == 0 else '03'

    # Generate compressed public key
    compressed_key = prefix + x
    return compressed_key

def ripemd160_hash(data):
    h = RIPEMD160.new()
    h.update(data)
    return h.digest()

def generate_bitcoin_address(public_key, compressed=True):
    sha256 = hashlib.sha256(bytes.fromhex(public_key)).digest()
    ripemd160 = ripemd160_hash(sha256)
    
    # Add version byte (0x00 for Bitcoin mainnet)
    versioned_ripemd160 = b'\x00' + ripemd160
    
    # Calculate checksum
    checksum = hashlib.sha256(hashlib.sha256(versioned_ripemd160).digest()).digest()[:4]

    # Final Base58Check encoded address
    address = base58.b58encode(versioned_ripemd160 + checksum).decode('utf-8')
    return address

if __name__ == "__main__":
    # Clear the terminal
    os.system('clear')

    # Input
    uncompressed_key = input("\n\033[92mEnter the uncompressed public key (130 characters, starting with '04'): \033[0m")

    # Convert to compressed public key
    compressed_key = compress_public_key(uncompressed_key)

    # Display results
    if compressed_key.startswith("02") or compressed_key.startswith("03"):
        print("\n", colored("Compressed Public Key:", "yellow"), "\n", colored(compressed_key, "cyan"))

        uncompressed_address = generate_bitcoin_address(uncompressed_key, compressed=False)
        compressed_address = generate_bitcoin_address(compressed_key, compressed=True)

        print("\n", colored("Bitcoin Address (Uncompressed):", "yellow"), "\n", colored(uncompressed_address, "cyan"))
        print("\n", colored("Bitcoin Address (Compressed):", "yellow"), "\n", colored(compressed_address, "cyan"))
    else:
        print("\n", colored("Error:", "red"), compressed_key)
