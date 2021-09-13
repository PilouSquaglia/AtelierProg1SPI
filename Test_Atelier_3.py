# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:47:55 2021

@author: Pilou
"""

from Atelier_3 import separer

def test_separer():
    
    """Teste la fonction separer()"""
    lst=[]
    print("Liste vide  : {}".format(separer(lst)))
    lst=[4, 8, -2,-3,-1, 0, -7, 0, 6, 5 ]
    print("Attendu [-2, -3, -1, -7, 0, 0, 4, 8, 6, 5]  \nRésultat : {}".format(separer(lst)))
    lst=[4, 5, 6, 0]
    print("Attendu [0, 4, 5, 6] \nRésultat : {}".format(separer(lst)))
    lst=[-4, -5, -6, 0]
    print("Attendu [-4, -5, -6, 0] \nRésultat : {}".format(separer(lst)))
