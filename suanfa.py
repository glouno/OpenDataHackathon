
'''marche=[1,2,3]

article=[1,2,3,4,5]

prix=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]'''

def main(marche,article,prix):
    article_marche=[]
    for i in range(len(article)):
        for n in range(len(marche)):
            a=article[i],marche[n]
            article_marche.append(a)
    #print(article_marche)
    article_marche_prix={article_marche:prix for article_marche,prix in zip(article_marche,prix)}
    #print(article_marche_prix)

    posibles=[]
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
                        #print(b)
    tousprixs={}
    for i in posibles:
        n=0
        prixs=0
        while n<5 :
            prixs=prixs+article_marche_prix.get((article[n],i[n]))
            n+=1
        if n==5:
            tousprixs[i] = prixs
    #print(tousprixs)
    min_prixs = min(zip(tousprixs.values(),tousprixs.keys()))
    print(min_prixs)













if __name__ == '__main__':
    main()
    #main(marche,article,prix)



    
