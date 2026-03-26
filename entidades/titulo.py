from datetime import date

class Titulo:

    def __init__(self, codigo_barras: int, valor: float, data_vencimento: date):
        self.codigo_barras = codigo_barras
        self.valor = valor
        self.data_vencimento = data_vencimento