<p align="center">
  <img src="assets/banner.png" alt="Public Key to Bitcoin Addresses banner" width="100%" />
</p>

<<<<<<< HEAD
## Project Description
=======
# 🧠 PUBLIC KEY TO BITCOIN ADDRESSES

**Public Key to Bitcoin Addresses** is a compact and reliable Python utility that converts an uncompressed Bitcoin public key to both compressed and uncompressed Bitcoin addresses using built-in encoding logic.
>>>>>>> 94c1743 (Add project README.md)

- ✅ Key compression (`04...` → `02...` / `03...`)
- ✅ Uncompressed and compressed address generation
- ✅ Base58Check output (legacy-compatible)
- ✅ Color-coded output in terminal

---

## ⚙️ Features

- 🔁 Compresses uncompressed public keys
- 🔐 Generates valid Bitcoin addresses (both forms)
- 🖥️ CLI-based interaction via terminal
- 🎨 Visual feedback using `termcolor`

---

## 📁 File Overview

- `public_key_to_bitcoin_addresses.py` – Main conversion script  
- `public_key_to_bitcoin_addresses.bat` – Windows launcher  
- `.vscode/`  
  - `settings.json` – Editor preferences  
  - `launch.json` – Debugging configuration  
  - `tasks.json` – Task runner integration  
  - `extensions.json` – Recommended VS Code extensions  
- `README.md` – This documentation  
- `ETHICS.md` – Ethical usage guidelines  
- `NOTICE` – Third-party attributions  
- `LICENSE` – Apache 2.0 license  
- `requirements.txt` – Python dependencies  

---

## 🛠️ Dependencies

```
pycryptodome
base58
termcolor
```

Install with:

```bash
pip install -r requirements.txt
```

> Python 3.8+ is recommended.

---

## 🚀 Usage

### Option 1 – via Python:
```bash
python public_key_to_bitcoin_addresses.py
```

### Option 2 – via `.bat` launcher (Windows):
```cmd
public_key_to_bitcoin_addresses.bat
```

- Input: 130-character uncompressed public key (starts with `04`)  
- Output:  
  - Compressed public key (`02`/`03`)  
  - Bitcoin address from uncompressed key  
  - Bitcoin address from compressed key  

---

## 📦 Example Output

```
Compressed Public Key:
  03a34f7b56d...

Bitcoin Address (Uncompressed):
  1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

Bitcoin Address (Compressed):
  1PMycacnJaSqwwJqjawXBErnLsZ7RkXUAs
```

---

## ⚠️ DISCLAIMER

This software is provided strictly for **educational, analytical, and research purposes only**.

The author **does not promote or condone** any unethical behavior, unauthorized access, or abuse of blockchain systems or cryptographic tools.  
By using this code, you agree to accept **full responsibility for your actions and their consequences**.

This project **does not include or generate any real private keys** linked to actual cryptocurrency holdings.  
It is designed to operate in **offline environments** or for simulation/testing purposes, using random or mock data for learning.

**The author accepts no liability** for any damages, losses, or illegal use resulting from this software.  
All responsibility lies solely with the end user.

Any attempt to use this tool maliciously or exploitatively is **strictly prohibited** and may violate international laws.

> **Use responsibly. Learn ethically. Contribute honestly.**

---

## ⚖️ Ethical Use

This tool is created strictly for **research and educational purposes**.  
See [ETHICS.md](./ETHICS.md) for the full statement.

> ❗ Do not use this tool for brute-force attempts or unauthorized activity.  
> 🧠 Use responsibly and with integrity.

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE)

---

## 📣 NOTICE

See [`NOTICE`](./NOTICE) for important information about attribution, DMCA protection, and reuse permissions.

---

## 📂 Project Structure

```
public-key-to-bitcoin-addresses/
├── assets/
│   └── banner.png
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── public_key_to_bitcoin_addresses.py
├── public_key_to_bitcoin_addresses.bat
├── LICENSE
├── NOTICE
├── ETHICS.md
├── README.md
├── requirements.txt
```

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

<<<<<<< HEAD
Created with dedication to education, blockchain exploration, and ethical research.  
*“I morph bits, not to break, but to understand.” — BitMorphX*
=======
## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
>>>>>>> 94c1743 (Add project README.md)
