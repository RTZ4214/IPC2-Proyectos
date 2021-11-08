import os
def Gráfica(m,n,matrizsolicitada,nombre):

    f = open('reporte.dot', 'w', encoding='utf-8')
    f.write("graph DIBUJO{\n")
    f.write('rankdir=TB;\n')
    f.write('node [shape=egg,height=0.5, width=2,style=filled,fontsize=30, fillcolor=orange,color=blue,fontcolor=blue];\n')
    f.write("labelloc=t;\nfontsize=30\nlabel="+nombre+";\n")#TITULO PARA EL GRAFO
    for x in range(1, m):                                        #CREACION DE LOS NODOS
        for y in range(1, n):
            OLA = matrizsolicitada.getmatriz(str(y), str(x))
            text="X"+str(OLA.fila)+"Y"+str(OLA.columna)
            Gasolina = str(OLA.gasolina)
            f.write(text+"[label="+Gasolina+"]\n")
    for x in range(1, m):                                       #COLOCAR LOS  NODOS DE FORMA HORIZONTAL
        for y in range(1, n-1):
            OLA = matrizsolicitada.getmatriz(str(y), str(x))
            OLA2 = matrizsolicitada.getmatriz(str(y+1), str(x))
            text = "X" + str(OLA.fila) + "Y" + str(OLA.columna)
            text2 = "X" + str(OLA2.fila) + "Y" + str(OLA2.columna)
            f.write(text+"--"+text2+"[constraint=false]\n")
    for x in range(1, m-1):                                      #COLOCAR LOS NODOS DE FORMA VERTICAL
        for y in range(1, n):
            OLA = matrizsolicitada.getmatriz(str(y), str(x))
            OLA2 = matrizsolicitada.getmatriz(str(y), str(x+1))
            text = "X" + str(OLA.fila) + "Y" + str(OLA.columna)
            text2 = "X" + str(OLA2.fila) + "Y" + str(OLA2.columna)
            f.write(text+"--"+text2+"\n")
    f.write("}")#Final del ARCHIVO DOT
    f.close()
    os.system("dot -Tpdf reporte.dot -o reporte.pdf")
    os.system("reporte.pdf")
