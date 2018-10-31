#graphMeasures

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from mpldatacursor import datacursor


fResponseNoBuff = pd.read_csv("fResponseNoBuff.csv")
fResponseBuff = pd.read_csv("fResponseBuff.csv")
stepResponseNoBuff = pd.read_csv("stepResponseNoBuff.csv")
stepResponseBuff = pd.read_csv("stepResponseBuff.csv")

plt.figure(1) #GRAFICO DE MAGNITUD respuesta en frecuencia (con y sin buffer en cascada)

plt.title("Respuesta en Frecuencia - Magnitud")
plt.grid(True)
plt.semilogx(fResponseBuff["f"], fResponseBuff["mag"], label='Con buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.semilogx(fResponseNoBuff["f"], fResponseNoBuff["mag"], label='Sin buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(2) #GRAFICO DE FASE respuesta en frecuencia (con y sin buffer en cascada)

plt.grid(True)
plt.semilogx(fResponseBuff["f"], fResponseBuff["pha"], label='Con buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.semilogx(fResponseNoBuff["f"], fResponseNoBuff["pha"], label='Sin buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Fase (degrees)")
plt.title("Respuesta en Frecuencia - Fase")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.figure(3) #RESPUESTA AL ESCALON (con o sin buffer en cascada)

plt.grid(True)
plt.semilogx(stepResponseBuff["t"], stepResponseBuff["in"], label='Escalón - Excitación')
plt.semilogx(stepResponseBuff["t"], stepResponseBuff["mag"], label='Con buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Tensión (Volts)")
plt.semilogx(stepResponseNoBuff["t"], stepResponseNoBuff["mag"], label='Sin buffer en cascada')
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Tensión (Volts)")
plt.title("Respuesta al Escalón")
plt.xticks()
plt.yticks()
plt.legend(loc = 'lower right')
datacursor(formatter="f:{x:.2f} Hz\n mag:{y:.2f} dB".format, display='multiple', draggable=True)

plt.show()