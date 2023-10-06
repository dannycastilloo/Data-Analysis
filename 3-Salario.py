import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('salario-1.csv')

education_counts = df['estudio'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(education_counts.index, education_counts.values)
plt.xlabel('Estudios')
plt.ylabel('Ingresos')
plt.title('Estudios vs. Ingresos')
plt.xticks(education_counts.index)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()