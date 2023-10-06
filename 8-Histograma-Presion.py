import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("problemas_del_corazon-4.csv")

presion = df["presion"]

plt.hist(presion, bins=10, edgecolor='k', alpha=0.75)

plt.xlabel("Presión")
plt.ylabel("Frecuencia")
plt.title("Histograma de la variable 'presion'")

plt.show()