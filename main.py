import FindPal as FP
PA = "palabras.txt"

FR = "frases.txt"

archivo = open(PA, 'r')

palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []

print("Lista de palabras: \n", palabras)
archivo = open(FR, 'r')

frases = []
for frase in archivo:
    frases.append(frase.strip())
    for palabra in palabras:
        palabras[palabra].append(frase.lower().count(palabra))
archivo.close()

print("Frases: \n", frases)
print("Palabras en frases: \n",palabras)
