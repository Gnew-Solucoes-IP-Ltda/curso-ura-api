class ServicoStatus:

    def __init__(self, nome: str):
        self.nome = nome


class Servico:

    def __init__(self, nome: str, status: str):
        self.nome = nome
        self.status = ServicoStatus(status)