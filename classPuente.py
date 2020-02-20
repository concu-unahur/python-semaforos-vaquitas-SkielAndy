import os
import random
import time
import threading
from puente import Puente
puentes= []

print("ingrese su cantidad de vacas pasen al mismo tiempo")
x=int(input())
semaforoPuente = threading.Semaphore(x)
print("ingrese su cantidad de puentes")
n=int(input())
for i in range(n):
    print("ingrese su inicio siempre mayor al puente anterior")
    b=int(input())
    print("ingrese su largo")
    y=int(input())
    p = Puente(b,y)
    puentes.append(p)
class Vaca(threading.Thread):
    def __init__(self):
        super().__init__()
        self.posicion = 0
        self.velocidad = random.uniform(0.1, 0.5)

    def avanzar(self):
        
        if (self.posicion == p.inicio() - 1):
            semaforoPuente.acquire()#esto congela a las vacas en una posicion anterior al puente 
        time.sleep(self.velocidad)
        self.posicion += 1
        if (self.posicion == p.inicio() + p.largo()):
            semaforoPuente.release()

    def dibujar(self):
        print(' ' * self.posicion + "v")

    def run(self):
        while(True):
            self.avanzar()

vacas = []

print("ingrese su cantidad de vacas")
n=int(input())
for i in range(n):
    v = Vaca()
    vacas.append(v)
    v.start()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


while(True):
    cls()
    print('Apreta Ctrl + C varias veces para salir...')
    print()
    for p in puentes:
        p.dibujarPuente()
    for v in vacas:
        v.dibujar()
    for p in puentes:
        p.dibujarPuente()
    time.sleep(0.2)
  