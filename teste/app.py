
from modelo.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('mexican food', 'Mexicano')
restaurante_pumo = Restaurante('il pumo', 'Italiano')

def main():

    Restaurante.lista_restaurantes()


if __name__ == '__main__':
    main()