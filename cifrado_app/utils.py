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

def preparar_texto(texto):
    texto = texto.upper().replace('J', 'I')
    texto = ''.join([c for c in texto if c in string.ascii_uppercase])
    resultado = ''
    i = 0
    while i < len(texto):
        a = texto[i]
        b = ''
        if i + 1 < len(texto):
            b = texto[i + 1]
        else:
            b = 'X'
        if a == b:
            resultado += a + 'X'
            i += 1
        else:
            resultado += a + b
            i += 2
    if len(resultado) % 2 != 0:
        resultado += 'X'
    return resultado

