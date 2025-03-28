# Calculadora de Expressões Matemáticas

Este projeto é uma implementação simples de uma **calculadora** que recebe uma expressão matemática do usuário, identifica automaticamente o operador inserido e realiza a operação correspondente entre dois números inteiros. O código trata operações de soma, subtração, multiplicação e divisão, além de ter uma verificação para evitar a divisão por zero.

## Funcionalidades

- Recebe uma **expressão matemática** do usuário no formato `número1 operador número2` (ex: `2+3`).
- Identifica automaticamente o operador: **+**, **-**, **\***, **/**.
- Realiza a operação matemática correspondente entre os dois números.
- **Tratamento de erro** para divisão por zero.

## Estrutura do Código

O código está organizado em funções para modularizar as operações:

- **`input_valores()`**: Recebe a expressão matemática do usuário, identifica o operador e extrai os números.
  
- **Funções de operação**:
  - **`soma()`**: Realiza a soma entre dois números.
  - **`subtracao()`**: Realiza a subtração entre dois números.
  - **`multiplicacao()`**: Realiza a multiplicação entre dois números.
  - **`divisao()`**: Realiza a divisão entre dois números.
