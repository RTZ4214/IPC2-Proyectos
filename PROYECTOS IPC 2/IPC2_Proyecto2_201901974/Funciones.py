from tkinter import filedialog
from xml.dom import minidom

import Grafica
from ListaMa import *
import xml.etree.ElementTree as ET
from  Grafica import *

def cargararhivo1():
    global archivo1, listadelineas, coladeproductos,listaproductos,listadecolas
    listadecolas = LISTASIMPLES()  # se crea una lista de colas
    listadelineas=LISTASIMPLE()

    archivo1 = filedialog.askopenfilename()
    tree = ET.parse(archivo1)
    root = tree.getroot()
    ar = minidom.parse(archivo1)
    CANTIDADDELINEAS = ar.getElementsByTagName("CantidadLineasProduccion")
    numerodelinea = ar.getElementsByTagName("Numero")
    cantidaddecomponentes = ar.getElementsByTagName("CantidadComponentes")
    tiempodeesamblar = ar.getElementsByTagName("TiempoEnsamblaje")
    producto = ar.getElementsByTagName("nombre")
    elaboracion = ar.getElementsByTagName("elaboracion")
    a = int(CANTIDADDELINEAS[0].firstChild.data)
    variable = 0
    ordnline=1
    while (variable != a):  # esto se repetira hasta que la variable sea igual al numero de lineas de produccion
        listas = lista()  # se crea una lista para almacenar toda la información de cada linea en el documento
        A = numerodelinea[variable].childNodes[0].data.strip()  # Se obtiene el numero de cada linea en el archivo
        B = cantidaddecomponentes[variable].childNodes[0].data.strip()  # se obtiene la cantidad de componenetes que posee cada linea
        C = tiempodeesamblar[variable].childNodes[0].data.strip()  # Se obtiene el tiempo de ensamblaje de cada linea
        """D = producto[variable].childNodes[0].data.strip()  # se obtiene el producto a ensamblar
        E = elaboracion[variable].childNodes[0].data.strip()  # se obtiene el orde de como se debe ensamblar el producto a crear"""
        listas.add(str(A), str(B), str(C),str(ordnline))  # se almacena la informacion en la lista para las lineas de produccion
        listadelineas.append(listas, 0,str(ordnline))  # se crea una lista para almacenar las listas de las lineas de produccion(almacenar la lista de la linea 28)

        variable += 1
        ordnline+=1
    productlista = root.find('ListadoProductos')
    listaproductos=LISTASIMPLES()
    for product in productlista.findall('Producto'):
        nombre = product.find('nombre')
        orden = product.find('elaboracion')
        listaproductos.append(orden.text.strip(),nombre.text.strip())

def cargararhivo2():
    global lstproordenados, listadesimulaciones, cont, cont1

    listadesimulaciones=LISTASIMPLE()
    archivo2=filedialog.askopenfilename()
    tree = ET.parse(archivo2)
    root = tree.getroot()
    conteonodos=int(len(root))
    cont = 0
    cont1=0
    cont2=0
    lstproordenados = LISTASIMPLES()
    while (cont != len(root)):
        if str(root[cont].text.strip()) == "":
            lstproordenados = LISTASIMPLES()
            cont2=0
            for v in root[cont]:
                lstproordenados.append(v.text.strip(),cont2)
                cont2+=1
            listadesimulaciones.append(lstproordenados, text, cont1)
            cont1 += 1
        else:
            text = root[cont].text.strip()
        cont += 1
