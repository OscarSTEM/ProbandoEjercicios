"""
Estas en clase de pociones y el profesor Snape nos ha dado teoria acerca de lo
que hace la pocion multijugos y sus efectos, Harry, Ron y Hermione están 
ideando un plan para colarse en la sala común de Slytherin, ayudales:
Ingredientes necesarios:
12 crisopos que se han guisado durante 21 días
1 onza de Antinomio crudo
4 sanguijuelas
16 escrúpulos de Descurainia sophia recogida con luna llena
3 dracmas de Sal Amoniac
2 hojas pulversadas de centunaida
1 poco de cuerno pulverizado de Bicornio
Escofinas de Salitre, Mercurio y Marte
Piel seca desmenuzada de una Serpiente arbórea africana
Gusarajo
Algo de la persona en la que se quiere transformar

Llevamos cerca de 2 meses elaborando la poción
-Crea un lista en la cual tengas una cierta variedad de ingredientes (puedes
poner todos)
-De esa misma lista coge el ingrediente que te falte, ya que hay algunos que ya
están metidos en el caldero
-Que te diga del 1 al 100 cuanto de bien te ha salido la pocion /roll,
+50 está bien y te has transformado en Crabbe y goyle, -50 has cogido el pelo
de la túnica  Millicent Bulstrode y eres un gato!
"""
import random
#Funcion


#Codigo Principal
listaIngredientes=["crisopos","antinomio crudo","sanguijuelas","descurainia sophia","dracmas","centunaida","cuerno bicornio","piel de serpiente","gusarajo","pelo de la persona"]
for ingrediente in listaIngredientes:
    print(f"\n¡Los ingredientes son {ingrediente}!", end="")
    if ingrediente == "piel de serpiente":
        print(f"¡Y tenemos el ingrediente que nos faltaba!")
        
minPocion = 0
maxPocion = 100
roll = random.randrange(minPocion,maxPocion+1)
print(f"\nLa poción se encuentra en un estado de {roll}: ")

