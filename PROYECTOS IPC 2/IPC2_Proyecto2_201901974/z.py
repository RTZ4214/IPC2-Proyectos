from ListaMa import LISTASIMPLE
a=LISTASIMPLE()
a.append(1,2,1)
a.append(2,3,2)
a.append(5,3,3)
for x in range(1,a.lenmatriz()+1):
    b=a.getMatriz(x)
    print(b.x)
a.desencolar()
for x in range(1,a.lenmatriz()+1):
    b=a.getMatriz(x)
    print(b.x)
