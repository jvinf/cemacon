from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Jax Jones',
            'email': 'jaxjones@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Olá tudo bem?'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Jax Jones',
            'email': 'jaxjones@gmail.com',
            'mensagem': 'Olá tudo bem?'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)