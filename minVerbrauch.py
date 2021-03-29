# Mindestverbrauch auf 100km bestimmen
# Den Fahrer mit dem geringsten Verbrauch loben

import numpy as np
import pandas as pd

def einlesen(excelfile):
    data = pd.ExcelFile("rsc/" + excelfile + ".xlsx")
    file = pd.read_excel(data)
    return file

# Daten einlesen
testdata01 = einlesen("testdata01")

# Einzelne Spalten auslesen
name = testdata01.get("Name")
verbrauch = testdata01.get("Verbrauch / Liter")
kilometer = testdata01.get("Kilometer")

# Den Vrauch in l/100km umrechnen
l_100km = []
for i in range(0, verbrauch.size):
    result = verbrauch.get(i) / kilometer.get(i) * 100
    result = round(result, 3)
    l_100km.append(result)

# Den Verbrauch aufsteigend sortieren
sorted_index = np.argsort(l_100km)
sorted = np.sort(l_100km)

# Die Namen passend zum Verbrauch sortieren
names_sort = []
for i in sorted_index:
   names_sort.append(name.get(i))

final_array = np.array([names_sort, sorted])

# Ergebnis präsentieren
print(final_array)
print("Herzlichen Glückwunsch " + final_array[0][0] + " zum niedrigsten Verbrauch von " + final_array[1][0] + " l/100km!")
