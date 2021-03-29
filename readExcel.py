# Ein paar Versuche mit numpy, matplotlib und pandas
# Excel Datei einlesen und weiterverarbeiten

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

list_name = []
list_kil = []

# Einlesen der Excel-Datei
testdata01 = pd.ExcelFile("rsc/testdata01.xlsx")
file = pd.read_excel(testdata01)

# Einzelne Spalten erhalten
name = file.get("Name")
kil = file.get("Kilometer")

# Array erzeugen
array_kil = np.array(kil)

# Listen erzeugen
for i in kil:
    list_kil.append(i)

for i in name:
    list_name.append(i)

print(list_name)
print(list_kil)

# Größter Wert
print(np.max(array_kil))

# Plot-Kilometer
plt.plot(list_kil)
plt.show()