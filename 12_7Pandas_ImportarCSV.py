import pandas as pd
SEPARADOR = ("*" * 20) + "\n"

notas = pd.read_csv("notas.csv", index_col=0)

print(notas)
print(SEPARADOR)