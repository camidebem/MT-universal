# Conversor de Máquina de Turing para Máquina de Turing Universal

Este é um projeto para converter uma Máquina de Turing (MT) em uma Máquina de Turing Universal (MTU). Uma MTU é uma Máquina de Turing especializada que é capaz de simular o comportamento de qualquer outra Máquina de Turing. Ela tem a capacidade de interpretar descrições de outras MTs e executar seus comportamentos.

## Passos do Projeto

### 1. Entrada

O projeto aceita como entrada um arquivo JSON descrevendo uma Máquina de Turing. O alfabeto da Máquina de Turing é restrito aos símbolos "0" e "1".

### 2. Codificação

Antes de converter a MT para uma MTU, os símbolos da MT precisam ser codificados. Utilizamos a seguinte codificação:

| Símbolo MT  | Codificação MTU |
|-------------|-----------------|
| 0           | 1               |
| 1           | 11              |
| B           | 111             |
| L           | 1               |
| R           | 11              |

### 3. Mapeamento das Funções de Transição

O projeto mapeia as funções de transição da Máquina de Turing normal.

### 4. Encode

As funções de transição são então convertidas em uma representação binária utilizando a codificação descrita acima (encoded)

## 5. Próximos passos ainda a serem definidos. 
