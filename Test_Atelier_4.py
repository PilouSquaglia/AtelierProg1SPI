# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:38:04 2021

@author: Pilou
"""

from Atelier_4 import full_name
from Atelier_4 import is_mail
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

def test_is_mail():
    
    
    email_tests = [
    "bisgambiglia_paul@univ-corse.fr",
    "bisgambiglia_paulOuniv_corse.fr",
    "bisgambiglia_paul@univ_corsePOINTfr",
    "@univ_corse.fr",
    "bisgambiglia_paul@univ_paris.fr"
    ]
    for email in email_tests:
        print(is_mail(email))
        
test_is_mail()