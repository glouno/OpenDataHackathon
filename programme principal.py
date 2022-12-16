from algorithme import *
from base_donnéespy import *

marche=['AUCHAN','MONOPRIX','FRANPRIX','LECLERC','CARREFOUR']
tous_articles=list(AUCHAN['produit'])
#print(tous_articles)
unite=list(AUCHAN['unité'])
prix=list(AUCHAN['prix'])+list(MONOPRIX['prix'])+list(FRANPRIX['prix'])+list(LECLERC['prix'])+list(CARREFOUR['prix'])
#print(prix)
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
article_unite={tous_articles:unite for tous_articles,unite in zip(tous_articles,unite)}
articles_unite=[]

def seulmag():
    a=str(input('Acheter que dans un seul magasin ? Oui ou non :'))
    if a=='oui':
        return 'oui'
    elif a=='non':
        return 'non'
    else :
        print('''Vous n'avez inscrit ni oui ni non. Veuillez réessayer''')
        return seulmag()

def sibillet():
    a=str(input('Avez-vous besoin de considérer le prix du billet? Oui ou non :'))
    if a=='oui':
        return 'oui'
    elif a=='non':
        return 'non'
    else :
        print('''Vous n'avez inscrit ni oui ni non. Veuillez réessayer''')
        return sibillet()





    #print('pour choisir la premiére option taper 1; pour choisir la deuxiéme option taper 2; pour choisi la troisiéme option taper 3 ')
Option1=str(input('''Quelle option d'optimisation souhaitez-vous choisir ?
    La première option : le meilleur prix
    La deuxième option : la distance la plus courte, pas de transfert
    La troisième option: optimale complète
    pour choisir la premiére option taper 1; pour choisir la deuxiéme option taper 2; pour choisi la troisiéme option taper 3
    Veuillez entrer 1, 2 ou 3 : '''))

if Option1=='1':
    moins_cher=True
    Option1_1=seulmag()
    if Option1_1=='oui':
        seul_magasin=True
    Option1_2=sibillet()
    if Option1_2=='non':
        billet=False

elif Option1=='2':
    plus_cours=True
    Option1_1=sibillet()
    if Option1_1=='non':
        billet=False

elif Option1=='3':
    optimale=True
    Option1_1=int(input('''
    Le plan entièrement optimisé vous donnera un plan avec des prix moins chers et moins de transferts.
    Dans le cadre de ce plan entièrement optimisé:
    si vous accordez plus d'attention aux prix bon marché qu'aux transferts, veuillez entrer 1 ;
    Si vous souhaitez donner un poids égal à des prix moins chers et à moins de transferts, entrez 2 ;
    Si vous valorisez moins de transferts plus que des prix inférieurs, entrez 3 :'''))
    tendance_optimisation=Option1_1
    Option1_2=sibillet()
    if Option1_2=='non':
        billet=False
    
#print(moins_cher,plus_cours,optimale,seul_magasin,billet)



continuer=True
while continuer==True :
    Option2=str(input('''Qu'avez-vous besoin d'acheter?
     Veuillez entrer les articles que vous devez acheter.
     Entrez non pour terminer :'''))
    if Option2=='non':
        continuer=False
    elif Option2 not in tous_articles:
        print('''Le produit que vous recherchez n'existe pas''')
        continue
    else:
        article.append(Option2)
        articles_unite.append(article_unite[Option2])
        Option3=int(input(f'Quelle est sa quantité ? (Entrez simplement un nombre, unité par défaut est {article_unite[Option2]}) :'))
        nombre_article.append(Option3)
article_nombre_unite=pd.DataFrame()
article_nombre_unite['article'] = article
article_nombre_unite['nombre']= nombre_article
article_nombre_unite['unité']  = articles_unite
print('Votre liste de courses est:')
print(article_nombre_unite)



Option4=str(input('où es tu maintenant (Les points prédéfinis incluent : ECE, Tour Eiffel, Arc de Triomphe, Louvre) :'))
if Option4.lower()=='ece':
    mysite=[0,0]
elif Option4.lower()=='tour eiffel':
    mysite=[1,0]
elif Option4.lower()=='arc de triomphe':
    mysite=[3,1]
elif Option4.lower()=='louvre':
    mysite=[2,9]
#print(Option4.lower(),mysite)

solution=main(marche, tous_articles, article, nombre_article, prix,
        site, mysite, seul_magasin, billet,
        prix_billet, plus_cours, moins_cher, optimale,tendance_optimisation)

result=pd.DataFrame()
result['produit'] = article
#print(list(solution[1]))
result['marche'] = list(solution[1])
print(f'ça coute {round(list(solution)[0],2)} €')
print('''Votre plan d'achat est :''')
print(result)