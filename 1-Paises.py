import matplotlib.pyplot as plt

x = [2012, 2022, 2025, 2028]
y = [42, 43, 45, 47]

x2 = [2012, 2022, 2025, 2028]
y2 = [42, 48, 49, 50]

plt.figure(figsize=(10, 6))

plt.plot(x, y, label='Perú', color='blue', marker='o', linestyle='-')

plt.plot(x2, y2, label='Colombia', color='green', marker='o', linestyle='-')

plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Población en Perú y Colombia (2012-2028)')

plt.legend()

plt.grid(True)
plt.show()