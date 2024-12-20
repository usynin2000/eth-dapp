from web3 import Web3
from solcx import compile_standard, install_solc
import json
from config import INFURA_API_KEY, PRIVATE_KEY

# Установим конкретную версию солc, если нужно
install_solc('0.8.0')

# Загрузим контракт из файла
with open("SimpleToken.sol", "r") as file:
    simple_token_source = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleToken.sol": {"content": simple_token_source}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled.json", "w", encoding="utf-8") as f:
    json.dump(compiled_sol, f, ensure_ascii=False, indent=4)


# ABI и Bytecode
abi = compiled_sol["contracts"]["SimpleToken.sol"]["SimpleToken"]["abi"]
bytecode = compiled_sol["contracts"]["SimpleToken.sol"]["SimpleToken"]["evm"]["bytecode"]["object"]

YOUR_INFURA_PROJECT_ID = INFURA_API_KEY

# Подключаемся к Sepolia RPC (например, публичный RPC)
w3 = Web3(Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{YOUR_INFURA_PROJECT_ID}"))

# Аккаунт
private_key = PRIVATE_KEY
account = w3.eth.account.from_key(private_key)
account_address = account.address

SimpleToken = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.get_transaction_count(account_address)

transaction = SimpleToken.constructor().build_transaction({
    "chainId": 11155111, # chainId для Sepolia
    "gas": 3000000,
    "gasPrice": w3.eth.gas_price,
    "nonce": nonce
})

signed_tx = account.sign_transaction(transaction)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress

if __name__ == "__main__":
# Создаем транзакцию на деплой

    print("Contract deployed at:", contract_address)


##
# Мы используем Python для того, чтобы:
#
# Скомпилировать смарт-контракт на Solidity.
# Подключиться к удаленному Ethereum-совместимому узлу (в данном случае — тестовой сети Sepolia через Infura).
# Подписать и отправить транзакцию для деплоя (развертывания) контракта в сеть.
# Дождаться подтверждения транзакции и получить адрес развернутого контракта.
