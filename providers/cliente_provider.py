from entidades.cliente import Cliente
from entidades.servico import Servico
from entidades.titulo import Titulo


CLIENTES = {
    '27411078905': {
        'documento': '27411078905',
        'telefone': '8436751857'
    },
    '96354391564': {
        'documento': '96354391564',
        'telefone': '8436751857'
    },
    '54968493495': {
        'documento': '54968493495',
        'telefone': '11889988997'
    }
}
SERVICOS = {
    '27411078905': {
        'nome': 'COMBO A',
        'status': 'ATIVO'
    },
    '96354391564': {
        'nome': 'COMBO B',
        'status': 'ATIVO'
    },
    '54968493495': {
        'nome': 'COMBO C',
        'status': 'MASSIVA'
    }
}
TITULOS = {
    '27411078905': {
        'codigo_barras': 123456789,
        'valor': 300.00,
        'data_vencimento': '2026-02-28'
    },
    '96354391564': {
        'codigo_barras': 123456780,
        'valor': 150.00,
        'data_vencimento': '2026-02-28'
    },
    '54968493495': {
        'codigo_barras': 123456700,
        'valor': 100.00,
        'data_vencimento': '2026-02-28'
    }

}


class ClienteProvider:

    def obter_cliente(self, documento: str) -> Cliente:
        if documento not in CLIENTES:
            raise Exception('Cliente não encontrado')
    
        cliente = CLIENTES[documento]
        return Cliente(cliente['documento'], cliente['telefone'])
    
    def obter_servico(self, cliente: Cliente) -> Servico:
        if cliente.documento not in SERVICOS:
            raise Exception('Serviço não encontrado')
    
        servico = SERVICOS[cliente.documento]
        return Servico(servico['nome'], servico['status'])
    
    def obter_titulo(self, cliente: Cliente) -> Titulo:
        if cliente.documento not in TITULOS:
            raise Exception('Título não encontrado')
    
        titulo = TITULOS[cliente.documento]
        return Titulo(titulo['codigo_barras'], titulo['valor'], titulo['data_vencimento'])