import random
from palabras import palabras
from figuras import figuras

def palabra_secreta():
    indice = random.randint(0,len(palabras) - 1)
    return palabras[indice]

def visual(palabra_buscar, oportunidades):
        if oportunidades > 0:
            encabezado()
        print(figuras[oportunidades])
        print('')
        print(palabra_buscar)
        print('\n----------------------------------------------')

def iniciar_juego():
    palabra = palabra_secreta()
    palabra_buscar = ['-'] * len(palabra)
    oportunidades = 0
    while True:
        visual(palabra_buscar, oportunidades)
        letra_ingresada = str(input('Ingresa una letra: '))
        letras_escritas = []

        for i in range(len(palabra)):
            if palabra[i] == letra_ingresada:
                letras_escritas.append(i)

        if len(letras_escritas) == 0:
            oportunidades += 1

            if oportunidades == 7:
                visual(palabra_buscar, oportunidades)
                print('')
                print(f'Lo siento {self.nombre} has perdido la palabra era : {palabra}')
                break
            else:
                for i in letras_escritas:
                    palabra_buscar[i]= letra_ingresada
                    letras_escritas = []

            try:
                palabra_buscar.index('-')
            except ValueError: #De preferencia se dice que tipo de error es el que se espera recibir
                print('')
                print(f'Felicidades,has adivinado la palabra {palabra}!')
                break

def encabezado():
    print('=================================')
    print('======JUEGO DEL AHORCADO=========')
    print('A D I V I N A la palabra secreta')
    print('(Palabras relacionadas al taller)')
    print('=================================')

encabezado()
iniciar_juego()


