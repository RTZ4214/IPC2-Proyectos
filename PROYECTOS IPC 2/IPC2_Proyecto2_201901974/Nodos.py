class NodoEncabezadoMa:
    def __init__(self, index):
        self.index = index
        self.anterior = None
        self.siguiente = None
        self.accesoNodo = None
class NodoListaMatrices:
    def __init__(self, x, y,n):
        self.x = x
        self.y = y
        self.n = n
        self.siguiente = None
class NODOcola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class Nodosim:
    def __init__(self,dato,index):
        self.dato=dato
        self.index=index
        self.siguiente=None
class NodosLineas:
    def __init__(self,lineas, componentes, time,n):
        self.lineas = lineas
        self.n=n
        self.componentes = componentes
        self.time = time
        self.siguiente = None

