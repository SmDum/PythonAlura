from Curso2.restaurantes import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
retaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

retaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    