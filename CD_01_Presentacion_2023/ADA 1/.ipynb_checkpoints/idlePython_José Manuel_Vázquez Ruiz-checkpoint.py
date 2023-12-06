# Cargar las biblioteca Pandas con el alias 'pd’
# Cargar las biblioteca Matplotlib con el alias ‘plt’
import matplotlib.pyplot as plt
import pandas as pd

# Leer datos del archivo datos.csv
data = pd.read_csv("datos/población_méxico.csv")

# Vista previa de las primeras 5 líneas de los datos cargados
print(data.head())

# Graficamos las variables
data.plot(x='Año', y='Población', kind='line')
plt.show()
