
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
