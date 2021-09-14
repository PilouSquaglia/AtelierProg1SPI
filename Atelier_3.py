# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:39:31 2021

@author: Pilou
"""

def somme1(L:[int]) -> int:
    
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

def somme2(L:[int]) -> int:
    
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

def somme3(L:[int]) -> int:
    
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
        moy=0
    else:
        for i in L:
            somme+=i
            moy=somme/len(L)
    return moy

#print(moyenne([20,9,100]))

def nb_sup(L:list, e:int) -> int:
    
    """admet en paramètre une liste d'entiers L et un entier e et
retourne le nombre de valeurs strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    res : int"""
    compt=0
    for i in L:
        if i>e:
            compt+=1
    #return "Il y a {} nombre(s) strictement superieur à {} dans la liste {}".format(compt, e, L)
    return compt
#print(nb_sup([20,9,100], 1000))

def nb_sup2(L:int, e:int) -> str:
    
    """admet en paramètre une liste d'entiers L et un entier e et
retourne le nombre de valeurs strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    res : str"""
    compt=0
    for i in range(len(L)):
        if L[i]>e:
            compt+=1
    return "Il y a {} nombre(s) strictement superieur à {} dans la liste {}".format(compt, e, L)

#print(nb_sup2([20,9,100], 10)) 

def moy_sup(L:list, e:int) -> float:
    
    """admet en paramètre une liste d'entiers L et un entier e,
et retourne la moyenne des valeurs de la liste strictement supérieures à e

inputs:
    L: [int]
    e: int
    
outputs:
    moy: float"""

    somme=0
    compt=0
    if L==[]:
        moy=0
    else:
        moy=0
        for i in L:
            if i>e:
                somme+=i
                compt+=1
                moy=somme/compt 
    return moy

#print(moy_sup([12,5,3,15], 4))

def val_max(L:list) -> int:
    
    """prend en paramètre une liste d'entiers et retourne la valeur
maximale de cette liste

inputs:
    L: [int]
    
outputs:
    maxi: int"""
    
    if L==[]:
        maxi=0
    else:
        maxi=L[0]
        for i in L:
            if i>maxi:
                maxi=i
    return maxi

#print(val_max([]))

def ind_max(L:list) -> int:
    
    """prend en paramètre une liste d'entiers et retourne l'indice
de l'élément maximal de cette liste

inputs:
    L: [int]
    
outputs:
    ind_max: int"""
    if L==[]:
        ind_max=0
    else:
        max=L[0]
        for i in L:
            if i>max:
                max=i
        ind_max=L.index(max)
        
    return ind_max

#print(ind_max([28, 19, 115]))

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
        res=0
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
        res=0
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

#print(position_while([4,3,6], 4))

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
        res=0
    else:
        occurence_e=0
        res=0
        for i in L:
            if i==e:
                occurence_e+=1
                res=occurence_e
    return res
    
#(nb_occurence([], 0))

def est_triee_for(L:list) -> bool:
    """
    admet en paramètres une liste L d'entiers et retourne un
booléen vrai si la liste est triée par ordre croissant, faux sinon version for.

    Parameters
    ----------
    L : [int]
        

    Returns
    -------
    res : bool
    """
    if L==[]:
        res=False
    else:
        res=True
        for i in range(1,len(L)):
            if L[i]<L[i-1]:
                res=False
    return res

#print(est_triee_for([0, 1, 2, 3]))

def est_triee_while(L:list) -> bool:
    """
    admet en paramètres une liste L d'entiers et retourne un
booléen vrai si la liste est triée par ordre croissant, faux sinon version while.

    Parameters
    ----------
    L : [int]

    Returns
    -------
   res : bool
        

    """
    
    if L==[]:
        res=False
    else:
        i=0
        res=True
        while i<len(L)-1 and res:
            if L[i]>L[i+1]:
                res=False 
            i+=1   
    return res
    
#print(est_triee_while([0, 1, 2 , 3]))   

def position_tri(L:list, e:int) -> int:
    """
    

    Parameters
    ----------
    L : [int]
    e : int

    Returns
    -------
    res : int
        

    """

    if L==[]:
        res=0
    else:
        res=-1
        index_e=L[0]
        i=len(L)/2
        while res!=e:
            if L[i]>e:
                index_e=L[i]
                res=L.index(index_e)
                i/=2
                
    #A finir
    return res

def a_repetition(lst:list) -> bool:
    """
    admet en paramètres une liste lst d'entiers et retourne
