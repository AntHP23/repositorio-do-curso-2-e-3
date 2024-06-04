"""
Control f faz com que você consiga alterar diretamente uma palavra no arquivo 
exemplo se ali ta Restaurante da para trocar toda a classe ou aonde tudo é sitado por bolacha 
mas dai tem que ver tudo o resto do arquivo para ver se ta rodando direito
"""


class Restaurante:

    restaurantes = []
     #O self é uma conveção poderia ser trocado por qualquer outra palavra mas todos optam por usar ele
    def __init__(self, nome, categoria):
        #se colocar _nome.title() a primeira letra ira ficar em maiusculo isso é uma padronização
        #se colocar _nome.upper() todas as letras ficaram em maiusculo
        self._nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)



    def __str__(self):
        # O | significa uma união de conjuntos mas tambem pode ser usado para declarar se é uma coisa ou outra tipo uma pergunta com duas respostas
        return f'{self._nome} | {self.categoria}'


    @classmethod
    def lista_restaurantes(cls):
        print(f'{"nome do restaurante".ljust(20)} | {"categoria do restaurante".ljust(25)} | {"status do restaurante".ljust(20)}')
          #para cada restuarante na lista de restaurantes
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(20)}')
    # esse comando pode ser usado como um "embelezador" de codigo colocando emogi 
    @property
    def ativo(self):
        #retrone se ele for ativo se ele for "☑" se não "☐" se for verdadeiro ele vai mostrar o quadrado com V se for falso ficara vazio
        return '☑' if self._ativo else "☐"

    def ativa_desativa_restaurante(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante ('Praça' , 'Gourmet')
restaurante_praca.ativa_desativa_restaurante()
restaurante_pizza = Restaurante ('Pizza Express', 'Italiana')

Restaurante.lista_restaurantes()