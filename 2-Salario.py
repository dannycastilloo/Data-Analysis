import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salario.csv')

edad = df['edad']
estudio = df['estudio']

plt.figure(figsize=(10, 6))
plt.scatter(edad, estudio, marker='o', color='blue', alpha=0.5)
plt.title('Edad vs. Estudio')
plt.xlabel('Edad')
plt.ylabel('Estudio')

plt.grid(True)
plt.show()