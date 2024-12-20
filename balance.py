from web3 import Web3

from config import INFURA_API_KEY
from test import abi

w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{INFURA_API_KEY}"))

contract_address = "0x40d87A3c7003A5A2dDA819721F998757fFcb65a8"

contract = w3.eth.contract(address=contract_address, abi=abi)

account_address = "0xac0fDFfe0F1E474D41Dc14B745f0846CB2362e9F"

balance = contract.functions.balanceOf(account_address).call()
print("Balance:", balance)