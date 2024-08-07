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

## 5. Próximos passos 

## Inicialização das Fitas:
- A fita 1 inicia com a entrada que representa a codificação da Máquina de Turing 𝑀 e a cadeia 𝑤 a ser processada por 𝑀.
- A fita 2 é utilizada para representar o estado atual de 𝑀.
- A fita 3 é utilizada para simular a computação de 𝑀.

## Conversão e Escrita Inicial:
- Verifique se a entrada na fita 1 está na forma correta (𝑅(𝑀)𝑤). Se não estiver, a máquina deve se mover para a direita indefinidamente (indicando rejeição).
- Copie a cadeia 𝑤 para o início da fita 3 e retorne a cabeça da fita 3 para o início.
- Escreva o estado inicial 𝑞₀ (codificado como "1") na fita 2.

## Simulação das Transições:
- Leia o símbolo atual na fita 3 e o estado atual na fita 2.
- Procure na fita 1 por uma transição correspondente.
- Se a transição for encontrada:
Atualize o estado na fita 2.
Escreva o novo símbolo na fita 3.
Mova a cabeça da fita 3 conforme especificado pela transição (L ou R).
- Repita o processo até que a entrada seja aceita ou rejeitada.







