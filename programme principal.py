import algorithme
from base_donnéespy import *

marche=['AUCHAN','MONOPRIX','FRANPRIX','LECLERC','CARREFOUR']
tous_articles=list(AUCHAN['produit'])
#print(tous_articles)
prix=list(AUCHAN['prix'])+list(MONOPRIX['prix'])+list(FRANPRIX['prix'])+list(LECLERC['prix'])+list(CARREFOUR['prix'])
nombre_article=[]
article=[]
moins_cher=False
optimale=False
tendance_optimisation=0
plus_cours=False
seul_magasin=False
billet=True
prix_billet=1.9
site=[(1,4),(6,0),(7,3),(5,7),(3,6)]
mysite=[0,0]


Option1=str(input('''Quelle option d'optimisation souhaitez-vous choisir ?
    La première option : le meilleur prix
    La deuxième option : la distance la plus courte, pas de transfert
    La troisième option: optimale complète'''))
if Option1=='1' or 'La première option':
    moins_cher=True
    Option1_1=str(input('Acheter que dans un seul magasin ?'))
    if Option1_1=='oui':
        seul_magasin=True
    Option1_2=str(input('Avez-vous besoin de considérer le prix du billet?'))
    if Option1_2=='non':
        billet=False

elif Option1=='2' or 'La deuxième option':
    plus_cours=True
    Option1_1=str(input('Avez-vous besoin de considérer le prix du billet?'))
    if Option1_1=='non':
        billet=False

elif Option1=='3' or 'La troisième option':
    optimale=True
    Option1_1=int(input('''Ou est-ce une optimisation qui favorise les transferts, ou une optimisation plus équilibrée ?
Veuillez entrer 1 pour un prix biaisé
Veuillez entrer 2 pour un solde partiel
Si vous préférez réduire le transfert, veuillez entrer 3'''))
    tendance_optimisation=Option1_1
    Option1_2=str(input('Avez-vous besoin de considérer le prix du billet?'))
    if Option1_2=='non':
        billet=False

print(moins_cher,optimale,plus_cours,seul_magasin,billet)