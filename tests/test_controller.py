from unittest import TestCase
from unittest.mock import MagicMock
from controller import Controller
from providers.cliente_provider import ClienteProvider


class ControllerTestCase(TestCase):

    def test_obter_cliente(self):
        provider = ClienteProvider()
        agi = MagicMock()
        agi.prompt_obter_documento.return_value = "27411078905"
        controller = Controller(agi, provider)
        cliente = controller.obter_cliente()
        self.assertEqual(cliente.documento, "27411078905")
        self.assertEqual(cliente.telefone, "8436751857")
        agi.prompt_obter_documento.return_value = '38891276065'
        cliente = controller.obter_cliente()
        self.assertIsNone(cliente)
        agi.prompt_obter_documento.return_value = "12345678900"
        self.assertRaises(Exception, controller.obter_cliente)
        self.assertEqual(controller._tentativa, 3)

    def test_obter_documento(self):
        provider = MagicMock()
        agi = MagicMock()
        agi.prompt_obter_documento.return_value = "12345678900"
        controller = Controller(agi, provider)
        self.assertRaises(ValueError, controller.obter_documento)
        agi.prompt_obter_documento.return_value = '38891276065'
        documento_informado = controller.obter_documento()
        self.assertEqual(documento_informado, '38891276065')