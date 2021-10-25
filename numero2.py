"""Escribir una funcion que reciba un diccionario con las notas de los alumnos
   en curso en un examen y devuelva una serie con la nota minima, la maxima, media
   y la desviacion tipica."""

import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadistica = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviacion tipica'])
    return estadistica

notas = {'Juan':9, 'Maria':6.5, 'Pedro':4, 'Carmen':8.5, 'Luis':5}
print(estadistica_notas(notas))