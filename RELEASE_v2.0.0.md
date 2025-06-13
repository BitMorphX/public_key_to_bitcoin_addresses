# 📎 RELEASE NOTES – public_key_to_bitcoin_addresses.py  
**Version:** 2.0.0  
**Release Date:** 2025-06-14

---

## 🚀 Overview

Version 2.0.0 brings a complete overhaul of the project structure, documentation, licensing, and platform support.

While v1.0.0 delivered a simple CLI for converting public keys to Bitcoin addresses, this version expands the tool into a fully documented, offline-ready utility with launch support, editor integration, and ethical usage policy.

---

## 🔄 What Changed Since v1.0.0

### 📄 Documentation

- ✅ Full `README.md` with usage, features, examples, license, support, and structure  
- ✅ Added `ETHICS.md` defining ethical usage guidelines  
- ✅ Added `NOTICE` for third-party library attributions  
- ✅ Introduced structured release notes (`RELEASE_v2.0.0.md`)

### ⚙️ Tooling & Integration

- ✅ `public_key_to_bitcoin_addresses.bat` – Windows one-click launcher  
- ✅ `.vscode/` directory with:
  - `settings.json`
  - `launch.json`
  - `tasks.json`
  - `extensions.json`
- ✅ `requirements.txt` file for dependency management

### 📜 Licensing

- 🛡️ License changed from **MIT** → **Apache 2.0** for improved clarity and protection

---

## ✅ Included in v2.0.0

- `public_key_to_bitcoin_addresses.py` – Main CLI tool  
- `public_key_to_bitcoin_addresses.bat` – Windows launcher  
- `README.md` – Full project documentation  
- `ETHICS.md` – Ethical usage policy  
- `LICENSE` – Apache 2.0 license  
- `NOTICE` – Third-party attributions  
- `.vscode/` – VS Code integration  
- `requirements.txt` – Python dependencies  
- `RELEASE_v1.0.0.md` – Previous release notes  
- `RELEASE_v2.0.0.md` – This file

---

## 📌 Feature Recap

Still included from v1.0.0:
- Converts uncompressed public keys to compressed format  
- Generates both legacy and compressed Bitcoin addresses  
- Uses SHA-256 and RIPEMD-160 hashing  
- Performs Base58Check encoding  
- Outputs to terminal using `termcolor`  
- 100% offline, deterministic address creation

---

## ⚠️ Notes

- Requires Python 3.8+  
- Expects a valid uncompressed public key starting with `04`  
- Does not connect to any blockchain networks  
- No private key generation – only address derivation from input key

---

## 📜 License  
Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**

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

## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
