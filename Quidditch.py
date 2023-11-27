"""
Estamos haciendo un recuento de cuantos jugadores hay en el campo de Quidditch en un entrenamiento de las 
casas, queremos probaros a todos y ver quien es el más apto para ser el buscador

Contamos:
Sois 7 jugadores en total 1 de vosotros será el buscador pero antes debemos de comprobarlo. 
"""
import random 

listaJugadores = ["Oscar","Harry","Ron","Fred","George","Neville","Hermione"]
minJugadores = 0
maxJugadores = 7

numBuscador = random.randrange(minJugadores,maxJugadores+1)
print(f"El buscador es {numBuscador}")

numBuscadorPremiado = random.randrange(1,numBuscador+1)
print(f"El buscador premiado es {numBuscadorPremiado}.")

buscador = False 
contadorDelBuscador = 0
numPersonaQuePrueba = 0

while not buscador:
    numSnitchCogida = random.randrange(1,numBuscador+1)
    if numSnitchCogida == numBuscadorPremiado:
        buscador = True
        contadorDelBuscador += 1
        print (f"{listaJugadores[numPersonaQuePrueba]} ha conseguido la snitch {numSnitchCogida}")
        numPersonaQuePrueba = (numPersonaQuePrueba+1)%len(listaJugadores)
print (f"¡El jugador ha conseguido la snitch al intento{contadorDelBuscador} ")
