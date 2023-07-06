import random

def obtener_palabra_aleatoria():
    palabras = [
        ('python', 'Es un lenguaje de programación popular y poderoso.'),
        ('programacion', 'Es el proceso de diseñar, codificar, depurar y mantener el código fuente de un programa de computadora.'),
        ('desarrollo', 'Es el proceso de crear, diseñar y mantener aplicaciones, sistemas o software.'),
        ('computadora', 'Es una máquina electrónica que recibe y procesa datos para convertirlos en información útil.'),
        ('juego', 'Es una actividad recreativa que se lleva a cabo con reglas y tiene como objetivo proporcionar entretenimiento.'),
        ('perro', 'Es un animal doméstico que suele ser leal y fiel.'),
        ('gato', 'Es un animal doméstico de pequeño tamaño, de comportamiento independiente y cazador.'),
        ('casa', 'Es una edificación utilizada como vivienda.'),
        ('libro', 'Es un conjunto de hojas de papel u otro material con un texto impreso, encuadernadas.'),
        ('comida', 'Es cualquier sustancia que se consume para proporcionar nutrientes y energía al cuerpo.')
        # Agrega más palabras comunes aquí
    ]
    return random.choice(palabras)

def mostrar_ahorcado(intentos):
    estados_ahorcado = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ===
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
          ===
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
          ===
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
          ===
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ===
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
          ===
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
          ===
        '''
    ]
    print(estados_ahorcado[intentos])

def jugar_ahorcado():
    palabra, pista = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        # Mostrar el estado actual del ahorcado
        mostrar_ahorcado(intentos)

        # Mostrar la palabra oculta
        palabra_mostrada = ''
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += '_ '

        print('Palabra:', palabra_mostrada)
        print('Pista:', pista)
        print('Intentos restantes:', intentos)

        # Solicitar al jugador que ingrese una letra o una palabra
        entrada = input('Ingresa una letra o una palabra: ').lower()

        if entrada in letras_adivinadas:
            print('Ya has ingresado esa letra o palabra. ¡Intenta con otra!\n')
            continue

        if len(entrada) == 1:
            letras_adivinadas.append(entrada)
            if entrada not in palabra:
                intentos -= 1
                print('¡Letra incorrecta!\n')
        else:
            for letra in entrada:
                if letra in palabra:
                    letras_adivinadas.append(letra)
                else:
                    intentos -= 1
            if len(letras_adivinadas) == len(palabra):
                print('¡Felicidades! ¡Has adivinado la palabra!')
                print('La palabra era:', palabra)
                return
            elif intentos == 0:
                break
            else:
                print('¡Palabra incorrecta!\n')

        # Verificar si el jugador ha adivinado todas las letras
        if all(letra in letras_adivinadas for letra in palabra):
            print('¡Felicidades! ¡Has adivinado la palabra!')
            print('La palabra era:', palabra)
            return

    mostrar_ahorcado(intentos)
    print('¡Oh no! Te has quedado sin intentos.')
    print('La palabra era:', palabra)

jugar_ahorcado()