def cargarcolas(text):
    global LisT,colalistafinal,TIME,minicola
    producto=listaproductos.getMatriz(text) #se compara text con el atributo index(el nombre del producto)
    orden=producto.dato#obtenemos la cadena de texto que nos indica el orden de ensamblaje de cada producto
    orden1=orden.split("p")#por medio de la funcion split obtebemos cada linea y componente
    orden2=orden.split(" ")
    LisT=[]#lista que almacena los encabezados de la tabla
    LisT1=[]#lista auxiliar

    for r in range(1,listadelineas.lenmatriz()+1):#ciclo for que va de 1 a al tamaño de la lista lineas(obtiene todas las lineas)
        A=listadelineas.getMatriz(r)
        B=A.x
        C=B.getMatriz(r)
        D=C.lineas
        print(D)
        LisT1.append(D)#se agregan a la lista auxiliar las lineas del archivo
    for b in orden1:#se obtiene una lista con el orden separados por el separador p, y se recorre
        for d in LisT1:# se recorre la lista auxiliar
            l="L"+str(d)#se forma la estructura del nombre de la linea
            if b.strip()==l:#compara si en la lista que nos da la linea y conponente sefun el producto es igyal al texto formado antenieriormente que indica todas las lineas existentes
                LisT.insert(int(d) - 1, b.strip())#si lo esta se agrega a la lista de encabezados
                LisT1.remove(d)#luego elimina ese valor de la lista auxiliar para evitar repeticiones
    x=0
    coladeproductos = Cola()
    minicola=LISTASIMPLE()
    while x!=len(orden2):
        coladeproductos.encolar(orden2[x].strip())
        minicola.append(orden2[x],text,x)
        x+=1
    listadecolas.append(coladeproductos,text)

    # Generar Proceso de Ensamblaje
    A=listadecolas.getMatriz(text)#Se busca el producto solicitado el cual contiene su orden de ensamblaje en una cola
    B = A.dato  # se obtiene el objeto cola dependiendo del producto seleccionado
    boleana=False
    TIME=0
    colalistafinal=Cola()#cola para almacenar el orden en que debe ser ensamblado pero ya procesado con el movimiento de cada brazo y ensamblaje
    while boleana==False:
        tramos=LISTASIMPLE()#se crea una lista para almacenar la información, el estado del brazo, el tiempo en que ocurre esto y la linea en la cual se efectua (estado, tiempo ,linea)
        C = B.primer()  # se obtiene el primer nodo de la cola
        if C==None:# compara si la cola que contiene el orden de ensamblaje esta vacia(B = A.dato)<- esta es la cola la cual contiene el orden
            boleana=True
        else:
            D = C.valor  # este el valor que esta en la primera posicion de la cola
            E = D.split("p")#con split separamos el orden de ensamblaje para obtener la linea y el componente a elegir
            line = E[0]# obtiene el nombre de la linea
            nl = line.split("L")#separamos el nombre para obtener el numero de la linea
            numline = (nl[1])#numero de la linea
            com = (E[1].split("C"))#se separa para el nombre del componente para obtener el numero de componente
            component = int(com[1])#numero de componente
            for x in range(1, listadelineas.lenmatriz() + 1):#ciclo for que se utilizara para obtener los atributos de la linea de ensamblaje seleccioanda
                v = listadelineas.getMatriz(x)#se obtiene la linea solicitada
                vv = v.x
                vvv = vv.getMatriz(x)
                v1 = vvv.lineas
                if v1 == numline:#compara si esa linea esta en la lista de linea
                    v2 = v.x#obtebemos la lista que contiene toda la info de la linea de produccion(linea, componente, tiempo)
                    v3 =vvv#buscamos la linea solicitada
                    compo = int(v3.componentes)#obtebemos el numero de componentes de esa linea
                    tmpensamblar = int(v3.time)#se obtiene el tiempo de ensamblar de esa linea

                    for b in range(1, compo + 1):#ciclo for que va de acuerdo al numero de componentes de la linea en la cual se trabaja
                        if component == b:#busca el componente solicitado segun la secuencia del producto solicitado
                            TIME += 1#variable que indica el tiempo aumenta en 1 al comienzo ya que el tiempo empieza en 0
                            print("Mover Brazo - Componente" + str(b))
                            tramos.append("Mover Brazo - Componente" + str(b), TIME, line)#se alamacena el ultimo movimiento del brazo con su tiempo respectivo y su linea
                            TIME += tmpensamblar#el tiempo aumenta segun el tiempo de ensamblaje de la linea
                            print("Ensamblar Componente "+str(b))
                            tramos.append("Ensamblar Componente " + str(b), TIME, line)#(x,y,n) se alamacena la esamblacion del procuto con su tiempo respectivo y su linea
                            colalistafinal.encolar(tramos)
                            B.desencolar()
                            break
                        else:
                            print("Mover Brazo - Componente" + str(b))
                            TIME += 1
                            tramos.append("Mover Brazo - Componente" + str(b), TIME, line)#se alamacena el movimiento del brazo con su tiempo respectivo y su linea

    Grafica.imagen()
    return TIME














