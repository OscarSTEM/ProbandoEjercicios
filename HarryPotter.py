#El sombrero seleccionador esta decidiendo a que casa perteneces,
# dependiendo de los valores que tengas ya sean osadía, valentía, inteligencia, etc...
# estarás destinado a una casa u a otra.

#Funcion 

#Codigo Principal 
listaCasas = ["Gryffindor","Hufflepuff","Slytherin","Ravenclaw"]
listaValores = []

sombreroSeleccionador = input("Dime uno de tus valores y te diré cual es la casa a la que perteneces: ")
listaValores.append(sombreroSeleccionador)
valores0 = False 
if valores0 == "aprendizaje" or "sabiduria" or "ingenio" or "intelecto":
    print("Mmm....Enhorabuena eres Ravenclaw")
elif valores0 == "valiente" or "imprudente" or "coraje" or "osadia":
    print("Mmm....Enhorabuena eres Gryffindor")
elif valores0 == "esfuerzo" or "amigable" or "leal":
    print("Mmm....Enhorabuena eres Hufflepuff")
elif valores0 == "ambicion" or "inteligencia" or "astuto" or "fuerte":
    print("Mmm....Enhorabuena eres Slytherin")
else:
    print("Fuera asquerosa sangre sucia!")









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