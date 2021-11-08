from Nodos import NodosLineas
from Nodos import *
class lista:
    def __init__(self):
        self.primero = None

    def add(self, lineas, componentes, time,n):
        nuevo = NodosLineas( lineas, componentes, time,n)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def getMatriz(self, n):
        temp = self.primero
        while temp is not None:
            if str(temp.n) == str(n):
                return temp
            temp = temp.siguiente
        return None

    def setMatriz(self, lineas, time):
        temp = self.primero
        while temp is not None:
            if str(temp.lineas) == str(lineas):
                temp.time = time
            temp = temp.siguiente
class LISTASIMPLE:
    def __init__(self):
        self.primero = None

    def append(self, x, y,n):
        nuevo = NodoListaMatrices(x, y,n)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def desencolar(self):
        if self.primero:

            self.primero = self.primero.siguiente

    def lenmatriz(self):
        temp = self.primero
        c = 0
        while temp is not None:
            c += 1
            temp = temp.siguiente
        return c

    def getMatriz(self, n):
        temp = self.primero
        while temp is not None:
            if str(temp.n) == str(n):
                return temp
            temp = temp.siguiente
        return None
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo=None
    def encolar(self,c):
        nuevo=NODOcola(c)
        if self.primero==None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo


    def desencolar(self):
        if self.primero:
            valor=self.primero.valor
            self.primero=self.primero.siguiente
            return valor
    def primer(self):
        return self.primero


    def imprimirCola(self):
        if self.primero==None:
            print("Cola vacía - Totalidad de órdenes entregadas")
        else:
            aux = self.primero
            contador = 0
            while aux != None:
                contador += 1
                print(aux.valor)
                aux = aux.siguiente
class LISTASIMPLES:
    def __init__(self):
        self.primero = None

    def append(self, valor,index):
        nuevo = Nodosim(valor,index)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def lenmatriz(self):
        temp = self.primero
        c=0
        while temp is not None:
           c+=1
           temp = temp.siguiente
        return c
    def primer(self):
        return self.primero

    def getMatriz(self, n):
        temp = self.primero
        while temp is not None:
            if str(temp.index) == str(n):
                return temp
            temp = temp.siguiente
        return None