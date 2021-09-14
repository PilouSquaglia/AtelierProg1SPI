# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:38:04 2021

@author: Pilou
"""

from Atelier_4 import full_name
def test_full_name():
    
    nom='squaglia pierre-louis'
    attendu='SQUAGLIA Pierre-louis'
    res="#####ECHEC#####"
    test=attendu==full_name(nom)
    
    print("Test avec {}, \nAttendu : {} \nResultat : {}".format(nom, attendu, full_name(nom)))
    print(test)
    
    if test:
        res="#####SUCCES#####"
    return res
        
print(test_full_name())