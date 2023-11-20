class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return str(self.carga) 

def principal():
    bucle = True
    raiz = Arbol("gato")
    while bucle:
        print("PIENSA EN UN ANIMAL")
        if (not si("Estas pensando en un animal? ")): 
            break
        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha
        animal = arbol.carga
        if si("Es un " + animal + "? "):
            print("He adivinado, soy el mejor")
            continue
        #obtener informacion
        nuevo = input("Que animal era? ")
        info = input("Que caracteristica diferencia un " + animal + "de un" +nuevo+ "? ")
        indicador = "Si el animal fuera un " + animal + " cual seria la respuesta?"
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)
    recorrer(input('¿Desea recorrer el arbol?'),raiz)
    return 0

def si(preg):
    resp = (input(preg))
    return (resp[0]=='s' or resp[0]=='S')

def recorrer(resp,raiz):
    if (resp[0]=='s' or resp[0]=='S'):
        inorden(raiz)

def inorden(raiz):
    if(raiz==None):
        return None
    else:
        inorden(raiz.izquierda)
        print(raiz)
        inorden(raiz.derecha)

if __name__ == '__main__':
    principal()

'''
import tkinter as tk
from tkinter import simpledialog, messagebox

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return str(self.carga)

def principal():
    raiz = tk.Tk()
    raiz.title("Adivinanza de Animales")

    def mostrar_mensaje(mensaje):
        messagebox.showinfo("Adivinanza", mensaje)

    def obtener_respuesta(pregunta):
        respuesta = simpledialog.askstring("Adivinanza", pregunta)
        if respuesta is None or respuesta.strip() == "":
            raiz.destroy()  # Cerrar la ventana si se cierra o está en blanco
            raise ValueError("Respuesta vacía o ventana cerrada.")
        return respuesta.strip().lower()  # Limpiar y convertir a minúsculas

    def si(preg):
        resp = obtener_respuesta(preg)
        return resp and resp[0] == 's'

    def recorrer(raiz):
        respuesta = obtener_respuesta('¿Desea recorrer el árbol? ')
        if respuesta and respuesta[0] == 's':
            inorden(raiz)

    def inorden(raiz):
        if raiz is None:
            return
        else:
            inorden(raiz.izquierda)
            mensaje = str(raiz)
            mostrar_mensaje(mensaje)
            inorden(raiz.derecha)

    bucle = True
    raiz_arbol = Arbol("gato")

    while bucle:
        mostrar_mensaje("PIENSA EN UN ANIMAL")

        if not si("¿Estás pensando en un animal? "):
            break

        arbol = raiz_arbol

        while arbol.izquierda is not None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        animal = arbol.carga

        if si("¿Es un " + animal + "? "):
            mostrar_mensaje("He adivinado, soy el mejor")
            continue

        nuevo = obtener_respuesta("¿Qué animal era? ")
        info = obtener_respuesta("¿Qué característica diferencia un " + animal + " de un " + nuevo + "? ")
        indicador = "Si el animal fuera un " + animal + ", ¿cuál sería la respuesta?"
        arbol.carga = info

        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)

    recorrer(raiz_arbol)
    raiz.destroy()

if __name__ == '__main__':
    try:
        principal()
    except ValueError as e:
        print(e)
'''