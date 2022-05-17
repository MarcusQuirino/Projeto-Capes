# Análise de Banco de Dados de Bolsistas da CAPES
# Marcus Filipe C. P. Quirino
# 23/03/22
# Importar a biblioteca pandas utilizada pra ler e interpretar as informações no arquivo .csv
import pandas as pd
import sys
# Atribuindo o banco de dados a variavel df (DataFrame)
df = pd.read_csv("capes_bolsistas.csv")


# Conjunto de funções necessárias
# Função meio gambiarra pra limpar a tela. Printa 100 linhas em branco
def clear():
    print(100 * "\n")


# Função usada para retirar os espaços na função buscar_bolsista()
def remove(string):
    return "".join(string.split())


# Função usada para encriptar o nome do bolsista na função buscar_bolsita
def encriptar_nome(nome_descriptado):
    # Lista com as letras do alfabeto para aplicar a cifra de cesar
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    # Pegar primeira letra do nome do bolsista
    primeira_letra = nome_descriptado[0]
    # Pegar a ultima letra do nome do bolsista
    ultima_letra = nome_descriptado[-1]
    # Variavel vazia
    meio = ""
    # For loop pra retirar o meio do nome do bolsista
    for vezes in range(1, len(nome_descriptado) - 1):
        meio += nome_descriptado[vezes]
    # Primeira parte da criptografia que consistia em inverter as letras do nome menos a última e a primeira
    nome_pre_encriptado = primeira_letra + meio[::-1] + ultima_letra
    nome_encriptado = ""
    # For loop necessário por aplicar a cifra de cesar
    for letra in nome_pre_encriptado.upper():
        # Verificar a posicão da letra no alfabeto
        posicao = alfabeto.index(letra)
        # Mudar a posição da letra em 1
        nova_posicao = posicao + 1
        nova_letra = alfabeto[nova_posicao]
        nome_encriptado += nova_letra
        # Retorna o nome encriptado
    return nome_encriptado


# lógica do menu
def selecao_interface():
    option = int(input("> "))
    if option == 1:
        # Chamar função de consultar bolsa zero/ano
        consultar_bolsa_ano()
    elif option == 2:
        # Chamar função de pesquisar por bolsista e encriptar nome
        buscar_bolsista()
    elif option == 3:
        # Chamar função de consultar média anual
        media_anual()
    elif option == 4:
        # Chamar função de rankear as 3 maiores e menores bolsas de todos os tempos
        ranking_bolsas()
    elif option == 0:
        # Fechar programa
        sys.exit()
    else:
        # Código responsavel por impedir input inválido
        while option != (1, 2, 3, 4, 0):
            print("DIGITE UM NÚMERO VÁLIDO: (1, 2, 3, 4 OU 0)\n")
            option = int(input("> "))
            if option == 1:
                consultar_bolsa_ano()
            elif option == 2:
                buscar_bolsista()
            elif option == 3:
                media_anual()
            elif option == 4:
                ranking_bolsas()
            elif option == 0:
                sys.exit()


# interface inicial
def interface_inicial():
    # Limpa a tela
    clear()
    # Interface grafica do menu
    print(53 * "#")
    print("====ANÁLIZE DE BANDO DE DADOS DOS BOLSISTAS CAPES====\n")
    print("-[1]Consultar bolsa zero/Ano")
    print("-[2]Buscar Bolsista")
    print("-[3]Consultar média anual")
    print("-[4]Ranking dos valores das bolsas")
    print("-[0]sair")
    print("\nSelecione a opção digitando o número correspondente")
    print(53 * "#")
    # Chamar função de lógica do menu (linha: 53)
    selecao_interface()


# consultar bolsa zero/ano
def consultar_bolsa_ano():
    clear()
    print(52 * "#")
    print("======PRIMEIRO BOLSITA DO SEU RESPECTIVO ANO========\n")
    # Checar se o ano é válido
    ano = input("Digite o ano:\n> ")
    if int(ano) != 2013 and int(ano) != 2014 and int(ano) != 2015 and int(ano) != 2016:
        while int(ano) != 2013 and int(ano) != 2014 and int(ano) != 2015 and int(ano) != 2016:
            ano = input("Digite o ano:\n> ")
    lista_ano = df.loc[df["AN_REFERENCIA"] == int(ano)]
    lista_organizada = lista_ano.sort_index(ascending=False)
    dados_bolsista = lista_organizada[["NM_BOLSISTA", "CPF_BOLSISTA", "NM_ENTIDADE_ENSINO", "CD_MOEDA",
                                       "VL_BOLSISTA_PAGAMENTO"]]
    print(dados_bolsista.iloc[0])
    # Tentar de novo ou voltar ao menu principal
    print(52 * "#")
    option = int(input("Digite 1 pra tentar de novo ou 0 pra voltar ao menu principal\n> "))
    if option == 1:
        # Chamar função de novo
        consultar_bolsa_ano()
    elif option == 0:
        # Voltar ao menu principal
        interface_inicial()
    else:
        # Código responsavel por impedir input inválido
        while option != (1, 0):
            option = int(input("DIGITE UM NÚMERO VÁLIDO! (1 OU 0)\n> "))
            if option == 1:
                consultar_bolsa_ano()
            elif option == 0:
                interface_inicial()


