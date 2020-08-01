import random
import string
import os


def abrir_archivo(nombre, ruta):
    """Esta funcion Abre los archivo y comprueba los datos en ellos, para comprobar 
       que esten en el rango requerido """
    
    try:
        if ".txt" not in nombre:
            nombre += ".txt"
        archivo = open(nombre, 'r')
        try:
            dimension = archivo.readline()
            dimension = int(dimension.strip())
            if (dimension<1 or dimension > 26):
                dimension = random.randint(1, 26)
        except Exception as e:
            print(f'Erro al obtener dimension de tipo {e}')
            exit(0)
        try:
            dificultad = archivo.readline()
            dificultad = dificultad.strip()
        except Exception as e:
            print(f'Erro al obtener la Dificultad de tipo {e}')
            exit(0)
        archivo.close()
    except:
        print(f'Erro al obtener el archivo, de tipo {e}')
        exit(0)

    return dimension, dificultad


def calcula_minas(dimension, dificultad):
    """Realiza el calculo del numero de minas en el tablero"""

    if dificultad.lower() == 'f':
        porcentaje = 0.1
    elif dificultad.lower() == 'm':
        porcentaje = 0.15
    elif dificultad.lower() == 'd':
        porcentaje = 0.2
    elif dificultad.lower() == 'd':
        porcentaje = 0.3

    numero_minas = int((dimension ** 2) * porcentaje)

    return numero_minas

def crear_tablero(letras, dimension):
    tablero = dict()
    for letra in letras:
        tablero[letra] = list()
        for i in range(dimension):
            tablero[letra].append('.')
    return tablero


def imprime_tablero(tablero, dimension):
    # Impresión del tablero
    for i in range(dimension + 1):
        if i == 0:
            print(end='  ')
        else:
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')

    print(end='\n')

    for llave, valor in tablero.items():
        cadena = llave
        for v in valor:
            cadena += '  ' + v
        print(cadena)


def ubicar_minas(numero_minas, tablero, dimension):
    posiciones = list()
    minas = set()
    for key in tablero.keys():
        for i in range(dimension):
            posiciones.append(f'{key}{i + 1}')
    for i in range(numero_minas):
        mina = random.choice(posiciones)
        while mina in minas:
            mina = random.choice(posiciones)
        minas.add(mina)
    return minas, posiciones


def crea_tablero(tablero, dimension):
    posiciones = list()
    for key in tablero.keys():
        for i in range(dimension):
            posiciones.append(f'{key}{i + 1}')

    return posiciones


def menu():
    return input('Escoge una opción: (1) Generar tablero (2) Cargar tablero (3) Salir : ')


def ingresa_posicion(posiciones_tablero):
    while True:
        posicion = input('Ingrese la casilla del tablero que quiere abrir: ').upper()
        if posicion in posiciones_tablero:
            break
        else:
            imprime_tablero(tablero, dimension)
            print(' ')
    return posicion


def comprueba_jugada(tablero, minas, posicion, letras):
    """ Esta funcion Realiza la comprobacion sobre el tablero de la posicion jugada,
        es decir nos indicara el numero de minas en el perimetro de la posicion jugada,
        o en caso de seleccionar la posicion de la mina, muestra todas las minas, para 
        finalizar el juego
        
        Tablero -> diccionario"""
        
    letra = posicion[0]
    numero = int(posicion[1:])
    if posicion in minas:
        for mina in minas:
            tablero[mina[0]][int(mina[1]) - 1] = '*'
    else:
        alrededor = 0
        indice = letras.index(letra)
        # Misma fila
        try:
            if f'{letra}{numero - 1}' in minas:
                alrededor += 1
        except:
            pass
        try:
            if f'{letra}{numero + 1}' in minas:
                alrededor += 1
        except:
            pass
        # Fila de arriba
        try:
            if indice > 0:
                if f'{letras[indice - 1]}{numero}' in minas:
                    alrededor += 1
        except:
            pass
        try:
            if indice > 0:
                if f'{letras[indice - 1]}{numero + 1}' in minas:
                    alrededor += 1
        except:
            pass
        try:
            if indice > 0:
                if f'{letras[indice - 1]}{numero - 1}' in minas:
                    alrededor += 1
        except:
            pass
        # Fila de abajo
        try:
            if f'{letras[indice + 1]}{numero}' in minas:
                alrededor += 1
        except:
            pass
        try:
            if f'{letras[indice + 1]}{numero + 1}' in minas:
                alrededor += 1
        except:
            pass
        try:
            if f'{letras[indice + 1]}{numero - 1}' in minas:
                alrededor += 1
        except:
            pass
        tablero[letra][numero - 1] = str(alrededor)
    return tablero


def cambio(diccionario):
    for key in diccionario.keys():
        for i, element in enumerate(diccionario[key]):
            if element == '.':
                diccionario[key][i] = '*'
    return diccionario


def comprueba_tablero(tablero, minas, dimension):
    for key in tablero.keys():
        if '*' in tablero[key]:
            imprime_tablero(tablero, dimension)
            print('PERDISTE')
            return True
    contador = 0
    for key in tablero.keys():
        contador += tablero[key].count('.')
    if contador == len(minas):
        tablero = cambio(tablero)
        imprime_tablero(tablero, dimension)
        print('GANASTE')
        return True
    return False


def guarda_tablero(nombre, ruta, dimension, minas):
    try:
        archivo = open(f'{nombre}', 'w')
        archivo.write(f'{dimension}\n')
    except:
        print("Error al crear el archivo de salida")
    for mina in minas:
        archivo.write(f'{mina}\n')
    archivo.close()


ruta = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(ruta, 'archivos')

while True:
    opcion = menu()
    try:
        opcion = int(opcion)
    except:
        opcion = 0
    if opcion == 1:
        nombre = input('Ingrese el nombre del archivo: ')
        nombre_sin_extension = nombre.split('.')[0]

        dimension, dificultad = abrir_archivo(nombre, ruta)
        numero_minas = calcula_minas(dimension, dificultad)
        letras = string.ascii_uppercase[:dimension]
        tablero = crear_tablero(letras, dimension)
        posicion_minas, posiciones_tablero = ubicar_minas(numero_minas, tablero, dimension)
        print(posicion_minas)
        guarda_tablero(f'{nombre_sin_extension}.sal', ruta, dimension, posicion_minas)

        print(" ")

    elif opcion == 2:
        while True:
            nombre = input('Ingrese el nombre del archivo: ')
            nombre_sin_extension = nombre.split('.')[0]
            ganador = False
            try:
                archivo = open(f'{nombre_sin_extension}.sal', 'r')
                tablero = archivo.readlines()
                archivo.close()
                break
            except:
                pass

        dimension = int(tablero[0].strip())
        aux = tablero[1:]
        minas = list()

        for mina in aux:
            minas.append(mina.strip())

        letras = string.ascii_uppercase[:dimension]
        tablero = crear_tablero(letras, dimension)
        contador = 0
        while True:
            imprime_tablero(tablero, dimension)

            posiciones = crea_tablero(tablero, dimension)

            posicion_jugada = ingresa_posicion(posiciones)
            tablero = comprueba_jugada(tablero, minas, posicion_jugada, letras)

            if comprueba_tablero(tablero, minas, dimension):
                break
    elif opcion == 3:
        break
    else:
        print(' ')