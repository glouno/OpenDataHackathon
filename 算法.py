marche=['a','b','c']

article=[1,2,3,4,5]

prix=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


article_marche_prix=[]
for i in range(len(article)):
    for n in range(len(marche)):
        b=i*len(marche)+n
        a=[article[i],marche[n],prix[i*len(marche)+n]]
        article_marche_prix.append(a)
#print(article_marche_prix)
'''q=[]
for i in article_marche_prix:
    
    if i[1]=='b':
        q.append(i)
print(q)'''

'''def al (n=0,articles=[]):
    if n<len(article):
        for i in marche:
            articles.append(marche)
            return al
        n=+1
    if n>=len(article):
        return articles
al (n=0,articles=[])
print(al (n=0,articles=[]))'''
b=[]
c=[]
d=[]
e=[]
f=[]

for i in range(len(marche)):
    a=[marche[i]]
    b.append(a)
for n in range(len(marche)):
    #print(b[n])
    for i in range(len(marche)):
        a=marche[i]
        B=b[n]
        #B=B.append(a)
        c.append(B)
        print(B)
'''for i3 in range(len(marche)):
    a=[marche[i]]
    e.append()
    
for i4 in range(len(marche)):
    b=[]
    a=[marche[i]]
    c.append(b.append(a))
for i5 in range(len(marche)):
    a=[marche[i]]
    b.append(a)'''
print(c)
print(len(c))

#modifier




    
