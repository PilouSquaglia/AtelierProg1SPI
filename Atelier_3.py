# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:39:31 2021

@author: Pilou
"""

def somme1(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste
 
inputs:
    L: [int]
    
outputs:
    somme: int"""
    somme=0
    
    for i in L:
        somme+=i
        
    return somme

def somme2(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste

inputs:
    L: [int]
    
outputs:
    somme: int"""
    somme=0
    
    for i in range(len(L)):
        somme+=L[i]
        
    return somme

def somme3(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste

inputs:
    L: [int]
    
outputs:
    somme: int"""
    i=0
    somme=0
    while i<len(L):
        somme+=L[i]
        i+=1
    return somme
    


def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme3([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 11111 : ", somme3(S))
    #test somme 129
    S=[20,9,100]
    print("Test somme 129 : ", somme3(S))
    
    
    
#test_exercice1()

def moyenne(L:list) -> float:
    
    """admet en paramètre une liste d'entiers L et renvoie la
moyenne des valeurs de la liste . La fonction doit renvoyer 0 si la liste est vide.

inputs:
    L: [int]
    
outputs:
    moyenne: float"""
    
    somme=0
    if L==[]:
        moyenne=0
    else:
        for i in L:
            somme+=i
            moyenne=somme/len(L)
    
    return moyenne

#print(moyenne([20,9,100]))

def nb_sup(L:int, e:int) -> str:
    
    """admet en paramètre une liste d'entiers L et un entier e et
retourne le nombre de valeurs strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    : str"""
    res=0
    for i in L:
        if i>e:
            res+=1
    return "Il y a {} nombre(s) strictement superieur à {} dans la liste {}".format(res, e, L)

#print(nb_sup([20,9,100], 1000))

def nb_sup2(L:int, e:int) -> int:
    
    """admet en paramètre une liste d'entiers L et un entier e et
retourne le nombre de valeurs strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    : str"""
    res=0
    for i in range(len(L)):
        if L[i]>e:
            res+=1
    return "Il y a {} nombre(s) strictement superieur à {} dans la liste {}".format(res, e, L)

#print(nb_sup2([20,9,100], 10)) 

def moy_sup(L:list, e:int) -> float:
    
    """admet en paramètre une liste d'entiers L et un entier e,
et retourne la moyenne des valeurs de la liste strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    moyenne: float"""

    res=0
    index=0
    for i in L:
        if i>e:
            res+=i
            index+=1
    moyenne=res/index
    return moyenne

#print(moy_sup([12,5,3,15], 4))

def val_max(L:list) -> int:
    
    """prend en paramètre une liste d'entiers et retourne la valeur
maximale de cette liste

inputs:
    L: [int]
    
outputs:
    max: int"""
    
    if L==[]:
        max=0
    else:
        max=L[0]
        for i in L:
            if i>max:
                max=i
        return max

#print(val_max([]))

def ind_max(L:list) -> int:
    
    """prend en paramètre une liste d'entiers et retourne l'indice
de l'élément maximal de cette liste

inputs:
    L: [int]
    
outputs:
    ind_max: int"""
    if L==[]:
        max=0
    else:
        max=L[0]
        for i in L:
            if i>max:
                max=i
            ind_max=L.index(max)
        
        return ind_max

#print(ind_max([28, 19, 15]))

#Exercice 2

def position_for(L:list, e:int) -> int:
    
    """admet en paramètres une liste L d'entiers et un entier e et
retourne l'indice de l'entier e dans la liste L.

inputs: 
    L:[int]
    e:int
    
outputs:
    
    index_e:int"""
    if L==[]:
        res="Liste vide"
    else:
        res=-1
        index_e=L[0]
        for i in L:
            if i==e:
                index_e=i
                res=L.index(index_e)
                return res

#print(position_for([9, 5, 7], 7))

def position_while(L:list, e:int) -> int:
    
    """admet en paramètres une liste L d'entiers et un entier e et
retourne l'indice de l'entier e dans la liste L.

inputs: 
    L:[int]
    e:int
    
outputs:
    
    index_e:int"""
    
    if L==[]:
        res="Liste vide"
    else:
        res=-1
        index_e=L[0]
        i=0
        cond=True
        while i<len(L) and cond:
            if L[i]==e:
                index_e=L[i]
                cond=False 
                res=L.index(index_e)
            i+=1   
    return res

#print(position_while([4,3,6], 6))

def nb_occurence(L:list, e:int) -> int:
    """
    admet en paramètres une liste L d'entiers et un
entier e, et retourne le nombre d'occurrences de l'entier e dans la liste L

    Parameters
    ----------
    L : list
       
    e : int
        

    Returns
    -------
    res : int
        DESCRIPTION.

    """
    if L==[]:
        res="Liste vide"
    else:
        occurence_e=0
        res=0
        for i in L:
            if i==e:
                occurence_e+=1
                res=occurence_e
    return res
    
#(nb_occurence([], 0))

def est_triee(L:list) -> bool:
    """
    admet en paramètres une liste L d'entiers et retourne un
booléen vrai si la liste est triée par ordre croissant, faux sinon.

    Parameters
    ----------
    L : [int]
        

    Returns
    -------
    res : bool
    """
    if L==[]:
        res="Liste vide"
    else:
        res=True
        for i in range(1,len(L)):
            if L[i]<L[i-1]:
                res=False
    return res

#print(est_triee([0, 1, 2, 3]))







    
    
    
    

           
        



































