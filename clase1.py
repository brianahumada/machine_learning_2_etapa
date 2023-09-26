import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (tamaño en SUPERFICIE (pies cuadrados))
tamanio = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
#Debo aplicar reshape a tamanio.
#Resultado: Vector REDIMENSIONADO

# Precios correspondientes en dólares
precio = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])
#Debo aplicar reshape a precio.
#Resultado: Vector REDIMENSIONADO

# Crear un objeto de modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos
modelo.fit(tamanio.reshape(-1, 1), precio) #

#Explicacion RESHAPE
#[[1,2,3],
# [4,5,6]]

#Aplicamos reshape.(3,2).

#[[1,2],
# [3,4],
# [5,6]]

# Realizar predicciones
tamanio_prediccion = np.array([1600, 1800, 2000]) #eSTOS SON LOS DATOS QUE QUIERO PREDECIR A PARTIR DEL MODELO
precio_prediccion = modelo.predict(tamanio_prediccion.reshape(-1, 1))

# Visualizar los resultados
plt.scatter(tamanio, precio, color='blue', label='Datos reales')
plt.plot(tamanio_prediccion, precio_prediccion, color='red', linewidth=2, label='Regresión Lineal')
plt.xlabel('Tamaño (pies cuadrados)')
plt.ylabel('Precio (dólares)')
plt.legend()
plt.title('Regresión Lineal para Predecir el Precio de las Casas')
plt.show()


# Imprimir las predicciones
for i in range(len(tamanio_prediccion)):
    print(f"Para una casa de {tamanio_prediccion[i]} pies cuadrados, el precio estimado es de ${precio_prediccion[i]:.2f}")
