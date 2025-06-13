@echo off
title Public Key to Bitcoin Addresses
color 0A

:: Activate virtual environment if it exists
IF EXIST .venv\Scripts\activate (
    call .venv\Scripts\activate
)

:: Run the script
python public_key_to_bitcoin_addresses.py

pause