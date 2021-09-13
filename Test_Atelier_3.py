# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:47:55 2021

@author: Pilou
"""

from Atelier_3 import separer

def test_separer():
    
    """Teste la fonction separer()"""
    lst=[]
    attendu=[]
    res=separer(lst)
    test=attendu==res
    print("Test avec lst=[]".format(lst))
    print("Liste vide, Attendu {} : \nRésultat :{}".format(attendu,res))
    print(test)
    lst=[4, 8, -2,-3,-1, 0, -7, 0, 6, 5 ]
    attendu=[-2, -3, -1, -7, 0, 0, 4, 8, 6, 5]
    res=separer(lst)
    test=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {}  \nRésultat : {}".format(attendu, res))
    print(test)
    lst=[4, 5, 6, 0]
    attendu=[0, 4, 5, 6]
    res=separer(lst)
    test=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu,res))
    print(test)
    lst=[-4, -5, -6, 0]
    attendu=[-4, -5, -6, 0]
    res=separer(lst)
    test=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu, res))
    print(test)
    lst=[0, 1, 2, 3]
    attendu=[0, 1, 2, 3]
    res=separer(lst)
    test=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu,res))
    print(test)
    
test_separer()