# buscar bolsista
def buscar_bolsista():
    # Limpar tela
    clear()
    # Interface gráfica
    print(52 * "#")
    print("=================BUSCAR BOLSISTA====================\n")
    nome_bolsista = str(input("Digite o nome inteiro do bolsista:\n> "))
    # Localiza o nome do bolsista no banco de dados
    bolsita = df.loc[df["NM_BOLSISTA"] == nome_bolsista.upper()]
    # Atribui o nome do bolsista a variavel string
    string = bolsita.iloc[0, 0]
    # remove espaços do nome
    nome_bolsista_formatado = remove(string)
    # Encripta o nome com a função encriptar_nome() (linha: 22)
    encriptar_nome(nome_bolsista_formatado)
    # Filtra as informações relevantes no banco de dados
    info = bolsita[["AN_REFERENCIA", "NM_ENTIDADE_ENSINO", "CD_MOEDA", "VL_BOLSISTA_PAGAMENTO"]]
    # Mostra o resultado
    print(encriptar_nome(nome_bolsista_formatado))
    print(info)
    # Tentar de novo ou voltar ao menu principal
    print(52 * "#")
    option = int(input("Digite 1 pra tentar de novo ou 0 pra voltar ao menu principal\n> "))
    if option == 1:
        # Chamar função de novo
        buscar_bolsista()
    elif option == 0:
        # Voltar ao menu principal
        interface_inicial()
    else:
        # Código responsavel por impedir input inválido
        while option != (1, 0):
            option = int(input("DIGITE UM NÚMERO VÁLIDO! (1 OU 0)\n> "))
            if option == 1:
                consultar_bolsa_ano()
            elif option == 0:
                interface_inicial()


# media anual
def media_anual():
    # Limpa a tela
    clear()
    # Interface gráfica
    print(52 * "#")
    print("======MÉDIA ANUAL DAS BOLSAS========\n")
    ano = input("Digite o ano:\n> ")
    # Checar se o ano é válido
    if int(ano) != 2013 and int(ano) != 2014 and int(ano) != 2015 and int(ano) != 2016:
        while int(ano) != 2013 and int(ano) != 2014 and int(ano) != 2015 and int(ano) != 2016:
            ano = input("Digite o ano:\n> ")
    # Localiza o ano pedido
    lista_ano = df.loc[df["AN_REFERENCIA"] == int(ano)]
    # Filtra as informações relevantes no banco de dados
    lista_ano_formatada = lista_ano[["AN_REFERENCIA", "CD_MOEDA", "VL_BOLSISTA_PAGAMENTO"]]
    #  Mostra o resultado da média
    print(lista_ano_formatada.groupby(["AN_REFERENCIA"]).mean())
    # Tentar de novo ou voltar ao menu principal
    print(52 * "#")
    option = int(input("Digite 1 pra tentar de novo ou 0 pra voltar ao menu principal\n> "))
    if option == 1:
        # Chamar função de novo
        media_anual()
    elif option == 0:
        # Voltar ao menu principal
        interface_inicial()
    else:
        # Código responsavel por impedir input inválido
        while option != (1, 0):
            option = int(input("DIGITE UM NÚMERO VÁLIDO! (1 OU 0)\n> "))
            if option == 1:
                consultar_bolsa_ano()
            elif option == 0:
                interface_inicial()


# top 3 maiores e menores bolsas
def ranking_bolsas():
    # Limpa a tela
    clear()
    # Interface gráfica
    print(52 * "#")
    print("================RANKING DAS BOLSAS==================\n")
    print("TOP 3 MAIORES BOLSAS:\n")
    # Organiza a lista pelo maiores valores e pega os primeiros 3
    lista_top3 = df.sort_values("VL_BOLSISTA_PAGAMENTO", ascending=False)
    print(lista_top3[["NM_BOLSISTA", "CD_MOEDA", "VL_BOLSISTA_PAGAMENTO"]][0:3])
    print("\n")
    print("TOP 3 MENORES BOLSAS:\n")
    # Oraganiza a lista pelos menores valores e pega os 3 menores
    lista_botton3 = df.sort_values("VL_BOLSISTA_PAGAMENTO")
    print(lista_botton3[["NM_BOLSISTA", "CD_MOEDA", "VL_BOLSISTA_PAGAMENTO"]][0:3])
    # Tentar de novo ou voltar ao menu principal
    print(52 * "#")
    option = int(input("Digite 1 pra tentar de novo ou 0 pra voltar ao menu principal\n> "))
    if option == 1:
        # Chamar função de novo
        ranking_bolsas()
    elif option == 0:
        # Voltar ao menu principal
        interface_inicial()
    else:
        # Código responsavel por impedir input inválido
        while option != (1, 0):
            option = int(input("DIGITE UM NÚMERO VÁLIDO! (1 OU 0)\n> "))
            if option == 1:
                consultar_bolsa_ano()
            elif option == 0:
                interface_inicial()


# Função inicial principal
interface_inicial()
