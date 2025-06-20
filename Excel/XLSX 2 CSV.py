import pandas as pd

# Datei laden (Pfad anpassen)

input_datei_pfad = "C:\\Users\\Falk\\TestData\\InputData.xlsx"

output_datei_pfad = "C:\\Users\\Falk\\TestData\\OutputData.csv"

df = pd.read_excel(input_datei_pfad)

# Inhalt anzeigen
#print(df.head())  # Zeigt die ersten 5 Zeilen der Tabelle

# Inhalt anzeigen
print(df.all)  


# Aktualisiertes DataFrame speichern
#df.to_csv("C:\\Users\\Falk\\TestData\\OutputData.csv", index=False)
df.to_csv(output_datei_pfad, index=False)
