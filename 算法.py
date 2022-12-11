'''Marche est une liste dont les éléments sont des chaînes, qui sont les noms des supermarchés. 
tous_articles est une liste, les éléments à l'intérieur sont des chaînes, qui sont les noms de tous les produits.
article est une liste, les éléments qu'elle contient sont des chaînes, qui sont les noms des produits à acheter.
prix est une liste, l'élément qu'elle contient est flot, qui est le prix de toutes les marchandises.
 L'ordre des éléments doit être strictement conforme à l'ordre de marche et tous_articles.
L'ordre spécifique est le prix de la première marchandise dans le premier supermarché en marche, 
et le prix du premier supermarché dans le premier supermarché, le prix de la deuxième marchandise, 
et ainsi de suite, puis le prix de la première marchandise dans le deuxième supermarché, et ainsi de suite.'''

'''marche=['auchan','lidl','franprix']

tous_articles=['pomme','lait','sel','riz','tomate']

article=['pomme','lait','sel']

prix=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]'''



def main(marche,tous_articles,article,prix):
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
    for i in posibles:
        n=0
        prixs=0
        while n<len(article) :
            prixs=prixs+article_marche_prix.get((article[n],i[n]))
            n+=1
        if n==len(article):
            tousprixs[i] = prixs
    #print(tousprixs)
    min_prixs = min(zip(tousprixs.values(),tousprixs.keys()))
    print(min_prixs)
    return min_prixs













if __name__ == '__main__':
    main()
    #main(marche,tous_articles,article,prix)



    
