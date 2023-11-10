# importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as LinearRegression

# forma 1=importar el data set desde git hub
# forma 2=simular un dataframe,creando el dataframe
# se conbina una matriz numeral con un vector que contenga el nombre de las columnas de la matriz que creamos

#creamos el dataframe
fruta_data = np.array([[10,100,8],[15,150,7],[8,120,9],[12,110,6]

]) #np.array =sirve para vectores y matricez

frutas_df = pd.DataFrame(fruta_data,columns=['Precio','Peso','Dulzura'])

#Mostramos el dataframe original
print(f"Dataframe original:\n{frutas_df}")

#procesamiento y limpieza
frutas_df.isnull().sum()
#eliminamos datos nulos
df_fruta_limpio = frutas_df.dropna()
#obtener estadistica descriptiba
df_fruta_limpio.describe()

#una vez que esta limpio
#Regrecion lineal aprendizage automatico -> modelo supervisado.
x = data['Precio']
y = data['Peso']

#REGRESION LOGISTICA
#CONVERTIMOS LOS DATOS EN COLUMNAS reshape() 

