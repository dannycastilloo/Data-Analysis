import pandas as pd

data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'ventas': [30500, 35600, 28300, 33900],
    'gastos': [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(data)
print(df)