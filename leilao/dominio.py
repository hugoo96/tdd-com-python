from typing import List

from leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido("Não pode propor um lance com um valor maior que o da carteira")
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self) -> float:
        return self.__carteira

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.menor_lance = 0.0
        self.maior_lance = 0.0
        self.descricao = descricao
        self.__lances: List[Lance] = []

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise LanceInvalido("erro ao propor lance!!")


    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos!!")

    def _lance_maior_que_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O lance tem que ser maior que o anterior!!")

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and
                                          self._lance_maior_que_anterior(lance))
