from builtins import print
from tkinter import *
from tkinter import ttk
import Funciones
from Funciones import *
import Grafica


                                      #   VENTANA PRINCIPAL
ventana=Tk()
ventana.title("Ensamblador")
ventana.geometry("650x650")
                                      #    CREAR UN CUADERNO
tab_control=ttk.Notebook(ventana)
                                        #     FRAMES
archivo=Frame(tab_control)
archivo.config(bg="blue")
reporte=Frame(tab_control)
reporte.config(bg="yellow")
ayuda=Frame(tab_control)
ayuda.config(bg="blue")

Label(ayuda,bg="green", text="Nombres", font=("Yu Gothic",20)).grid(column=0, row=1, padx=30, pady=30)
Label(ayuda, bg="green",text="Joseph Raphael",font=("Yu Gothic",20)).grid(column=1, row=1, padx=30, pady=30)
Label(ayuda,bg="green", text="Apellidos", font=("Yu Gothic",20)).grid(column=0, row=2, padx=30, pady=30)
Label(ayuda,bg="green", text="Gómez Tzorin",font=("Yu Gothic",20)).grid(column=1, row=2, padx=30, pady=30)
Label(ayuda, bg="green",text="Registro Académico", font=("Yu Gothic",20)).grid(column=0, row=3, padx=30, pady=30)
Label(ayuda,bg="green", text="201901974",font=("Yu Gothic",20)).grid(column=1, row=3, padx=30, pady=30)
Label(ayuda,bg="green", text="Asignatura", font=("Yu Gothic",20)).grid(column=0, row=4, padx=30, pady=30)
Label(ayuda,bg="green", text="IPC 2 SECCION C",font=("Yu Gothic",20)).grid(column=1, row=4, padx=30, pady=30)



                                        #  BOTONES
botonarchivo1=Button(archivo,font=("Yu Gothic",30) ,text="ARCHIVO 1",command=cargararhivo1, bg="orange").place(x=220,y=60)
botonarchivo2=Button(archivo,font=("Yu Gothic",30),text="ARCHIVO 2",command=cargararhivo2, bg="orange").place(x=220,y=200)

def combosimulacion():
    global comboboxsimulaciones
    opciones = []
    for x in range(0, int(Funciones.listadesimulaciones.lenmatriz())):#ciclo for para extraer el nombre de las simulaciones a ejecutar
        valorx = Funciones.listadesimulaciones.getMatriz(x)#con la funcion getmatriz obtenemos el objeto lista
        opciones.append(valorx.y) #de la lista anteriormente creada obtenemos el atributo y que sera el nombre de la simulacion y lo incertamos en una lista
    comboboxsimulaciones = ttk.Combobox(reporte,value=opciones, state="readonly")#creamos el ComboBox y sus opciones seran la lista de simulaciones
    comboboxsimulaciones.place(x=10, y=50)#posicionamos el ComboBox

def ProductoS():
    global comboboxproductos
    opciones2=[]
    txt = comboboxsimulaciones.get()#obtenemos el texto actual del comboBox de la lista de simulaciones
    for x in range(0, int(Funciones.listadesimulaciones.lenmatriz())):#nuevamente ciclo for para extraer el nombre de las simulaciones
        valorx = Funciones.listadesimulaciones.getMatriz(x)#obtemos la lista
        if txt==str(valorx.y):#comparamos si el texto actual del ComboBox es igual
            num=int(valorx.x.lenmatriz())#obtenemos el tamaño de la lista
            for vv in range(0,num): #creamos otro for para extraer los datos del listado de productos
                var=valorx.x.getMatriz(str(vv))#obtnemos el atributo x de la lista de simulaciones que es otra lista que contiene la lista de productos(objeto lista)
                #a esta variable var le asignamos el el objeto lista para poder acceder a los atributos de esta otra lista
                opciones2.append(var.dato)#obtenemos el atributo dato el cual contiene el nombre del producto que le pertenece a esa simulación
    comboboxproductos = ttk.Combobox(reporte, value=opciones2, state="readonly")#creamos otro combobox con estos productos que iran cambiando dependiendo de la simulación elegida
    comboboxproductos.place(x=10, y=80)
