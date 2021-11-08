class vertices:
    def __init__(self,i,name,f,c):
        self.id=i
        self.fila=f
        self.columna=c
        self.vecinos=[]
        self.name=name
        self.visitado=False
        self.padre=None
        self.distancia=float('inf')
    def agregarvecino(self,v,p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])
class graph:
    def __init__(self):
        self.vertices={}
    def agregarVertices(self,id,name,f,c):
        if id not in self.vertices:
            self.vertices[id]=vertices(id,name,f,c)
    def agregarArista(self,a,b,p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarvecino(b,p)
            self.vertices[b].agregarvecino(a, p)
    def imprimirgrafica(self,text):
        for v in self.vertices:
            if self.vertices[v].name == text:
                return v
    def camino(self,a,b):
        camino=[]
        actual=b
        while actual != None:
            camino.insert(0,actual)
            actual=self.vertices[actual].padre
        return camino
    def minimo(self,lista):
        if len(lista)>0:
            m=self.vertices[lista[0]].distancia
            v=lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m= self.vertices[e].distancia
                    v=e
            return v
    def dijkstra(self,a):
        if a in self.vertices:
            self.vertices[a].distancia=0
            actual=a
            novisitados=[]
            for x in self.vertices:
                if x != a:
                    self.vertices[x].distancia=float('inf')
                self.vertices[x].padre=None
                novisitados.append(x)
            while len(novisitados)>0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado==False:
                        if self.vertices[actual].distancia+vecino[1]< self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia+vecino[1]
                            self.vertices[vecino[0]].padre=actual
                self.vertices[actual].visitado=True
                novisitados.remove(actual)
                actual=self.minimo(novisitados)

        else:
            return False
