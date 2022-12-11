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
 '''

marche=['auchan','lidl','franprix']
tous_articles=['pomme','lait','sel','riz','tomate']
article=['pomme','lait','sel']
nombre_article=[1,2,3]
prix=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]
seul_magasin=False


def main(marche,tous_articles,article,nombre_article,prix,seul_magasin=False):
    tous_article_marche=[]
    for i in range(len(article)):
        for n in range(len(marche)):
            a=tous_articles[i],marche[n]
            tous_article_marche.append(a)
    #print(article_marche)
    article_marche_prix={article_marche:prix for article_marche,prix in zip(tous_article_marche,prix)}
    #print(article_marche_prix)





    posibles=[]
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


    tousprixs={}                    
    if seul_magasin==False:                    
        for i in posibles:
            n=0
            prixs=0
            while n<len(article) :
                prixs=prixs+article_marche_prix.get((article[n],i[n]))*nombre_article[n]
                n+=1
            if n==len(article):
                tousprixs[i] = prixs
        min_prixs = min(zip(tousprixs.values(),tousprixs.keys())) 
        #print(tousprixs)
    if seul_magasin==True:
        for i in marche:
            n=0
            prixs=0
            while n<len(article) :
                prixs=prixs+article_marche_prix.get((article[n],i))*nombre_article[n]
                n+=1
            if n==len(article):
                tousprixs[i] = prixs
        min_prixs = min(zip(tousprixs.values(),tousprixs.keys()))

    print(min_prixs)
    return min_prixs



if __name__ == '__main__':
    #main()
    main(marche,tous_articles,article,nombre_article,prix,seul_magasin)



    