def colascargar():
    tiempO=cargarcolas(comboboxproductos.get())

    ala=Funciones.LisT
    Tabla = ttk.Treeview(reporte, height="20", columns=ala)
    Tabla.place(x=120, y=110)
    archivo = open("tabla.css ", "w")
    archivo.write(""" /*
    	Color fondo: #632432;
    	Color header: 246355;
    	Color borde: 0F362D;
    	Color iluminado: 369681;
    */
    body{
    	background-image:url("https://cdn.wallpapersafari.com/21/29/ecAh3t.jpg");
        background-size: 100%;
        font-family: Arial;
    }
    #main-container{
    	margin: 150px auto;
    	width: 600px;
    }
    table{
    	background-color: white;
    	text-align: left;
    	border-collapse: collapse;
    	width: 100%;
    }
    th, td{
    	padding: 10px;
    }
    thead{
    	background-color: #246355;
    	border-bottom: solid 5px #0F362D;
    	color: white;
    }
    tr:nth-child(even){
    	background-color: #ddd;
    }
    tr:hover td{
    	background-color: #369681;
    	color: white;
    }""")
    archivo.close()
    archivo1 = open("SALIDA.html", "w", encoding="utf-8")
    archivo1.write("<center><h1><font color =white>"+comboboxsimulaciones.get()+"producto ->"+comboboxproductos.get()+"</font></h1></center>")
    archivo1.write("""<head>
    	<meta charset="UTF-8">
    	<link rel="stylesheet" href="tabla.css"></head>
        <body>
    	<div id="main-container">
    		<table>
    			<thead>
    				<tr>""")

    d = open('sol.xml', 'w', encoding='utf-8')
    d.write('<SalidaSimulación>\n')
    d.write('<Nombre>' + comboboxsimulaciones.get() + ' </Nombre>\n')
    d.write('<ListadoProductos>\n')
    d.write('<Producto>\n')
    d.write('<Nombre>' +comboboxproductos.get()+ '</Nombre>\n')
    d.write('<TiempoTotal>' + str(tiempO)+'</TiempoTotal>\n')
    d.write('<ElaboracionOptima>\n')
    Tabla.heading("#0", text="Tiempo(s)")
    archivo1.write("<th>" +"Tiempo(s)" + "</th>")
    temp=1
    for x in ala:
        Tabla.heading(x, text=x, anchor=CENTER)
        archivo1.write("<th>"+x+"</th>")
    archivo1.write("""</tr>
			</thead>
			""")


    boleanaa=False
    colafinal = Funciones.colalistafinal
    while boleanaa == False:
        colafinal1 = colafinal.primer()
        if colafinal1==None:
            boleanaa==True
            break
        else:
            primerelemento = colafinal1.valor  # (estado , tiempo, linea)->(x,y,n)

            if primerelemento.lenmatriz()==0:
                colafinal.desencolar()
            else:
                plo=[]
                archivo1.write(" <tr>")
                archivo1.write("<td>" + str(temp) + "</td>")
                for r in ala:
                    A = primerelemento.getMatriz(r)
                    poslinea = int(ala.index(r))
                    if A == None:
                        plo.insert(poslinea, "No hacer Nada")
                        d.write('<Tiempo NoSegundo="' +str(temp)+ '">\n')
                        d.write('<LineaEnsamblaje NoLinea="' + r + '">\n')
                        d.write("No hacer Nada\n")
                        d.write("</LineaEnsamblaje>\n")
                        d.write('</Tiempo>\n')

                        archivo1.write("<td>" + "No hacer Nada" + "</td>")

                        if len(plo)==len(ala):
                            archivo1.write("</tr>")
                            Tabla.insert("", END,text=temp, values=plo)

                    else:
                        plo.insert(poslinea, A.x)
                        primerelemento.desencolar()
                        temp=A.y
                        d.write('<Tiempo NoSegundo="' +str(temp) + '">\n')
                        d.write('<LineaEnsamblaje NoLinea="' + r + '">\n')
                        d.write(str(A.x)+"\n")

                        archivo1.write("<td>" + A.x+ "</td>")
                        d.write("</LineaEnsamblaje>\n")
                        d.write('</Tiempo>\n')
                        if len(plo)==len(ala):
                            archivo1.write("</tr>")
                            Tabla.insert("", END,text=temp, values=plo)
    d.write('</ElaboracionOptima>\n')
    d.write('</Producto>\n')
    d.write('</ListadoProductos>\n')
    d.write('</SalidaSimulación>\n')
    d.close()
    archivo1.write("""
        		</table>
        	</div>
        </body>
        </html>""")
    archivo1.close()
    os.system("SALIDA.html")


logo = PhotoImage(file='reporte.png')
lb = Label(reporte, font=("Yu Gothic", 10), image=logo)
lb.place(x=100, y=600)




#---------------------------------BOTONES PARA CARGAR SIMULACIONES Y PRODUCTOS-------------------------
botoncargar=Button(reporte,command=combosimulacion,font=("Yu Gothic",10) ,text="SIMULACIONES", bg="orange").place(x=10,y=10)
botoncargar2=Button(reporte,command=ProductoS,font=("Yu Gothic",10) ,text="PRODUCTOS", bg="orange").place(x=130,y=10)
gar2=Button(reporte,command=colascargar,font=("Yu Gothic",10) ,text="ORDENAR", bg="orange").place(x=240,y=10)

#----------------------------------AGREGAR LOS FRAMES AL CUADERNO----------------------------------------
tab_control.add(archivo, text="ARCHIVO")
tab_control.add(reporte, text="REPORTES")
tab_control.add(ayuda, text="AYUDA")
tab_control.pack(expand=1,fill='both')
ventana.mainloop()