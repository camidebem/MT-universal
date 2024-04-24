import json

nome_arquivo = "entrada.json"
# Função para ler o arquivo JSON
def ler_json(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo: # abrindo no modo para leitura (Read)
        dados_json = json.load(arquivo)
    return dados_json

dados_mt = ler_json(nome_arquivo) # chama a função de leitura 

# Exibindo os dados lidos
print("Alfabeto:", dados_mt["alfabeto"])
print("Estados:", dados_mt["estados"])
print("Estado Inicial:", dados_mt["estadoInicial"])
print("Estados Finais:", dados_mt["estadosFinais"])
print("Transições:")
for transicao in dados_mt["transicoes"]:
    print(transicao)


# fazer um dicionário da codificação 
dic_qualquer = {"0" : 1, "1" : 11, "B" : 111, "L" : 1, "R" : 11}

def encode(input):
    if(len(input) == 1): # se houver apenas um caractere, é tratamento especial.
        codificacao = str(dic_qualquer[input])
        
        return codificacao
    elif(len(input) > 1): # se houver mais de um caractere, é um estado.
        auxiliar_num = input[1]
        auxiliar_num = int(auxiliar_num) + 1

        codificacao = "1" * auxiliar_num
        return codificacao

    
# encode(estado)+ 0 + encode(X)+ 0 +encode
transicoes_codificadas = ""
for dicionario_transicao in dados_mt["transicoes"]:
    for _, valor in dicionario_transicao.items():
        transicoes_codificadas += encode(valor)+"0"
    transicoes_codificadas += "0"


print(transicoes_codificadas)



