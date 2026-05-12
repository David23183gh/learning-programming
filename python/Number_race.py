import os
## func niveles del tablero
def nvls_tablero ():
    print("[1.]lvl_basic= 20")
    print("[2.]lvl_intermedio = 30")
    print("[3.]lvl_avanzado= 50")
    print("[4.]lvl_experto= 100")

## func Dados
from random import randint

def roll_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

os.system('clear')

##Validar numero de jugadores
cantidad_jugadores=0
cantidad_jugadores=int(input ("Ingrese la cantidad de jugadores: "))
while cantidad_jugadores <2 :
    cantidad_jugadores=int(input ("Ingrese de nuevo la cantidad de jugadores: "))
while cantidad_jugadores >4 :
    cantidad_jugadores=int(input ("Ingrese de nuevo la cantidad de jugadores: "))
nvls_tablero()
level= int(input("Ingrese el nivel deseado: "))

##Nivel de tablero a escoger
numtab=0

if level == 1:
    numtab = 20
elif level ==2:
    numtab =30
elif level ==3:
    numtab =50
elif level ==4:
    numtab=100

print(f"su nivel ingresado es el siguiente: {level} con un tablero de {numtab} posiciones.")

## Jugadores
Jugador1=0
avance1=0
Jugador2=0
avance2=0
Jugador3=0
Jugador4=0

##while cantidad_jugadores ==2: 
    #input("Jugador 1 tire los dados")
    #dices= roll_dices ()
    #print(dices)
    #print (f"dice 1: {dices[0]}")
    #print (f"dice 2: {dices[1]}")
    #avance1=(dices[0] + dices[1])
    #Jugador1= Jugador1+avance1
    #input("Jugador 2 tire los dados")
    #dices= roll_dices ()
    #print(dices)
    #print (f"dice 1: {dices[0]}")
    #print (f"dice 2: {dices[1]}")
    #avance2=(dices[0] + dices[1])
    #Jugador2= Jugador2+avance2

## Dados
dices= roll_dices ()
print(dices)
print (f"dice 1: {dices[0]}")
print (f"dice 2: {dices[1]}")    



