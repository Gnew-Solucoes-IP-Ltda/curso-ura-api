from validate_docbr import CPF
from entidades.cliente import Cliente
from providers.cliente_provider import ClienteProvider
from providers.agi_provider import AgiAbstract


class Controller:

    def __init__(self, agi: AgiAbstract, cliente_provider: ClienteProvider) -> None:
        self.agi = agi
        self._provider = cliente_provider
        self._tentativa = 0
    
    def iniciar(self) -> None:

        try:
            cliente = self.obter_cliente()

            if not cliente:
                self.agi.direcionar_para_atendimento()
            
            opcao = self.obter_opcao_menu_principal()

            if opcao == '1':
                servico = self._provider.obter_servico(cliente)

                if servico.status.nome == 'MASSIVA':
                    self.agi.reproduzir_mensagem_massiva()
                    self.agi.desligar()
                
                self.agi.direcionar_para_suporte()

            elif opcao == '2':
                titulo = self._provider.obter_titulo(cliente)
                self.agi.reproduzir_mensagem_boleto(titulo.codigo_barras)
                self.agi.desligar()
            
            else:
                self.agi.direcionar_para_atendimento()
        
        except:        
            self.agi.direcionar_para_atendimento()
        
    def obter_cliente(self) -> Cliente:
        numero_maximo_tentativas = 3
        self._tentativa = 0
        documento = None

        while self._tentativa < numero_maximo_tentativas and documento is None:
            try:
                self._tentativa += 1
                documento = self.obter_documento()
                cliente = self._provider.obter_cliente(documento)
                return cliente
            
            except ValueError:
                ...
            
            except Exception:
                return None
            
        raise Exception('Número máximo de tentativas excedido')
    
    def obter_opcao_menu_principal(self) -> str:
        opcao = None
        tentativas = 3
        opcoes_validas = ['1', '2']

        while not opcao and tentativas > 0:
            tentativas -= 1
            opcao_informada = self.agi.prompt_menu_principal()

            if opcao_informada in opcoes_validas:
                opcao = opcao_informada
        
        return opcao

    def obter_documento(self) -> str:
        documento_informado = self.agi.prompt_obter_documento()
        self._verificar_documento_valido(documento_informado)
        return documento_informado

    def _verificar_documento_valido(self, documento: str) -> None: 
        cpf = CPF()

        if not cpf.validate(documento):
            raise ValueError("Documento inválido")