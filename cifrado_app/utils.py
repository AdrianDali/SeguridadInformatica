import string


def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            num = ord(caracter)
            num += desplazamiento
            if caracter.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif caracter.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            resultado += chr(num)
        else:
            resultado += caracter
    return resultado

def cifrado_vigenere(mensaje, clave):
    resultado = ""
    indice_clave = 0
    clave = clave.lower()
    for caracter in mensaje:
        if caracter.isalpha():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('a')
            if caracter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            num = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(num)
            indice_clave += 1
        else:
            resultado += caracter
    return resultado

def descifrado_vigenere(mensaje, clave):
    resultado = ""
    indice_clave = 0
    clave = clave.lower()
    for caracter in mensaje:
        if caracter.isalpha():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord('a')
            if caracter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            num = (ord(caracter) - base - desplazamiento) % 26 + base
            resultado += chr(num)
            indice_clave += 1
        else:
            resultado += caracter
    return resultado


def generar_matriz_clave(clave):
    clave = clave.upper().replace('J', 'I')
    matriz = []
    letras_usadas = set()
    for c in clave:
        if c not in letras_usadas and c in string.ascii_uppercase:
            matriz.append(c)
            letras_usadas.add(c)
    for c in string.ascii_uppercase:
        if c not in letras_usadas and c != 'J':
            matriz.append(c)
            letras_usadas.add(c)
    return [matriz[i:i+5] for i in range(0, 25, 5)]

def buscar_posicion(matriz, letra):
    for i, fila in enumerate(matriz):
        for j, c in enumerate(fila):
            if c == letra:
                return i, j
    return None


############################################################3
def generar_matriz_playfair(clave):
    # Convertir la clave a mayúsculas
    clave = clave.upper()
    # Eliminar duplicados manteniendo el orden
    clave_sin_duplicados = ''.join(sorted(set(clave), key=clave.index))
    # Crear una lista de letras del alfabeto sin la letra 'J'
    alfabeto = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) != 'J'])
    # Combinar la clave y el alfabeto, eliminando duplicados
    letras_unicas = clave_sin_duplicados + ''.join([c for c in alfabeto if c not in clave_sin_duplicados])
    # Crear la matriz de 5x5
    matriz_final = [list(letras_unicas[i:i+5]) for i in range(0, 25, 5)]
    return matriz_final

def preparar_texto_playfair(texto):
    texto = texto.upper().replace('J', 'I')
    texto = ''.join([c for c in texto if c.isalpha()])
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = ''
        if (i + 1) < len(texto):
            b = texto[i + 1]
        if a != b:
            pares.append(a + (b if b else 'X'))
            i += 2
        else:
            pares.append(a + 'X')
            i += 1
    if len(pares[-1]) == 1:
        pares[-1] += 'X'
    return pares

def encontrar_posicion(matriz, letra):
    for row_idx, row in enumerate(matriz):
        if letra in row:
            return row_idx, row.index(letra)
    return None, None

def cifrar_playfair(mensaje, clave):
    matriz = generar_matriz_playfair(clave)
    pares = preparar_texto_playfair(mensaje)
    resultado = ''
    for par in pares:
        fila1, col1 = encontrar_posicion(matriz, par[0])
        fila2, col2 = encontrar_posicion(matriz, par[1])
        if fila1 == fila2:
            resultado += matriz[fila1][(col1 + 1) % 5]
            resultado += matriz[fila2][(col2 + 1) % 5]
        elif col1 == col2:
            resultado += matriz[(fila1 + 1) % 5][col1]
            resultado += matriz[(fila2 + 1) % 5][col2]
        else:
            resultado += matriz[fila1][col2]
            resultado += matriz[fila2][col1]
    return resultado

def descifrar_playfair(mensaje, clave):
    matriz = generar_matriz_playfair(clave)
    pares = [mensaje[i:i+2] for i in range(0, len(mensaje), 2)]
    resultado = ''
    for par in pares:
        fila1, col1 = encontrar_posicion(matriz, par[0])
        fila2, col2 = encontrar_posicion(matriz, par[1])
        if fila1 == fila2:
            resultado += matriz[fila1][(col1 - 1) % 5]
            resultado += matriz[fila2][(col2 - 1) % 5]
        elif col1 == col2:
            resultado += matriz[(fila1 - 1) % 5][col1]
            resultado += matriz[(fila2 - 1) % 5][col2]
        else:
            resultado += matriz[fila1][col2]
            resultado += matriz[fila2][col1]
    return resultado