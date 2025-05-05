# 📌 Public Key to Bitcoin Addresses Generator

## Project Description

**public_key_to_bitcoin_addresses.py** is a Python script designed to generate Bitcoin addresses from an uncompressed public key.
The program automatically:
- 🔄 Converts an uncompressed public key into compressed format.
- 🛠️ Generates Bitcoin addresses for both compressed and uncompressed keys.

This project is intended for **educational and learning purposes** only.

---

## Features

- ✅ Validates whether the provided public key is correctly formatted.
- 🔒 Performs SHA-256 and RIPEMD-160 hashing.
- 🚀 Creates Bitcoin addresses using Base58Check encoding.
- 🎯 Outputs addresses for both compressed and uncompressed keys.

---

## Requirements

- 🐍 Python 3.6+

**Required libraries:**
```bash
pip install pycryptodome base58 termcolor
```

Run the program:

```bash
python public_key_to_bitcoin_addresses.py
```

Enter an uncompressed public key (130 characters, starting with "04").

The program will display:
- The compressed public key.
- Bitcoin address derived from the uncompressed key.
- Bitcoin address derived from the compressed key.

---

## License

This project is distributed under the [MIT License](LICENSE), allowing you to:
- 📖 Use freely
- 📚 Copy
- ✏️ Modify
- 📢 Distribute with proper attribution to the original author.

For more information, see the [LICENSE](LICENSE) file.

---

## Disclaimer

- 🚫 This tool is for educational and learning purposes only.
- ⚠️ Do not use this program in production environments or for financial transactions.
- ❗ The author is not liable for any losses, data corruption, financial damages, or any other consequences arising from the use of this project.
- 🛡️ Use at your own risk.

---

## 🎁 Support

If you'd like to support future development and research:

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

---

We also value early privacy coins such as **Bytecoin (BCN)**:

`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

Created with dedication to education, blockchain exploration, and ethical research.  
*“I morph bits, not to break, but to understand.” — BitMorphX*
