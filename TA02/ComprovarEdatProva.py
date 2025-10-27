from softwareproperties.gtk.DialogAdd import DialogAdd
from datetime import datetime
import sys

hoy= datetime.now()

AnyA= hoy.year
MesA= hoy.month
DiaA= hoy.day

def CompEdat():
    if (AnyA - AnyN) <= 18:
        if (MesA - MesN) > 0:
            CompMes()
            if (DiaA - DiaN) > 0 :
                print("Ets major d'edat!!!")
                print("Fin del programa")
            else:
                print("No ets major d'edat!!!")
                print("Fin del programa")

def CompMes():
    if MesN < 1 and MesN < 12:
        print("El mes no existeix")
        print("Fin del programa")
        sys.exit()


AnyN=int(input("Quin any vas neixer? "))
CompEdat()
MesN=int(input("Quin mes vas neixer? "))
CompEdat()
DiaN=int(input("Quin dia vas neixer? "))
CompEdat()
