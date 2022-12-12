'''Marche est une liste dont les éléments sont des chaînes, qui sont les noms des supermarchés. 
tous_articles est une liste, les éléments à l'intérieur sont des chaînes, qui sont les noms de tous les produits.
article est une liste, les éléments qu'elle contient sont des chaînes, qui sont les noms des produits à acheter.
Notez que la liste d'articles ne peut pas contenir plus de 10 éléments
prix est une liste, l'élément qu'elle contient est flot, qui est le prix de toutes les marchandises.
 L'ordre des éléments doit être strictement conforme à l'ordre de marche et tous_articles.
L'ordre spécifique est le prix de la première marchandise dans le premier supermarché en marche, 
et le prix du premier supermarché dans le premier supermarché, le prix de la deuxième marchandise, 
et ainsi de suite, puis le prix de la première marchandise dans le deuxième supermarché, et ainsi de suite.
La sortie du programme est un tuple, où le premier élément est le prix le plus bas, 
et le deuxième élément est un tuple où l'élément est une chaîne, qui est le nom du supermarché.
L'ordre des noms est cohérent avec le ordre des marchandises dans l'article,
par exemple dans Dans les résultats de l'exécution des données de test, (12, ('auchan', 'auchan', 'auchan'))
 12 représente le prix le plus bas de 12 euros,le premier auchan signifie pomme acheté à auchan, 
 et le deuxième auchan signifie lait Acheter à auchan,
 le troisième représente sel acheter à auchan
 
 Ajoutez deux paramètres: seul_magasin signifie s'il faut choisir de faire ses achats dans un seul magasin, true signifie oui,
 false signifie que vous pouvez faire vos achats dans plusieurs magasins et la valeur par défaut du paramètre est false.
nombre_article est une liste, l'élément de la liste est int, qui est le nombre d'articles,
 dans l'ordre des articles dans la liste article.

 Ajoutez deux paramètres billette et billet_prix, billette indique s'il faut considérer le prix du billet, 
 vrai signifie à considérer, faux signifie à ne pas considérer, la valeur par défaut est true. 
 billet_prix est le prix du billet, la valeur par défaut est 1,9

 Ajoutez trois paramètres plus_cours, site et mysite, plus_cours indique s'il faut choisir l'itinéraire le plus court, 
 false représente non, true représente oui et la valeur par défaut est false. 
 site est une liste, et les éléments de la liste sont des tuples. Le contenu des tuples sont les coordonnées x et y du magasin. 
 L'ordre d'arrangement des coordonnées du magasin doit être strictement conforme à l'ordre de la liste marche.
 mysite est une liste, les éléments de la liste sont mes coordonnées x et mes coordonnées y, la valeur par défaut est [0,0]

Ajoutez deux paramètres optimale et tendance_optimisation, optimale représente s'il faut choisir la solution optimale,
 false est non, true est oui, la valeur par défaut est false. 
 tendance_optimisation représente la tendance d'optimisation, la valeur est 0, 1, 2. 0 représente le prix préféré , 
 1 représente Aucune préférence, 2 signifie une préférence pour moins de transferts.

 '''
'''Le concepteur importe les valeurs dans la fonction pour obtenir le résultat. 
Parmi eux, marche, tous_articles,article, nombre_article, prix, site, mysite, et prix_billet 
 n'ont pas de valeurs par défaut et nécessitent de saisir manuellement des données spécifiques,
 qui sont des données tabulaires collectées au préalable. Après avoir saisi ces données, saisissez les données du client.
 Les données suivantes sont des données de test, si vous avez besoin de les utiliser ,supprimez ''' ''',
et supprimez ''' ''' dans la dernière ligne et ajoutez un # avant main()'''


from collections import Counter
import random

'''marche=['auchan','lidl','franprix','carrefour','casino']
tous_articles=['pomme','lait','sel','riz','tomate']
article=['pomme','lait','sel']
nombre_article=[1,2,3]
prix=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
moins_cher=False
seul_magasin=False
billet=True
prix_billet=1.9
site=[(1,4),(6,0),(7,3),(5,7),(3,6)]
plus_cours=False
mysite=[5,8]
optimale=True
tendance_optimisation=0'''
'''random.shuffle(prix)
random.shuffle(nombre_article)'''