un booléen True si la liste lst comporte des répétitions de valeurs et False sinon
    

    Parameters
    ----------
    lst : list
    
    Returns
    -------
    res : bool
        DESCRIPTION.

    """
    lst_t=[]
    i=0
    res=False
    while i<len(lst) and res==False:
        if lst[i] not in lst_t:
            lst_t.append(lst[i])
        else:
            res=True
        i+=1
    return res 

#print(a_repetition([0, 1, 4, 1]))


#Exercice 3

def separer(lst:list) -> list:
    """
    prend en paramètre une liste d'entiers lst et retourne la
        liste lst_sep avec les nombre négatifs à gauche,
            les nombres positifs à droite et les
                nombres nuls au milieu
    

    Parameters
    ----------
    lst : list[int]
    
    Returns
    -------
    lst_sep : list[int]

    """
    lst_sep=[]
    lst_n=[]
    lst_p=[]
    i=0
    while i<len(lst):
        if lst[i]<0:
            lst_sep.append(lst[i])
        elif lst[i]==0:
            lst_n.append(lst[i])
        elif lst[i]>0:
            lst_p.append(lst[i])
        i+=1
    lst_sep.extend(lst_n)
    lst_sep.extend(lst_p)
    return lst_sep

#print(separer([-1, 2, 0, -3, 4, 6, -7]))                
        

#Exercice 4


def histo(lst_f:list) -> list:
    """
    admet en paramètre la liste d'entiers lst_f définissant une fonction et renvoie une
liste d'entiers lst_h représentant l'histogramme de lst_f
    

    Parameters
    ----------
    lst_f : list[int]

    Returns
    -------
    lst_h : list[int]
        DESCRIPTION.

    """
    lst_h=[]
    maxi=val_max(lst_f)
    for i in range(0,maxi+1):
        occ=nb_occurence(lst_f, i)
        lst_h.append(occ)
    return lst_h

#print(histo([7,4,6,5,7]))

def est_injective(lst_f:list) -> bool:
    """
    renvoie la valeur True si la fonction représentée par la liste lst_f est une injection.
Dans le cas contraire, elle renvoie False

    Parameters
    ----------
    lst_f : list

    Returns
    -------
    res : bool
        DESCRIPTION.

    """
    lst_h=histo(lst_f)
    cond=True
    i=0
    while i<len(lst_h) and cond:
        if lst_h[i]>1:
            res=False
            cond=False
        else:
            res=True  
        i+=1
    return res
    
    
#print(est_injective([7,4,6,5,7])) 

def est_surjective(lst_f:list) -> bool:
    """
    renvoie la valeur True si la fonction représentée par la liste lst_f est une
surjection. Dans le cas contraire, elle renvoie False

    Parameters
    ----------
    lst_f : list

    Returns
    -------
    res : bool

    """   
    lst_h=histo(lst_f)    
    cond=True
    i=0
    while i<len(lst_h) and cond:
        if lst_h[i]<1:
            res=False
            cond=False
        else:
            res=True  
        i+=1
    return res   

#print(est_surjective([4,0,2,1,3]))   

def est_bijective(lst_f:list) -> bool:
    """
    renvoie la valeur True si la fonction représentée par la liste lst_f est une bijection.
Dans le cas contraire, elle renvoie False

    Parameters
    ----------
    lst_f : list

    Returns
    -------
    res : bool
        DESCRIPTION.

    """       
    if est_injective(lst_f) and est_surjective(lst_f):
        res=True
    else:
        res=False
    return res

#print(est_bijective([4,0,2,1,3])) 

#Question 2

def affiche_histo(lst_f:list):
    """
    

    Parameters
    ----------
    lst_f : list

    Returns
    -------
    None.

    """
    lst_h=histo(lst_f)
    print("TEST HISTOGRAMME")
    print("\nF = {}".format(lst_f))
    print("\nHISTOGRAMME")
    for i in range(0, len(lst_h)):
        for j in range(0,lst_h[i]):
            print("\n#")
        print("|--| \n {}".format(i), end='')
        
    
#affiche_histo([1, 5, 5, 5, 9, 11, 11, 15, 15, 15])
    
import matplotlib.pyplot as plt           

def affiche_histo_plt(lst_f:list) -> bool:
    
    print(plt.hist(lst_f))
    
#affiche_histo_plt([1, 5, 5, 5, 9, 11, 11, 15, 15, 15])
    
    
#Exercice 5

import random

def test_present(present:callable) -> bool:
    """
    admet en paramètres une liste d'entiers lst et un nombre entier e 
