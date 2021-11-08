class Nodo:
    def __init__(self, fecha, facturas_recibidas, nite_invalido, nitr_invalido, IVA, TOT, FC, EMISORES, RECEPTORES, autorizaciones):
        self.fecha = str(fecha)
        self.facturas_recibidas = str(facturas_recibidas)
        self.nite_invalido = str(nite_invalido)
        self.nitr_invalido = str(nitr_invalido)
        self.IVA = str(IVA)
        self.TOT = str(TOT)
        self.FC = str(FC)
        self.EMISORES = str(EMISORES)
        self.RECEPTORES = str(RECEPTORES)
        self.autorizaciones = str(autorizaciones)
class nodo2:
    def __init__(self,nits,ivA,fech):
        self.nits=str(nits)
        self.ivA=ivA    
        self.fech=fech