def main(marche, tous_articles, article, nombre_article, prix,
        site, mysite=[0,0], seul_magasin=False, billet=True,
        prix_billet=1.9, plus_cours=False, moins_cher=False, optimale=False,tendance_optimisation=0):

    tous_article_marche=[]
    #Il s'agit d'une liste dont les éléments sont des tuples de supermarchés et de noms de produits
    for i in range(len(article)):
        for n in range(len(marche)):
            a=tous_articles[i],marche[n]
            tous_article_marche.append(a)
    #print(tous_article_marche)
    article_marche_prix={article_marche:prix for article_marche,prix in zip(tous_article_marche,prix)}
    #Il s'agit d'un dictionnaire où la clé est un tuple de supermarché et d'article et la valeur est le prix.
    #print(article_marche_prix)

    marche_site={marche:site for marche,site in zip(marche,site)}
    #Ceci est un dictionnaire où les clés sont des supermarchés et les valeurs sont des tuples de coordonnées de supermarché



    posibles=[]
    '''Ceci est une liste, les éléments de la liste sont des tuples, et les tuples sont composés de noms de supermarchés,
     et la position du supermarché dans le tuple représente que le produit représenté par la position est acheté dans le supermarché'''
    if len(article)==1:
        for n1 in range(len(marche)):
            a=[marche[n1]]
            a=tuple(a)
            posibles.append(a)
    
    if len(article)==2:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                a=[marche[n1]]
                a.append(marche[n2])
                a=tuple(a)
                posibles.append(a)
    
    if len(article)==3:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                            a=[marche[n1]]
                            a.append(marche[n2])
                            a.append(marche[n3])
                            a=tuple(a)
                            posibles.append(a)

    if len(article)==4:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                            a=[marche[n1]]
                            a.append(marche[n2])
                            a.append(marche[n3])
                            a.append(marche[n4])
                            a=tuple(a)
                            posibles.append(a)

    if len(article)==5:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            a=[marche[n1]]
                            a.append(marche[n2])
                            a.append(marche[n3])
                            a.append(marche[n4])
                            a.append(marche[n5])
                            a=tuple(a)
                            posibles.append(a)
    
    if len(article)==6:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            for n6 in range(len(marche)):
                                a=[marche[n1]]
                                a.append(marche[n2])
                                a.append(marche[n3])
                                a.append(marche[n4])
                                a.append(marche[n5])
                                a.append(marche[n6])
                                a=tuple(a)
                                posibles.append(a)
    
    if len(article)==7:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            for n6 in range(len(marche)):
                                for n7 in range(len(marche)):
                                    a=[marche[n1]]
                                    a.append(marche[n2])
                                    a.append(marche[n3])
                                    a.append(marche[n4])
                                    a.append(marche[n5])
                                    a.append(marche[n6])
                                    a.append(marche[n7])
                                    a=tuple(a)
                                    posibles.append(a)
    if len(article)==8:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            for n6 in range(len(marche)):
                                for n7 in range(len(marche)):
                                    for n8 in range(len(marche)):
                                        a=[marche[n1]]
                                        a.append(marche[n2])
                                        a.append(marche[n3])
                                        a.append(marche[n4])
                                        a.append(marche[n5])
                                        a.append(marche[n6])
                                        a.append(marche[n7])
                                        a.append(marche[n8])
                                        a=tuple(a)
                                        posibles.append(a)
    
    if len(article)==9:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            for n6 in range(len(marche)):
                                for n7 in range(len(marche)):
                                    for n8 in range(len(marche)):
                                        for n9 in range(len(marche)):
                                            a=[marche[n1]]
                                            a.append(marche[n2])
                                            a.append(marche[n3])
                                            a.append(marche[n4])
                                            a.append(marche[n5])
                                            a.append(marche[n6])
                                            a.append(marche[n7])
                                            a.append(marche[n8])
                                            a.append(marche[n9])
                                            a=tuple(a)
                                            posibles.append(a)
    
    if len(article)==10:
        for n1 in range(len(marche)):
            for n2 in range(len(marche)):
                for n3 in range(len(marche)):
                    for n4 in range(len(marche)):
                        for n5 in range(len(marche)):
                            for n6 in range(len(marche)):
                                for n7 in range(len(marche)):
                                    for n8 in range(len(marche)):
                                        for n9 in range(len(marche)):
                                            for n10 in range(len(marche)):
                                                a=[marche[n1]]
                                                a.append(marche[n2])
                                                a.append(marche[n3])
                                                a.append(marche[n4])
                                                a.append(marche[n5])
                                                a.append(marche[n6])
                                                a.append(marche[n7])
                                                a.append(marche[n8])
                                                a.append(marche[n9])
                                                a.append(marche[n10])
                                                a=tuple(a)
                                                posibles.append(a)
    #print(posibles)


        


    tousprixs={} 
    '''Ceci est un dictionnaire, la clé est constituée de la possibilité du supermarché, 
    et la valeur est le coût total des achats sous cette possibilité'''
    if moins_cher==True :   
    #Le code suivant indique que l'utilisateur a sélectionné le plan le plus favorable               
        if seul_magasin==False:
        #Le code suivant indique que l'utilisateur n'a pas choisi d'acheter dans un seul magasin                   
            for i in posibles:
                n=0
                prixs=0
                while n<len(article) :
                    prixs=prixs+article_marche_prix.get((article[n],i[n]))*nombre_article[n]
                    n+=1
                if n==len(article):
                #Le code suivant indique si l'utilisateur choisit de prendre en compte le prix du billet
                    if billet==False:
                        tousprixs[i] = prixs
                    if billet==True:
                        tousprixs[i] = prixs+prix_billet*(len(dict(Counter(i)))+1)

            solution = min(zip(tousprixs.values(),tousprixs.keys())) 
            #print(tousprixs)

        if seul_magasin==True:
            for i in marche:
                n=0
                prixs=0
                while n<len(article) :
                    prixs=prixs+article_marche_prix.get((article[n],i))*nombre_article[n]
                    n+=1
                if n==len(article):
                    if billet==False:
                        tousprixs[i] = prixs
                    if billet==True:
                        tousprixs[i] = prixs+prix_billet*2
            solution = min(zip(tousprixs.values(),tousprixs.keys()))
    
    Poids={}
    '''Dans le plan optimal complet, la pondération est utilisée pour mesurer la qualité d'un plan. 
    Il s'agit d'un dictionnaire. La clé du dictionnaire est le plan d'achat et la valeur est la valeur de pondération du plan.
     Plus la valeur de pondération est petite, meilleur est le plan.'''
    if optimale==True:
    #Cette ligne de code représente le choix de l'utilisateur de la solution optimale
        for i in posibles:
            n=0
            prixs=0
            while n<len(article) :
                prixs=prixs+article_marche_prix.get((article[n],i[n]))*nombre_article[n]
                n+=1
            if n==len(article):
                if billet==False:
                    tousprixs[i] = prixs   
                if billet==True:
                    tousprixs[i] = prixs+prix_billet*(len(dict(Counter(i)))+1)
            #Le code suivant représente la préférence d'optimisation sélectionnée par l'utilisateur
            if  tendance_optimisation==0:    
                a=0.9 
            if  tendance_optimisation==1:     
                a=0.7
            if  tendance_optimisation==2:
                a=0.5
            Poids[i]= tousprixs[i]/max(tousprixs.values()) *a+len(dict(Counter(i)))/len(marche)*(1-a)
            
        solution = tousprixs[list(min(zip(Poids.values(),Poids.keys())))[1]],list(min(zip(Poids.values(),Poids.keys())))[1]


    if plus_cours==True:
    #Cette ligne indique que l'utilisateur a sélectionné le plan avec la distance la plus proche
        value_sites=[]
        for i in site:
            value_site=((list(i)[0]-mysite[0])**2) + ((list(i)[1]-mysite[1])**2)
            value_sites.append(value_site)
        #print(value_sites)
        value_site_marche={value_sites:marche for value_sites,marche in zip(value_sites,marche)}
        min_value_site=min(value_site_marche)
        n=0
        prixs=0
        while n<len(article) :
            prixs=prixs+article_marche_prix.get((article[n],value_site_marche[min_value_site]))*nombre_article[n]
            n+=1
        if n==len(article):
            if billet==False:
                solution=prixs,value_site_marche[min_value_site]
            if billet==True:
                solution=prixs+prix_billet*2,value_site_marche[min_value_site]
            


        









    print(solution)
    return solution



if __name__ == '__main__':
    main()
    '''main(marche, tous_articles, article, nombre_article, prix,
        site, mysite, seul_magasin, billet,
        prix_billet, plus_cours, moins_cher, optimale,tendance_optimisation)'''



    
