import csv

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

print("Marché A:", MarcheA)

with open('testDataStruct.csv', 'w', newline='') as fichierCSV:
    writer = csv.writer(fichierCSV)
    writer.writerow(MarcheA)
    writer.writerow(MarcheB)
    writer.writerow({'This':'is', 'aNew':'Row'})


with open('testDataStruct.csv', 'r') as fichierCSVIN:
    for ligne in fichierCSVIN:
        print("fichier CSV:", ligne)
