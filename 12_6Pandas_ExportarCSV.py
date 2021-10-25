import pandas as pd
import random
SEPARADOR = ("*" * 20) + "\n"

#Creacion de un DataFrame a partir de un diccionario
diccionario_notas_aleatorias = { \
    "Crescencio":[random.randrange(60, 101) for x in range(4)], \
    "Domitila":[80, 100, 57, 90], "Rutilio":[80, 70, 57, 90], "Panfilo":[20, 100, 100, 90], \
    "Ludoviko":[100, 100, 100, 90], "Geraldine": [90, 90, 90, 90], "Eduardo":[90, 90, 90, 90], \
    "Luis":[90, 90, 90, 90]}
notas = pd.DataFrame(diccionario_notas_aleatorias)
notas.index = ["Programacion", "Base de datos", "Contabilidad", "Estructura de datos"]


notas.to_csv (r'notas.csv',index=True, header=True)  #No olvidar la extension del archivo
print("¡EXITO!")