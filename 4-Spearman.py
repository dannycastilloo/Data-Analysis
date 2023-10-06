import pandas as pd

df = pd.read_csv("problemas_del_corazon.csv")
correlation_matrix = df.corr(method='spearman')

print(correlation_matrix)