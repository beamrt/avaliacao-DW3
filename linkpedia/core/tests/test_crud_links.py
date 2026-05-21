from django.test import TestCase
from django.urls import reverse 
from django.contrib.auth.models import User

from core.models import LinkModel

class ListaLinksTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='aluno',
            email='aluno@cps.sp.gov.br',
            password='fatec'
        )
    
    def test_usuario_logado_acessa_listagem(self):

        self.client.login(
            username='aluno',
            password='fatec'
        )
    
        response = self.client.get(
        reverse('listar_links')
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'listar.html'
        )