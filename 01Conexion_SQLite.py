import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("PrimerIntentDemo.db") as conn:
        print(sqlite3.version)
except Error as e:
    print (e)

#El bloque with es un MANEJADOR DE CONTEXTO