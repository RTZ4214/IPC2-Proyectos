import math
import numpy as np
from matplotlib import colors, pyplot as plt
grafico=plt.figure()
empanada=["hola", "arroz"]
ventas=[33,44]
colores=("red","blue")
plt.pie(ventas, labels=empanada)
grafico.savefig("img.png")
plt.show()