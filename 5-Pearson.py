import pandas as pd

df = pd.read_csv("csv/problemas_del_corazon-1.csv")
correlation = df["edad"].corr(df["colesterol"], method="pearson")

print("Correlación entre edad y colesterol:", correlation)