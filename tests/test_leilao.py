from unittest import TestCase

from leilao.dominio import Usuario, Lance, Leilao
from leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.hugo = Usuario('Hugo', 500.0)
        self.lance_do_hugo = Lance(self.hugo, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        juliano = Usuario("Juliano", 500.0)
        lance_do_juliano = Lance(juliano, 100)

        self.leilao.propoe(lance_do_juliano)
        self.leilao.propoe(self.lance_do_hugo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        juliano = Usuario("Juliano", 500.0)
        lance_do_juliano = Lance(juliano, 100.0)

        self.leilao.propoe(lance_do_juliano)
        self.leilao.propoe(self.lance_do_hugo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        gui = Usuario('Gui', 500.0)

        lance = Lance(gui, 150.0)

        self.leilao.propoe(lance)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        gui = Usuario('Gui', 500.0)
        lance_do_gui = Lance(gui, 150.0)

        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        vini = Usuario('Vini', 500.0)
        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe(self.lance_do_hugo)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)

    # se o ultimo usuario for diferente, de permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):

        juliano = Usuario("Juliano", 500.0)
        lance_do_juliano = Lance(juliano, 100.0)
        self.leilao.propoe(lance_do_juliano)
        self.leilao.propoe(self.lance_do_hugo)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebidos)

    # se o ultimo usuario for o mesmo, não deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_hugo200 = Lance(self.hugo, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_hugo)
            self.leilao.propoe(lance_do_hugo200)


