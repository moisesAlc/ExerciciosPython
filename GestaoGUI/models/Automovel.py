class Automovel:
    def __init__(self, nome: str, marca: str, ano: int, cor: str):
        self.nome = nome,
        self.marca = marca,
        self.ano = ano,
        self.cor = cor
        self.numero = 123,  # @todo
        self.alugado = False

    def muda_cor(self, cor):
        self.cor = cor

    def aluga_carro(self):
        self.alugado = True

    def libera_carro(self):
        self.alugado = False

