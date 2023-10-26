#Hemos aprendido el hechizo alohomora, 
#pero el ojo de la cerradura se nos resiste.
#Hasta que no conjures y hagas bien el movimiento de varita correcto,
#no podrás abrir dicha cerradura, ¡mucha suerte!
#Esto es con un bucle while.
#-------------Enunciado-------------------
#Funcion
#Codigo Principal
puertaOjo = "alohomora"
confirmacionHechizo = input("¿Que hechizo vas a utilizar?: ")
while puertaOjo != confirmacionHechizo:
    confirmacionHechizo = input("¡No has entrenado suficiente el movimiento de varita!, echale ganas: ")
print(f"¡Enhorabuena has abierto la puerta!")