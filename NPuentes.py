import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
inicioPuente2= 35
largoPuente2=50
print("ingrese su cantidad de vacas pasen al mismo tiempo")
x=int(input())
print("ingrese su cantidad de vacas pasen al mismo tiempo en el segundo puente")
y=int(input())
semaforoPuente = threading.Semaphore(x)
semaforoPuente2= threading.Semaphore(y)
class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.5)

  def avanzar(self):
    if (self.posicion == inicioPuente - 1):
      semaforoPuente.acquire()#esto congela a las vacas en una posicion anterior al puente 
    if (self.posicion == inicioPuente2 - 1):
      semaforoPuente2.acquire()
    time.sleep(self.velocidad)
    self.posicion += 1

    if (self.posicion == inicioPuente + largoPuente):
      semaforoPuente.release()
    if (self.posicion == inicioPuente2 + largoPuente2):
      semaforoPuente2.release()

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

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)
  print(' ' * inicioPuente2 + '=' * largoPuente2)

while(True):
  cls()
  print('Apreta Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
  