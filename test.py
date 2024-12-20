import json

with open("compiled.json", "r") as f:
    res = json.load(f)
    print(type(res))


abi = res["contracts"]["SimpleToken.sol"]["SimpleToken"]["abi"]


