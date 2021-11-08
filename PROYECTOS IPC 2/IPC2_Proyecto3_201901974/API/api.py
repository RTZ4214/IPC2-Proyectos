from logging import debug
from flask import Flask, Response, request
from flask_cors import CORS
import json
import re
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from nodo import *
from matplotlib import pyplot as plt
def calculo(nit):
    dos=0
    for x in range(len(nit)-1,-1,-1):
        val=int(nit[x])
        
        uno=val*x
        dos+=uno
    tres=dos%11
    cuatro=abs(11-tres)
    cinco=cuatro%11
    if cinco>=10:
        return "invalido"
    else:
        return "valido"
app = Flask(__name__)
cors=CORS(app , resources={r"/*":{"origin":"*"}})
@app.route('/datos', methods=['GET'])
def get_data():
    save_file=open('autorizaciones.xml', 'r+')
    
    return Response(status=200,
    response=save_file.read(),
    content_type='text/plain')

@app.route('/datos', methods=['POST'])

def post_data():
    global GRfech
    str_file= request.data.decode('utf-8')
    Jsonarchivo = json.loads(str_file)
    tit=Jsonarchivo['SOLICITUD_AUTORIZACION']
    expreg= '[0-3][0-9]/[0-1][0-9]/20[0-9][0-9]'
    ft=0
    fc=0
    fechas=[]
    Lautorizaciones=[]
    error_ref=0
    nitr_invalido = 0
    nite_invalido = 0
    iva_malo = 0
    total_malo = 0
    referencias = []
    nite = []
    nitr= []
    iVa=[]
    NITS=[]
    GRfech=[]
    
    for dte in tit['DTE']:
        tiempo = dte['TIEMPO']
        tiempo_validado = re.findall(expreg, tiempo)
        tiempo_validado = tiempo_validado[0]
        if tiempo_validado not in fechas and ft > 0:

            Lautorizaciones.append(Nodo(tiempo_validado, ft, nite_invalido,nitr_invalido, iva_malo, total_malo,fc, len(nite), len(nitr), None))
            error_ref=0
            nitr_invalido=0
            nite_invalido=0
            ft=0
            fc=0
            iva_malo=0
            total_malo=0
            referencias=[]
            nite = []
            nitr= []
            fechas.append(tiempo_validado)
        
        referencia = dte['REFERENCIA']
        emis=str(dte["NIT_EMISOR"])
        recept=str(dte["NIT_RECEPTOR"])
        veremi=calculo(emis)
        verrecp=calculo(recept)
        if veremi=="valido":
            print("VALIDO")
            emisorvalido=emis
        else:
            print("F1")
            nite_invalido+=1
        if verrecp=="valido":
            print("VALIDO2")
            receptorvalido=recept
        else:
            print("F2")
            nitr_invalido+=1    

        
        if referencia in referencias:
            error_ref += 1
        else:
            referencias.append(referencia)
        ft += 1
        valor = dte['VALOR']
        valor = float(valor)
        iva = dte['IVA']
        total = dte['TOTAL']

        iva_correcto = round(valor*0.12, 2)
        total_correcto = round(iva_correcto + valor, 2)
        

        if iva != iva_correcto:
            iva_malo += 1

        if total != total_correcto:
            total_malo += 1
        text= emisorvalido+receptorvalido
        IV=float(iva_correcto)
        iVa.append(IV)
        NITS.append(text)
        GRfech.append(nodo2(NITS,iVa,tiempo_validado))
    
    autorizaciones = Element('LISTAAUTORIZACIONES')
    for aut in Lautorizaciones:
        autorizacion = SubElement(autorizaciones, 'AUTORIZACION')
        fecha = SubElement(autorizacion, 'FECHA')
        fecha.text = aut.fecha
        fre = SubElement(autorizacion, 'FACTURAS_RECIBIDAS')
        fre.text = aut.facturas_recibidas

        # Nodo Errores
        errores = SubElement(autorizacion, 'ERRORES')
        emi = SubElement(errores, 'NIT_EMISOR')
        emi.text = aut.nite_invalido
        recep = SubElement(errores, 'NIT_RECEPTOR')
        recep.text = aut.nitr_invalido
        iva = SubElement(errores, 'IVA')
        iva.text = aut.IVA
        total = SubElement(errores, 'TOTAL')
        total.text = aut.TOT

        # Resto Nodos Principales
        fco = SubElement(autorizacion, 'FACTURAS_CORRECTAS')
        fco.text = aut.FC

        canemi = SubElement(autorizacion, 'CANTIDAD_EMISORES')
        canemi.text = aut.EMISORES

        canrecep = SubElement(autorizacion, 'CANTIDAD_RECEPTORES')
        canrecep.text = aut.RECEPTORES

    # ET.dump(autorizaciones)
    tree = ET.ElementTree(autorizaciones)
    xml.etree.ElementTree.indent(tree, space="\t", level=0)
    tree.write("autorizaciones.xml", encoding="utf-8")
    grafico=plt.figure()
    plt.pie(iVa,labels=NITS)
    grafico.savefig("img.png")
    plt.show()
    return Response(status=204)

if __name__=='__main__':
    app.run(debug= True)
