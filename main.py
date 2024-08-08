import json

nome_arquivo = "entrada.json"
# Função para ler o arquivo JSON
def ler_json(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo: # abrindo no modo para leitura (Read)
        dados_json = json.load(arquivo)
    return dados_json

def encode(input, dic_qualquer):
    if(len(input) == 1): # se houver apenas um caractere, é tratamento especial.
        codificacao = str(dic_qualquer[input])
        return codificacao
    elif(len(input) > 1): # se houver mais de um caractere, é um estado.
        auxiliar_num = int(input[1]) + 1
        codificacao = "1" * auxiliar_num
        return codificacao
    
# encode(estadoAtual)+ 0 + encode(X)+ 0 +encode(Y) + encode(proximoEstado)+ encode(Direcao)
# Função para preparar a fita 1 com a codificação das transições
def prep_fita1(dados_mt, dic_qualquer):
    fita1Encode = "000"
    for dicionario_transicao in dados_mt["transicoes"]:
        for _, valor in dicionario_transicao.items():
            fita1Encode += encode(valor, dic_qualquer)+ "0"
        fita1Encode += "0"
    fita1Encode += "0"
    return fita1Encode

def processar_fita1(fita1Encode):
    # Remover os três zeros iniciais e finais
    fita1_processada = fita1Encode[3:-3]
    # Separar cada transição que é delimitada por 2 zeros
    fita1 = fita1_processada.split("00")
    return fita1

def processar_fita(fitas):
    # Separar a palavra conforme necessário
    fita = "".join(fitas).split("0")
    return [p for p in fita if p]  # Remove elementos vazios

def encodeEstadosFinais(dados_mt, dic_qualquer):
    estadoFinalEncode = ""
    
    for estadoFinal in dados_mt["estadosFinais"]:
        estadoFinalEncode += encode(estadoFinal, dic_qualquer) + '0'

    return estadoFinalEncode

def transicaoParaDicionario(transicao_partes):
		transicao_partes = transicao_partes.split('0')
		return {
        'estado_inicial': transicao_partes[0],
        'simbolo_entrada': transicao_partes[1],
        'simbolo_escrita': transicao_partes[2],
        'estado_destino': transicao_partes[3],
        'direcao': transicao_partes[4]
    }

def buscar_transicao(fita2, fita3, cabeca_maquina, fita1):

    transicoes = []
    # Cria uma lista com todas as transições que existem partindo do estado atual
    for transicao in fita1:
         if transicao['estado_inicial'] == fita2:
              transicoes.append(transicao)

    # Se não tiver transições, a lista será vazia
    if transicoes == []:
        
        return False, None

    # Para todas as possíveis transições partindo do estado atual, executar a que convém
    for transicao in transicoes:
        if cabeca_maquina < len(fita3) and transicao['simbolo_entrada'] == fita3[cabeca_maquina]:
            
            return True, transicao

    return False, None

def executar_transicao(fita2, fita3, cabeca_maquina, transicao):
    fita2 = transicao['estado_destino']
    fita3[cabeca_maquina] = transicao['simbolo_escrita']
    if transicao['direcao'] == "11":
        cabeca_maquina += 1
    else:
        cabeca_maquina -= 1
        if cabeca_maquina < 0:
            raise Exception("ErroMaquina")

    return fita2, fita3, cabeca_maquina

def executar_maquina(fita1, fita2, fita3, cabeca_maquina, estadosFinais):
    REJEITA = "\nPalavra rejeitada\n"
    ACEITA = "\nPalavra aceita\n"

    i = 1

    resultado, ultima_transicao = buscar_transicao(fita2, fita3, cabeca_maquina, fita1)
    
    while resultado and ultima_transicao != None:
        # Heurísticas para detectar loops infinitos
        if i > (len(fita3) ** len(fita1)):
            print(REJEITA)
            print("possível loop infinito")
            return

        i += 1

        
        fita2, fita3, cabeca_maquina = executar_transicao(fita2, fita3, cabeca_maquina, ultima_transicao)
        
        resultado, ultima_transicao = buscar_transicao(fita2, fita3, cabeca_maquina, fita1)
        
        
        
    if fita2 in estadosFinais and cabeca_maquina == len(fita3):
        print(ACEITA)
    else:
        print(REJEITA)
    

dados_mt = ler_json(nome_arquivo) # chama a função de leitura
# fazer um dicionário da codificação 
dic_qualquer = {"0" : 1, "1" : 11, "B" : 111, "L" : 1, "R" : 11}
#preparando lista com estados finais
estadosFinais = processar_fita(encodeEstadosFinais(dados_mt, dic_qualquer))
#preparando a fita 1
fita1Separada = processar_fita1(prep_fita1(dados_mt, dic_qualquer))
fita1 = [transicaoParaDicionario(tran) for tran in fita1Separada]
# Preparando a fita 2, colocando o estado q0 em unario
fita2 = "1"
# Preparando a fita 3 e a cabeca para mover para direita e esquerda, a entrada ja esta na forma unaria
fita3 = processar_fita(list(dados_mt["entrada"]))
#Inicia na posicao 0 da maquina
cabeca_maquina = 0

#executa toda a logica da maquina de transicoes, aceitacao e rejeicao
executar_maquina(fita1, fita2, fita3, cabeca_maquina, estadosFinais)
