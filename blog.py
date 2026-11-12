# Blog-pyton - Generador de blogs con IA
# Creado por Luz 
# Version original - Tema libre
import random

total_blogs = 0

def generar_blog(tema):
    inicios = [
        f"El tema de {tema} se ha vuelto muy relevante en los ultimos tiempos. Entenderlo nos ayuda a ver la realidad desde otra perspectiva.",
        f"Actualmente, hablar de {tema} es muy comun. Este asunto influye en muchos aspectos de nuestro dia a dia.",
        f"{tema} es un concepto que todos hemos escuchado alguna vez. Sin embargo, pocas veces nos detenemos a analizarlo a fondo."
    ]
    desarrollo = [
        f"Si analizamos {tema}, notamos que tiene varias caras. No solo afecta a nivel personal, sino tambien a nivel colectivo.",
        f"Uno de los puntos clave de {tema} es como ha ido evolucionando. Lo que antes parecia lejano, hoy es parte de nuestra rutina.",
        f"Es importante mencionar que {tema} no es algo aislado. Esta conectado con otros temas como la tecnologia, la cultura y la sociedad."
    ]
    ejemplos = [
        f"Por ejemplo, cuando vemos noticias sobre {tema}, podemos notar su presencia en nuestra ciudad, escuela o familia.",
        f"Un caso claro de {tema} es lo que pasa en internet todos los dias. Ahi se refleja como este tema nos rodea.",
        f"Pensemos en un ejemplo simple de {tema} en nuestra vida: cada vez que tomamos una decision, este tema aparece de alguna forma."
    ]
    consejos = [
        f"Si quieres saber mas de {tema}, te recomiendo buscar videos, leer articulos cortos y platicar con otras personas.",
        f"Para dominar {tema}, lo mejor es no quedarse con una sola opinion. Busca diferentes fuentes y compara ideas.",
        f"Mi consejo sobre {tema} es que lo veas con mente abierta y con ganas de aprender algo nuevo cada dia."
    ]
    cierres = [
        f"Para cerrar, {tema} es mucho mas que una palabra de moda. Es una oportunidad para crecer y aprender.",
        f"En definitiva, {tema} nos invita a reflexionar y a mejorar la forma en que vemos el mundo.",
        f"Al final, entender {tema} nos hace mas conscientes y preparados para lo que viene."
    ]

    texto = random.choice(inicios) + "\n\n"
    texto += random.choice(desarrollo) + "\n\n"
    texto += random.choice(ejemplos) + "\n\n"
    texto += random.choice(consejos) + "\n\n"
    texto += random.choice(cierres)
    return texto

def nuevo_blog():
    global total_blogs
    print("\n** GENERADOR DE BLOGS - LUZ **")
    print("Categorias: Tecnologia / Salud / Ecologia / Arte / Deportes")
    tema = input("Escribe de que tema quieres tu blog: ")
    resultado = generar_blog(tema)
    print("\n========== TU BLOG ==========\n")
    print(resultado)
    print("\n=============================\n")
    total_blogs += 1

while True:
    op = input("Generar blog? (Y = si): ")
    if op.lower() != "y":
        print(f"Bye Luz! Hiciste {total_blogs} blogs.")
        break
    nuevo_blog()
