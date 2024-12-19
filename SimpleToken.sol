// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleToken {
    string public name = "MyTestToken";
    string public symbol = "MTT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000 * (10 ** uint256(decimals));

    mapping(address => uint256) public balanceOf;

    constructor() {
        // Все токены изначально принадлежат создателю
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _amount) public returns (bool success) {
        require(balanceOf[msg.sender] >= _amount, "Not enough tokens");
        balanceOf[msg.sender] -= _amount;
        balanceOf[_to] += _amount;
        return true;
    }
}

//Этот контракт:
//
//Создает простые токены.
//Хранит балансы в balanceOf.
//Позволяет вызывать transfer для перевода токенов