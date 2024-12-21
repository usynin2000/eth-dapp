from web3 import Web3

from config import INFURA_API_KEY
from typing import Any
import json


def get_balance(contract_address: str, account_address: str) -> Any:
    with open("compiled.json", "r") as f:
        res = json.load(f)

    abi = res["contracts"]["SimpleToken.sol"]["SimpleToken"]["abi"]

    w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"))
    contract = w3.eth.contract(address=contract_address, abi=abi)
    balance = contract.functions.balanceOf(account_address).call()
    return balance


if __name__ == "__main__":
    contract_address = "0x40d87A3c7003A5A2dDA819721F998757fFcb65a8"
    account_address = "0xac0fDFfe0F1E474D41Dc14B745f0846CB2362e9F"
    balance = get_balance(contract_address, account_address)
    print("Balance:", balance)
