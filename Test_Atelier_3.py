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
    test1=attendu==res
    print("Test avec lst={}".format(lst))
    print("Liste vide, Attendu {} : \nRésultat :{}".format(attendu,res))
    print(test1)
    print("#############")
    lst=[4, 8, -2,-3,-1, 0, -7, 0, 6, 5 ]
    attendu=[-2, -3, -1, -7, 0, 0, 4, 8, 6, 5]
    res=separer(lst)
    test2=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {}  \nRésultat : {}".format(attendu, res))
    print(test2)
    print("#############")
    lst=[4, 5, 6, 0]
    attendu=[0, 4, 5, 6]
    res=separer(lst)
    test3=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu,res))
    print(test3)
    print("#############")
    lst=[-4, -5, -6, 0]
    attendu=[-4, -5, -6, 0]
    res=separer(lst)
    test4=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu, res))
    print(test4)
    print("#############")
    lst=[0, 1, 2, 3]
    attendu=[0, 1, 2, 3]
    res=separer(lst)
    test5=attendu==res
    print("Test avec lst={}".format(lst))
    print("Attendu {} \nRésultat : {}".format(attendu,res))
    print(test5)
    if test1 and test2 and test3 and test4 and test5:
        print("######SUCCES######")
    
test_separer()