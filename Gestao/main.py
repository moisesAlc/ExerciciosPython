import os
import time
from sys import platform


def print_personalizado(texto, tipo):
    dict_cores = {
        "roxo": "\033[95m",
        "azul": "\033[94m",
        "ciano": "\033[96m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "vermelho": "\033[91m",
        "negrito": "\033[1m",
        "sublinhado": "\033[4m",
        "padrão": "\033[0m",
    }
    if tipo in dict_cores:
        print(dict_cores[tipo] + texto + dict_cores["padrão"])
    else:
        print(texto)


veiculos = (
    {
        "nome": "Ford Mustang GT",
        "marca": "Ford",
        "ano": "2015",
        "alugado": False,
    },
    {
        "nome": "Hyundai Tiburon GT V6",
        "marca": "Hyundai",
        "ano": "2016",
        "alugado": False,
    },
    {
        "nome": "Lamborghini Murciélago",
        "marca": "Lamborghini",
        "ano": "2017",
        "alugado": False,
    },
    {
        "nome": "Nissan 350Z",
        "marca": "Nissan",
        "ano": "2018",
        "alugado": False,
    }
)


def limpa_tela():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def aguarda_tecla():
    print('\nAperte qualquer tecla para continuar.')
    input()


def mostra_tela_inicial():
    print('''
    Sistema de Aluguel de Veículos
    O que deseja fazer?
    1) Ver veículo(s)
    2) Adicionar veículo
    3) Editar veículo
    4) Remover veículo
    5) Sair
    ''')


def mostra_veiculo(veiculo, numero):
    print(
        f'''
=============================Veículo================================    
    Nº {numero} - {veiculo["marca"]}, {veiculo["ano"]} - {"Alugado" if veiculo["alugado"] else "Disponível para alugar"} 
====================================================================
''')


def ver_veiculos():
    opcao = input(f'Você deseja ver (t)odos os {len(veiculos)} veículos ou um (v)eículo específico? ')
    print()
    if opcao == 't':
        for num_veiculo, veiculo in enumerate(veiculos, start=1):
            mostra_veiculo(veiculo, num_veiculo)
            time.sleep(0.4)
        aguarda_tecla()

    elif opcao == 'v':
        opcao_procura = int(input('''Você quer procurar por:
        1) Por número(id)
        2) Por marca
        3) Por ano
        4) Alugados
        5) Não alugados
        
        '''))

        opcao_valor = int(input('Digite o valor para a busca: '))

        if opcao_procura == 1:
            limpa_tela()
            for veiculo in filter(lambda v: veiculos.index(v) == opcao_valor - 1, veiculos):
                mostra_veiculo(veiculo, veiculos.index(veiculo) + 1)
            aguarda_tecla()


def adicionar_veiculo():
    global veiculos
    limpa_tela()
    print('Adicionar veículo:')
    nome_veiculo = input('Qual é o nome? ')
    marca_veiculo = input('Qual é a marca? ')
    ano_veiculo = int(input('Qual é o ano?'))
    veiculo = {
        "nome": nome_veiculo,
        "marca": marca_veiculo,
        "ano": ano_veiculo,
        "alugado": False
    }
    # @todo aqui fazer testes com os valores inseridos...
    veiculos = veiculos + (veiculo,)


def loop_inicial():
    opcao = 0
    while opcao != 5:
        limpa_tela()
        mostra_tela_inicial()
        opcao = int(input())
        if opcao == 1:
            ver_veiculos()
        elif opcao == 2:
            adicionar_veiculo()
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            limpa_tela()
            print('Saindo do sistema...')
            aguarda_tecla()
            exit()
        else:
            print_personalizado('Código incorreto.', 'atenção')
            aguarda_tecla()


if __name__ == '__main__':
    #loop_inicial()
    print_personalizado("a", 'b')
