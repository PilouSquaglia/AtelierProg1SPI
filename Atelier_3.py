# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:39:31 2021

@author: Pilou
"""

def somme1(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste"""
    somme=0
    
    for i in L:
        somme+=i
        
    return somme

def somme2(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste"""
    somme=0
    
    for i in range(len(L)):
        somme+=L[i]
        
    return somme

def somme3(L:list) -> int:
    
    """Admet en paramètre une liste
d'entiers L et retourne la somme des valeurs de la liste"""
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
    
    
    
test_exercice1()