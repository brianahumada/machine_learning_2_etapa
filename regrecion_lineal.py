#########################################################
#___________EJEMPLO DE REGRESION LINEAL CON FRUTAS____________

# ==============================================================================
##################################
# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# ==============================================================================
##################################
# Crear un DataFrame con los datos de frutas en varios locales comerciales
data = pd.DataFrame({
    'Kilogramos_Frutas': [5, 7, 8, 10, 3, 6, 12, 15, 4, 9],  # Cantidad de frutas compradas en kg
    'Precios': [10, 14, 16, 20, 6, 12, 25, 30, 8, 18]  # Precio total
})

# ==============================================================================
##################################
# Separar las características (X) y la variable objetivo (y)
X = data[['Kilogramos_Frutas']]  # X son las cantidades de frutas en kg
y = data['Precios']  # y son los precios totales


# ==============================================================================
##################################
# Crear un objeto de modelo de regresión lineal
modelo = LinearRegression() #OBJETO: Es una abstraccion de la realidad pasada a codigo

#NOTA(modelo?): Queremos aproximarnos a saber los precios de las frutas,
#       a traves de una "MAQUINA"= el objeto "modelo"


# ==============================================================================
##################################
# Entrenar el modelo con los datos
modelo.fit(X, y)

#NOTA(fit?):
  #_1: Nosotros le mostramos a la "MAQUINA" algunos EJEMPLOS (datos= dataframe (data set)=x e y= vectores)
  #     de frutas y sus precios

  #_2: La "MAQUINA" observa estos ejemplos y trata de aprender como los precios de las frutas, estan relacionados
  #     con cuantos kilogramos de frutas hay



# ==============================================================================
##################################
# Realizar predicciones de precios para nuevas cantidades de frutas
kilogramos_prediccion = np.array([11, 13, 16]).reshape(-1, 1)  # Nuevas cantidades de frutas
#NOTA: Reshape:  Redimensiona, ORGANIZA LOS DATOS para que la maquina pueda entenderlos mejor
print(kilogramos_prediccion)



precio_prediccion = modelo.predict(kilogramos_prediccion)
#NOTA(Prediccion): Despues de que la maquina ha aprendido, le damos un numero de kilogramos de frutas,
                  # y le pedimos que "ADIVINE" cuanto le costaria (la maquina usa lo que ha aprendido
                  #   para hacer mejor su conjetura)


# ==============================================================================
##################################
# Visualizar los resultados de la regresión lineal
plt.scatter(X, y, color='blue', label='Datos reales')  # Graficar los datos reales
plt.plot(kilogramos_prediccion, precio_prediccion, color='red', linewidth=2, label='Regresión Lineal')  # Graficar la regresión lineal
plt.xlabel('Kilogramos de Frutas')  # Etiqueta del eje X
plt.ylabel('Precio (dólares)')  # Etiqueta del eje Y
plt.legend()  # Mostrar la leyenda
plt.title('Regresión Lineal para Predecir el Precio de las Frutas')  # Título del gráfico


# ==============================================================================
##################################
# Imprimir las predicciones
for i in range(len(kilogramos_prediccion)):
    print(f"Para {kilogramos_prediccion[i]} kg de frutas, el precio estimado es de ${precio_prediccion[i]:.2f}")


##################################
# Mostrar la gráfica
plt.show()  # Mostrar el gráfico en pantalla


"""
Explicación de la Regresión Lineal:

La regresión lineal es una técnica que se utiliza para encontrar una relación lineal entre dos variables.
En este caso, estamos tratando de predecir el precio total de las frutas (variable dependiente) en función
de la cantidad de kilogramos comprados (variable independiente).

1- Creamos un DataFrame con los datos de frutas, donde tenemos dos columnas: "Kilogramos_Frutas" y "Precios".

2- Separamos los datos en características (X) y la variable objetivo (y). Las características son las cantidades
de kilogramos de frutas, y la variable objetivo es el precio total.

3- Creamos un modelo de regresión lineal (LinearRegression) y lo entrenamos utilizando las características (X) y
la variable objetivo (y).

4- Realizamos predicciones de precios para nuevas cantidades de frutas utilizando el modelo entrenado.

5- Visualizamos los resultados en un gráfico que muestra los datos reales como puntos azules y la línea roja que
representa la regresión lineal.

6- Finalmente, imprimimos las predicciones de precios para las nuevas cantidades de frutas.
"""