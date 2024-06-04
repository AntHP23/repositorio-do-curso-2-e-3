from abc import ABC, abstractmethold



class ItemCardapio:
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    @abstractmethold
    def aplicar_desconto(self):
        pass