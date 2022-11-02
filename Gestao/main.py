import os
import time
from sys import platform

""" Variável em contexto global que armazenará os dados dos veículos """
veiculos = (
    {
        "numero": 1,
        "nome": "Ford Mustang GT",
        "marca": "Ford",
        "ano": "2015",
        "alugado": False,
        "cor": "branco"
    },
    {
        "numero": 2,
        "nome": "Hyundai Tiburon GT V6",
        "marca": "Hyundai",
        "ano": "2016",
        "alugado": False,
        "cor": "cinza",
    },
    {
        "numero": 3,
        "nome": "Lamborghini Murciélago",
        "marca": "Lamborghini",
        "ano": "2017",
        "alugado": False,
        "cor": "preto",
    },
    {
        "numero": 4,
        "nome": "Nissan 350Z",
        "marca": "Nissan",
        "ano": "2018",
        "alugado": False,
        "cor": "verde perolado",
    }
)

""" imprime um texto e uma formatação de acordo com argumentos """
def print_personalizado(texto, formato):

    """ contém um dict com nomes de cores e os respectivos códigos """
    dict_cores = {
        "roxo": "\033[95m",
        "azul": "\033[94m",
        "ciano": "\033[96m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "vermelho": "\033[91m",
        "negrito": "\033[1m",
        "sublinhado": "\033[4m",
        "fonte_padrao": "\033[0m",
    }

    if formato in dict_cores:
        print(dict_cores[formato] + texto + dict_cores["fonte_padrao"])
    else:
        print(texto)


def limpa_tela():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def aguarda_tecla():
    print_personalizado('\nAperte qualquer tecla para continuar.', 'roxo')
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


def mostra_veiculo(veiculo):
    print(
        f'''
=============================Veículo================================    
    Nº {veiculo["numero"]} - {veiculo["nome"]}, {veiculo["marca"]}, {veiculo["ano"]} - {"Alugado" if veiculo["alugado"] else "Disponível para alugar"} 
====================================================================
''')


def ver_veiculos():
    opcao = input(f'Você deseja ver (t)odos os {len(veiculos)} veículos ou um (v)eículo específico? ')
    print()
    if opcao == 't':
        for num_veiculo, veiculo in enumerate(veiculos, start=1):
            mostra_veiculo(veiculo)
            time.sleep(0.4)
        aguarda_tecla()

    elif opcao == 'v':
        opcao_procura = int(input('''Você quer procurar por:
        1) Por número
        2) Por marca
        3) Por ano
        4) Alugados
        5) Não alugados
        
        '''))

        opcao_valor = int(input('Digite o valor para a busca: '))

        if opcao_procura == 1:
            limpa_tela()
            for veiculo in filter(lambda v: veiculos.index(v) == opcao_valor - 1, veiculos):
                mostra_veiculo(veiculo)
            aguarda_tecla()
        elif opcao_procura == 2:
            limpa_tela()
            for veiculo in filter(lambda v: v["marca"] == veiculo["marca"], veiculos):
                mostra_veiculo(veiculo)
            aguarda_tecla()


def adicionar_veiculo():
    global veiculos
    limpa_tela()
    print('Adicionar veículo:')
    nome_veiculo = input('Qual é o nome? ')
    marca_veiculo = input('Qual é a marca? ')
    ano_veiculo = int(input('Qual é o ano? '))
    veiculo = {
        "nome": nome_veiculo,
        "marca": marca_veiculo,
        "ano": ano_veiculo,
        "alugado": False
    }
    # @todo aqui fazer testes com os valores inseridos...
    veiculos = veiculos + (veiculo,)


def editar_veiculo():
    global veiculos
    limpa_tela()
    qtd_veiculos = len(veiculos)
    numero_inserido = int(input('Qual o número do veículo que deseja editar? '))
    if qtd_veiculos - 1 > numero_inserido or numero_inserido < 1:
        print_personalizado(f'Digite um número válido, de 1 a {qtd_veiculos}', 'vermelho')
    else:
        veiculo_a_editar = veiculos[numero_inserido - 1]
        mostra_veiculo(veiculo_a_editar)
        aspecto_a_editar = int(input("Qual aspecto deseja editar?\n1 - Disponibilidade, 2 - cor, 3 - Desistir "))
        if aspecto_a_editar == 1:
            escolha = input(f'o veículo está {"Alugado" if veiculo_a_editar["alugado"] else "Disponível para alugar"}. Deseja mudar o status? s/n ')
            if escolha == 's':
                veiculo_a_editar["alugado"] = not veiculo_a_editar["alugado"]
                mostra_veiculo(veiculo_a_editar)
                print_personalizado('Modificação realizada.', 'verde')
                aguarda_tecla()
        elif aspecto_a_editar == 2:
            veiculo_a_editar["cor"] = input(f'o veículo está com a cor {veiculo_a_editar["cor"]}. Digite a nova cor: ')
            mostra_veiculo(veiculo_a_editar)
            print_personalizado('Modificação realizada.', 'verde')
            aguarda_tecla()
        else:
            print_personalizado('Saindo...', 'amarelo')

def remover_veiculo():
    global veiculos
    veiculos_lista_temp = list(veiculos)
    limpa_tela()
    numero_veiculo_a_remover = int(input("Qual o número do veículo que deseja remover? "))
    for veiculo in veiculos:
        if veiculo["numero"] == numero_veiculo_a_remover:
            mostra_veiculo(veiculo)
            confirmacao = input("Este é o veículo que deseja remover? s/n ")
            if confirmacao == 's':
                veiculos_lista_temp.remove(veiculo)
                print_personalizado("Veículo removido.", "verde")
    veiculos = tuple(veiculos_lista_temp)

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
            editar_veiculo()
        elif opcao == 4:
            remover_veiculo()
        elif opcao == 5:
            limpa_tela()
            print('Saindo do sistema...')
            aguarda_tecla()
            exit()
        else:
            print_personalizado('Código incorreto.', 'vermelho')
            aguarda_tecla()


if __name__ == '__main__':
    loop_inicial()
