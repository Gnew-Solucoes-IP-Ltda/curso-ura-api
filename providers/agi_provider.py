from abc import ABC, abstractmethod
from asterisk.agi import AGI


class AgiAbstract(ABC):
    @abstractmethod
    def prompt_obter_documento(self) -> str:
        pass

    @abstractmethod
    def prompt_menu_principal(self) -> str:
        pass
    
    @abstractmethod
    def reproduzir_mensagem_boleto(self, codigo_barras: str) -> None:
        pass

    @abstractmethod
    def reproduzir_mensagem_massiva(self) -> None:
        pass

    @abstractmethod
    def direcionar_para_atendimento(self) -> None:
        pass

    @abstractmethod
    def direcionar_para_suporte(self) -> None:
        pass

    @abstractmethod
    def desligar(self) -> None:
        pass


class Agi(AgiAbstract):

    def __init__(self) -> None:
        self._agi = AGI()
        self._caminho_arquivos_audios = '/var/lib/asterisk/agi-bin/ura-api/audios/'

    def prompt_obter_documento(self) -> str:
        audio = 'saudacao_inicial'
        return self._executar_prompt(audio)
    
    def prompt_menu_principal(self) -> str:
        audio = 'menu_principal'
        return self._executar_prompt(audio)

    def reproduzir_mensagem_boleto(self, codigo_barras: str) -> None:
        audio = 'mensagem_boleto'
        self._reproduzir_mensagem(audio)
        self._agi.say_digits(codigo_barras)
        self._reproduzir_mensagem('obrigado')
        self.desligar()
    
    def reproduzir_mensagem_massiva(self) -> None:
        audio = 'mensagem_massiva'
        self._reproduzir_mensagem(audio)
        self.desligar()
    
    def direcionar_para_atendimento(self) -> None:
        audio = 'nao_localizamos_cadastro'
        self._reproduzir_mensagem(audio)
        self._goto('from-internal,atendimento,1')

    def direcionar_para_suporte(self) -> None:
        audio = 'mensagem_transferencia'
        self._reproduzir_mensagem(audio)
        self._goto('from-internal,suporte,1')

    def desligar(self) -> None:
        self._agi.hangup()

    def _executar_prompt(self, audio: str) -> str:
        timeout = 3000
        quantidade_maxima_digitos = 20
        digitos_recebidos = self._agi.get_data(
            f'{self._caminho_arquivos_audios}{audio}',
            timeout,
            quantidade_maxima_digitos
        )
        return digitos_recebidos

    def _reproduzir_mensagem(self, audio: str) -> None:
        self._agi.stream_file(f'{self._caminho_arquivos_audios}{audio}')
    
    def _goto(self, destino: str) -> None:
        self._agi.app_exec('GoTo', destino)