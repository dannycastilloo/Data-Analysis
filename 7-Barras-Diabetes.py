import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/problemas_del_corazon-3.csv')

diabetic_counts = df["diabetico"].value_counts()
plt.bar(diabetic_counts.index, diabetic_counts.values)

plt.xlabel("Diabetes")
plt.ylabel("Número de casos")
plt.title("Distribución de la variable 'diabetico'")

plt.show()
