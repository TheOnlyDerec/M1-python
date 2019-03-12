def crible(n):
    L=list(range(2,n)) #Liste des candidats
    p=2  #Premier nombre premier
    while True : #Calcul en boucle
        for i in range(2*p,max(L)+1,p):  #Multiples de p
            if i in L:
                L.remove(i) #On marque i si il est dans la liste
        try:
            p=L[L.index(p)+1] #Nouveau p
        except:
            return L #Si p est hors de la liste fin de la fonction


def crible2(n):
    L=list(range(2,n)) #Liste des candidats
    mark=[False for _ in range (2,n)]
    p=2  #Premier nombre premier
    while True : #Calcul en boucle
        mark[0:n-2:p]=True #Dire slice=true pour chaque elt
        try:
            p=L[L.index(p)+1] #Nouveau p
        except:
            for i in range(2,n): #Si p est hors de la liste fin de la fonction
                if not mark[i]:
                    return L[i]


Liste=crible2(100)
print(Liste)