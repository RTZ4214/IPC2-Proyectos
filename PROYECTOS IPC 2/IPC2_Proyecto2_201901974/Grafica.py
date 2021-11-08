import os
import Funciones
def imagen():
    arreglo=Funciones.minicola
    f = open('reporte.dot', 'w', encoding='utf-8')
    f.write("digraph dibujo{\n")
    f.write('rankdir=LR;\n')
    f.write('node [shape=egg,style=filled];\n')
    for x in range(0, arreglo.lenmatriz()-1):
        A=arreglo.getMatriz(x)
        B=arreglo.getMatriz(x+1)
        f.write(A.x + "->" + B.x + "\n")
    f.write("}")
    f.close()
    os.system("dot -Tpng reporte.dot -o reporte.png")

