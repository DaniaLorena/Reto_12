

with open ("mbox.txt") as file_object:
    leer = file_object.read()

def num_vocales (leer):
    num_vocales : int = 0
    vocales = "aeiouáéíóúAEIOU"
    for letra in leer:
        if letra in vocales:
            num_vocales +=1
    print (num_vocales)


def num_consonantes (leer):
    num_consonantes : int = 0
    consonante :str ="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    for letra in leer:
        if letra in consonante:
            num_consonantes+=1
    print (num_consonantes)


def palabras_repetidas(leer: str)-> list:
    #Se quitan los caracteres no deseados   
    caracteres_no_deseados : list = ['.', ',', ';', ':', '!', '?', '"', '(', ')', '[', ']', '{', '}', '-', '_', '“', '”', '\n', '\r', '\t']
    for caracter in caracteres_no_deseados:
        leer = leer.replace(caracter, ' ')

    #Se dividen las palabras
    palabras = leer.split()

    #Se cuenta la frecuencia de las palabras
    frecuencia_palabras : dict = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    #Se ordenan las palabras por su frecuencia
    palabras_ordenadas = sorted(frecuencia_palabras.items(), key=lambda item: item[1], reverse=True)

    #Se separan las 50 palabras más repetidas
    palabras_50 = []
    for i in range (50):
        palabras_50 += palabras_ordenadas[i]

    print (palabras_50)

num_vocales (leer)
num_consonantes (leer)
palabras_repetidas (leer)