et retourne un booléen True si l'élément e est présent dans la liste lst et False sinon

    Parameters
    ----------
    present : callable

    Returns
    -------
   res : bool

    """
    #Test liste vide
    res1=False
    lst=[]
    e=random.random()
    test=present(lst, e)
    if test:
        print("ECHEC : test liste vide")
    else:
        print("SUCCES : test liste vide")
        res1=True
    
    #Tests sur plusieurs cas
    
    lst_test=[1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
    res2=False
    e=lst_test[0]
    test=present(lst, e)
    if test:
        print("ECHEC : test debut")
    else:
        print("SUCCES : test debut")
        res2=True
        
    res3=False    
    e=lst_test[9]
    test=present(lst, e)
    if test:
        print("ECHEC : test fin")
    else:
        print("SUCCES : test fin")
        res3=True
    
    res4=False    
    e=lst_test[4]
    test=present(lst, e)
    if test:
        print("ECHEC : test milieu")
    else:
        print("SUCCES : test milieu")
        res4=True
     
    res5=False    
    e=10
    test=present(lst, e)
    if test:
        print("ECHEC : test absence")
    else:
        print("SUCCES : test absence")
        res5=True
        
    if res1 and res2 and res3 and res4 and res5:
        res=True
    return res
        
#VERSION 1

#La boucle s'arrete si le premier élément est égale à e 
def present1(lst, e) :
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
            return(True)
 #      else :             
#            return (False)
    return (False) 

#VERSION 2

#b doit être initialisé à False et le else peut-être supprimé
def present2(lst, e) :
#    b=True
    b=False 
    for i in range (0, len(lst), 1) : 
        if (lst[i] == e) :
            b=True
#        else :       
#           b=False
    return (b)

#VERSION 3

#La variable b est inutilisé, et la boucle ne prend pas en compte la dernière valeur
def present3(lst, e) :
#   b=True 
#  for i in range (0, len(lst), 1) :
#      return (lst[i] == e) 
   return (e in lst)

#VERSION 4

#Le  while ne s'execute jamais car b est initialisé à False, i ne s'incremente pas
def present4(lst, e) :
    b=False
    i=0
#    while (i<len(lst) and b) : 
    while (i<len(lst) and not b) :
        if (lst[i] == e) :
            b=True
        i += 1 
    return (b)

#print("TESTS PRESENT")
#print("TEST 1")
#test_present(present1)
#print("TEST 2")
#test_present(present2)
#print("TEST 3")
#test_present(present3)
#print("TEST 4")
#test_present(present4)

def test_pos(pos:callable) -> bool:
    """
    admet en paramètres une liste d'entiers lst et un nombre entier e 
et retourne un booléen True si l'élément e est présent dans la liste lst et False sinon

    Parameters
    ----------
    pos : callable

    Returns
    -------
   res : bool

    """
    #Test liste vide
    res1=False
    lst=[]
    e=random.random()
    test=pos(lst, e)
    if test:
        print("ECHEC : test liste vide")
    else:
        print("SUCCES : test liste vide")
        res1=True
    
    #Tests sur plusieurs cas
    
    lst_test=[1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
    res2=False
    e=lst_test[0]
    test=pos(lst, e)
    if test:
        print("ECHEC : test debut")
    else:
        print("SUCCES : test debut")
        res2=True
        
    res3=False    
    e=lst_test[9]
    test=pos(lst, e)
    if test:
        print("ECHEC : test fin")
    else:
        print("SUCCES : test fin")
        res3=True
    
    res4=False    
    e=lst_test[4]
    test=pos(lst, e)
    if test:
        print("ECHEC : test milieu")
    else:
        print("SUCCES : test milieu")
        res4=True
     
    res5=False    
    e=10
    test=pos(lst, e)
    if test:
        print("ECHEC : test absence")
    else:
        print("SUCCES : test absence")
        res5=True
        
    if res1 and res2 and res3 and res4 and res5:
        res=True
    return res
           
        
#VERSION 1

#Il faut initialisé la liste lst_res avec une liste vide
def pos1(lst, e) :
#   lst_res = list(lst)
    lst_res = [] 
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
            lst_res += [i]
    return lst_res

# VERSION 2


def pos2(lst, e) :
    lst_res = list(lst)
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
            lst_res[i] = i
        else:
            lst_res[i] = -1 
    while -1 in lst_res:
        lst_res.remove(-1)
    return lst_res

# VERSION 3
def pos3(lst, e) :
    nb= lst.count(e)
    lst_res = [0]*nb
    occ = 0 
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
#          lst_res.append(i) 
            lst_res[occ] = i
            occ += 1
    return lst_res

# VERSION 4
def pos4(lst, e) :
    nb= lst.count(e)
    lst_res = [0]*nb
    j=0
    for i in range (0, len(lst), 1) :
        if (lst[i] == e) :
            lst_res[j]= i
            j += 1 
    return lst_res

print("TESTS POS")
print("TEST 1")
test_pos(pos1)
print("TEST 2")
test_pos(pos2)
print("TEST 3")
test_pos(pos3)
print("TEST 4")
test_pos(pos4)


































