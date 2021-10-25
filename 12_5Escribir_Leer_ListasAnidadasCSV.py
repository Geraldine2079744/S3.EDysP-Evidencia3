"""El modulo csv implementa clases para leer y escribir datos tabuladores en formato CSV.
Permita a los programadores decir, <<escribir estos datos en el formato preferido por Excel>>
o <<lee datos de este archivo que fue generado por Excel>>, sin conocer los detalles precisos
del formato CSV usado por Excel."""

import csv

columnas = ("Clave", "Nombre", "Correo")
datos = [[1, "Rodimiro", "rod@gmail.com"],
         [2, "Teofilo", None],
         [3, "Domitila", "domi@gmail.com"]]



with open("datos.csv", "w", newline="") as archivo:
    registrador = csv.writer(archivo)
    registrador.writerow(columnas)
#    for registro in datos:
#        registrador.writerow(registro)
    registrador.writerows(datos)



columnas = None
datos = list()



with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo, delimiter = ",")
    registros = 0

    for clave, nombre, correo in lector:
        if registros == 0:
            columnas = (clave, nombre, correo)
            registros = registros + 1
        else:
            clave = int(clave)
            datos.append([clave, nombre, correo])

print(datos)