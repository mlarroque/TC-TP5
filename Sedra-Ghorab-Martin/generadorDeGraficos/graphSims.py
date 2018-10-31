#graphSims
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


simZinE1 = pd.read_csv("simZinE1.csv")
simZinE2 = pd.read_csv("simZinE2.csv")
simZoutE1 = pd.read_csv("simZoutE1.csv")
simZoutE2 = pd.read_csv("simZoutE2.csv")
simGanE1 = pd.read_csv("simGanE1.csv")
simGanE2 = pd.read_csv("simGanE2.csv")
simZinEtotal = pd.read_csv("zin.csv")

plt.figure(1) #GRAFICO DE MAGNITUD Zin (E1 y E2 superpuestos)
plt.semilogx(simZinE1["f"], 10**(simZinE1["mag"]/20), label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (ohms)")
plt.title("Impedancia de Entrada - Magnitud")
plt.grid(True)
plt.semilogx(simZinE2["f"], 10**(simZinE2["mag"]/20), label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (ohms)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(2) #GRAFICO DE Fase Zin (E1 y E2 superpuestos)
plt.semilogx(simZinE1["f"], simZinE1["pha"], label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.title("Impedancia de Entrada - Fase")
plt.grid(True)
plt.semilogx(simZinE2["f"], simZinE2["pha"], label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(3) #GRAFICO DE MAGNITUD Zout (E1 y E2 superpuestos)
plt.semilogx(simZoutE1["f"], 10**(simZoutE1["mag"]/20), label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (ohms)")
plt.title("Impedancia de Salida - Magnitud")
plt.grid(True)
plt.semilogx(simZinE2["f"], 10**(simZoutE2["mag"]/20), label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (ohms)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(4) #GRAFICO DE Fase Zout (E1 y E2 superpuestos)
plt.semilogx(simZoutE1["f"], simZoutE1["pha"], label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.title("Impedancia de Salida - Fase")
plt.grid(True)
plt.semilogx(simZinE2["f"], simZinE2["pha"], label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(5) #GRAFICO DE MAGNITUD ganancia (E1 y E2 superpuestos)
plt.semilogx(simGanE1["f"], simGanE1["mag"], label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.title("Ganancia - Magnitud")
plt.grid(True)
plt.semilogx(simGanE2["f"], simGanE2["mag"], label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(6) #GRAFICO DE Fase ganancia (E1 y E2 superpuestos)
plt.semilogx(simGanE1["f"], simGanE1["pha"], label='Etapa 1')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.title("Ganancia - Fase")
plt.grid(True)
plt.semilogx(simGanE2["f"], simGanE2["pha"], label='Etapa 2')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(7) #GRAFICO DE Fase Zin (E1 y E2 superpuestos)
plt.semilogx(simZoutE1["f"], 10**(simZoutE1["mag"]/20), label='Etapa 1 - Zout')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Mag (ohms)")
plt.title("Impedancias Zin/Zout - Magnitud")
plt.grid(True)
plt.semilogx(simZinE2["f"], 10**(simZinE2["mag"]/20), label='Etapa 2 - Zin')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Mag (ohms)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(8) #GRAFICO DE Fase Zin (E1 y E2 superpuestos)
plt.semilogx(simZinEtotal["f"], 10**(simZinEtotal["mag"]/20))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Mag (ohms)")
plt.title("Impedancia de Entrada - Magnitud")
plt.grid(True)

plt.show()