#!/var/lib/asterisk/agi-bin/ura-api/venv/bin/python


if __name__ == '__main__':
    from providers.agi_provider import Agi
    from providers.cliente_provider import ClienteProvider
    from controller import Controller

    agi = Agi()
    cliente_provider = ClienteProvider()
    controller = Controller(agi, cliente_provider)
    controller.iniciar()