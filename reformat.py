import os
import nltk
from nltk.tokenize import sent_tokenize
import pandas as pd

source = "data/sample/casa_espejos.txt"

with open(source, "r") as f:
    lines = f.readlines()

# remove empty lines
parrafos = [line for line in lines if line.strip() != ""]

matriz_texto = pd.DataFrame(columns=["parrafo", "oracion", "orden_oracion"])

pnum = 0

for parrafo in parrafos:
    oraciones = sent_tokenize(parrafo)
    pnum += 1
    id = f"p{str(pnum).zfill(3)}"
    snum = 0
    for oracion in oraciones:
        snum += 1
        sid = f"s{str(snum).zfill(3)}"
        matriz_texto = pd.concat([matriz_texto, pd.DataFrame({"parrafo": id, "oracion": oracion, "orden_oracion":sid}, index=[0])], ignore_index=True)

# pivot table (file parrafo column orden_oracion)
matriz_texto = matriz_texto.pivot(index="parrafo", columns="orden_oracion", values="oracion")

# save to csv
csv_name = os.path.splitext(source)[0] + ".csv"
matriz_texto.to_csv(csv_name)
