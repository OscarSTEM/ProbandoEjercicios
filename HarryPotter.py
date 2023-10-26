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
