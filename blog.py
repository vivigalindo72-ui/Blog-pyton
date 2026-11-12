# Blog-pyton - Generador de parrafos con IA
# Creado por Luz 

def generar_parrafo(tema):
    base = f"The meaning of {tema} is a question that has been asked by people throughout history. There are a number of different interpretations of what this means."
    return base

while True:
    r = input("Write a paragraph? Y for yes, anything else for no. ")
    if r.lower() != "y":
        break
    tema = input("What should this paragraph talk about? ")
    print("")
    print(generar_parrafo(tema))
    print("")
