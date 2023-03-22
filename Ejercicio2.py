import threading
import time
import random

NUM_CLIENTES = 20 #La cantidad de clientes que se elige al programa
clientes_atendidos = 0
sillas_espera = threading.Semaphore(4)
silla_barbero = threading.Semaphore(1)

def recortar_cliente():
    tiempo = random.randint(1, 5)
    time.sleep(tiempo)

def cliente():
    global clientes_atendidos
    if silla_barbero.acquire(blocking=False):
        print("Cliente sentándose en la silla del barbero")
        sillas_espera.release()
        recortar_cliente()
        silla_barbero.release()
        clientes_atendidos += 1
        print("Cliente atendido")
    else:
        print("No hay sillas disponibles. El cliente se va.")

def barbero():
    global clientes_atendidos
    while clientes_atendidos < NUM_CLIENTES:
        sillas_espera.acquire()
        silla_barbero.acquire()
        print("Barbero afeitando a un cliente")
        recortar_cliente()
        silla_barbero.release() 
        print("Barbero ha terminado de afeitar a un cliente")
 
for i in range(NUM_CLIENTES):
    threading.Thread(target=cliente).start()

threading.Thread(target=barbero).start()

