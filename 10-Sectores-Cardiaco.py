import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("problemas_del_corazon-5.csv")
cardiaco_counts = df['cardiaco'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(cardiaco_counts, labels=cardiaco_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Diagrama de Sectores Circular - Variable "cardiaco"')
plt.axis('equal')

plt.show()