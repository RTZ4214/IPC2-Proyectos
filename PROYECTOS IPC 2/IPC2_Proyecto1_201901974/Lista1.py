from Nodos import *
class listaEncabezado:
    def __init__(self):
        self.primero = None

    def setEncabezado(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        elif int(nuevo.index) < int(self.primero.index):
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:

                if int(nuevo.index) < int(actual.siguiente.index):
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente

            if actual.siguiente == None:
                actual.siguiente = nuevo
                nuevo.anterior = actual

    def getEncabezado(self, index):
        actual = self.primero
        while actual != None:
            if actual.index == index:
                return actual
            actual = actual.siguiente
        return None
class LISTASIMPLE:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def append(self,dato):
        if self.primero==None:
            self.primero=self.ultimo=Nodosim(dato)
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodosim(dato)
    def mostrar(self):
        aux=self.primero
        while aux!= None:
            print(aux.dato)
            aux=aux.siguiente
    def buscar(self,dato):
        temp = self.primero
        while temp is not None:
            if str(temp.dato) == str(dato):
                return True
            temp = temp.siguiente
        return False






