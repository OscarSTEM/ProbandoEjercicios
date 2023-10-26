#El sombrero seleccionador esta decidiendo a que casa perteneces,
# dependiendo de los valores que tengas ya sean osadía, valentía, inteligencia, etc...
# Dependiendo de que características poseas estarás destinado a una casa u a otra.

#Funcion 

#Codigo Principal 
listaCasas = ["Gryffindor","Hufflepuff","Slytherin","Ravenclaw"]
listaValoresG = ["valiente","imprudente","coraje", "osadia"]
listaValoresR = ["aprendizaje", "sabiduria", "ingenio", "intelecto"]
listaValoresH = ["esfuerzo","amigable","leal"]
listaValoresS = ["ambicion","inteligencia","astuto","fuerte"]
casa1 = "Gryffindor"
casa2 = "Ravenclaw"
casa3 = "Hufflepuff"
casa4 = "Slytherin"
sombreroSeleccionador = input("Depende de la casa a la que pertenezcas te diré cuales son tus valores: ")

if casa1 == sombreroSeleccionador:
    print (f"Tus valores son {listaValoresG} y perteneces a la casa {casa1}")
elif casa2 == sombreroSeleccionador:
     print (f"Tus valores son {listaValoresR} y perteneces a la casa {casa2}")
elif casa3 == sombreroSeleccionador:
    print (f"Tus valores son {listaValoresH} y perteneces a la casa {casa3}")
elif casa4 == sombreroSeleccionador:
     print (f"Tus valores son {listaValoresS} y perteneces a la casa {casa4}")
else: 
    print ("¡Fuera muggle!")

sombreroSeleccionador = input("Dime uno de tus valores y te diré cual es la casa a la que perteneces: ")

valoresR = "intelecto"
valoresG = "valientes"
valoresH = "leal"
valoresS = "fuerte"

if valoresR == sombreroSeleccionador:
    print(f"Mmm....Enhorabuena eres {casa2}")
elif valoresG == sombreroSeleccionador:
    print(f"Mmm....Enhorabuena eres {casa1}")
elif valoresH == sombreroSeleccionador:
    print(f"Mmm....Enhorabuena eres {casa3}")
elif valoresS == sombreroSeleccionador:
    print(f"Mmm....Enhorabuena eres {casa4}")
else:
    print("¡Enemigos del heredero temed!")
"""
if valoresR == "aprendizaje" or "sabiduria" or "ingenio" or "intelecto":
    print("Mmm....Enhorabuena eres Ravenclaw")
elif valoresG == "valiente" or "imprudente" or "coraje" or "osadia":
    print("Mmm....Enhorabuena eres Gryffindor")
elif valoresH == "esfuerzo" or "amigable" or "leal":
    print("Mmm....Enhorabuena eres Hufflepuff")
elif valoresS == "ambicion" or "inteligencia" or "astuto" or "fuerte":
    print("Mmm....Enhorabuena eres Slytherin")
else:
    print("¡Enemigos del heredero temed!")
"""









"""
listaValoresRavenclaw = ["aprendizaje", "sabiduria", "ingenio", "intelecto"]
listaValoresGryffindor = ["valientes","imprudentes","coraje", "osadia"]
listaValoresHufflepuff = ["esfuerzo","amigables","leales"]
listaValoresSlytherin = ["ambicion","inteligencia","astuto","fuerte"]
"""
"""
for numCasas in range(4):
    sombreroSeleccionador = input("Dime uno de tus valores y te diré a que casa perteneces: ")
    listaValores.append(sombreroSeleccionador)
    print(sombreroSeleccionador)

if numCasas == "aprendizaje" or "sabiduria" or "ingenio" or "intelecto":
    print("Mmm....Enhorabuena eres Ravenclaw")
elif numCasas == "valiente" or "imprudente" or "coraje" or "osadia":
    print("Mmm....Enhorabuena eres Gryffindor")
elif numCasas == "esfuerzo" or "amigable" or "leal":
    print("Mmm....Enhorabuena eres Hufflepuff")
elif numCasas == "ambicion" or "inteligencia" or "astuto" or "fuerte":
    print("Mmm....Enhorabuena eres Slytherin")
"""