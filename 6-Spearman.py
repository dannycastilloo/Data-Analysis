import pandas as pd

data = pd.read_csv("csv/problemas_del_corazon-2.csv")
correlation = data["presion"].corr(data["colesterol"], method="spearman")

print("Correlación entre presión y colesterol:", correlation)