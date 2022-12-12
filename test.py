import csv
import pandas as pd
import numpy

print("Hello world")

print("Different from main")

print("Making a commit, you need to update")




distanceAB = 10
distances = [distanceAB]
listeProduits = ["oeuf", "pate", "fromage"]
prixProduits = [3, 2, 5]

MarcheA = [distances, listeProduits, prixProduits]

distanceAB = 10
distancesB = [distanceAB]
listeProduits = ["tomate", "poulet", "fromage"]
prixProduits = [6, 8, 5]

MarcheB = [distancesB, listeProduits, prixProduits]
'''
print("Marché A:", MarcheA)

with open('testDataStruct.csv', 'w', newline='') as fichierCSV:
    writer = csv.writer(fichierCSV)
    writer.writerow(MarcheA)
    writer.writerow(MarcheB)
    writer.writerow({'This':'is', 'aNew':'Row'})


with open('testDataStruct.csv', 'r') as fichierCSVIN:
    for ligne in fichierCSVIN:
        print("fichier CSV:", ligne)



with open('prixProduits.csv', 'r') as fichierIN:
    for ligne in fichierIN:
        print("fichier CSV Prix Produits:", ligne)

'''

data = pd.read_excel(r'prix des produits.xlsx')
print(data)

columnData = pd.read_excel(r'prix des produits.xlsx', index_col=0)
print(columnData)

columnData = pd.read_excel(r'prix des produits.xlsx',
                            dtype= {"produit ": str,
                            "Prix": float})
print("Testing Head:")
print(columnData)

df = pd.DataFrame(data, columns=['produit ', 'prix'])
print("Printing Data Frame:")
print(df)
print("Printing df['produit'] column:")
print(df.index)

print("Printing df.loc location:")
print(df.loc(0))
#?????

#df[df["produit "]] == 'œufs'.head