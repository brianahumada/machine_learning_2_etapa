import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Forma 1 Importar el data set desde GIT HUB


#Forma 2 SIMULAR UN DATA FRAME, creando el DATAFRAME (como se hace esto:
# se combina una matriz numeral con un vector que contiene el nombre de las columnas de la matriz quye creamos))

# Crear data frame con los datos simulados de un data set de frutas
#np.array sirve tanto para vectores como matrices
fruta_data=np.array([ [10, 100, 8],[15, 150, 7],[8, 120, 9],[12, 110, 6] #PRECIO, PESO, DULZURA
                     
    
])
frutas_df = pd.DataFrame(fruta_data, columns=['Precio','peso','Dulzura'])

#mostrar el data frame original
print("data frame original: ")
print(frutas_df)

#Preprocesamiento y LIMPIEZA valores nulos lo sumamos
frutas_df.isnull().sum()
#eliminamos valores nulos
data_frame_limpio = frutas_df.dropna()




#------ VECTOR -------
#Vector [10, letras, etc]

#Vector:

# [111, 25, 64, 55]

#-------- MATRIX: Un vector sobre otro vector= Tipo excel: COLUMNAS Y FILAS -----------
# [111, 25, 64, 55]
# [66, 25, 64, 55]