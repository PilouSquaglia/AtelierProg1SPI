# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 13:45:25 2021

@author: Pilou
"""

from math import sqrt
import datetime as date

def message_IMC(IMC:float) -> str:
    
    """Renvoie une chaine de caractère correspondant à l'interprétation de l'IMC"""
    
    tab_IMC = ['dénutrition ou famine','maigreur','corpulence normale', 'surpoids', 'obésité modérée', 'obésité sévère', 'obésité morbide']
    
    IMC_1=16.5
    IMC_2=18.5
    IMC_3=25
    IMC_4=30
    IMC_5=35
    IMC_6=40
    
    res = tab_IMC[0]
    
    if IMC>IMC_6:
        res = tab_IMC[6]
    elif IMC>=IMC_5 and IMC<=IMC_6:
        res = tab_IMC[5]
    elif IMC>=IMC_4 and IMC<IMC_5:
        res = tab_IMC[4]
    elif IMC>=IMC_3 and IMC<IMC_4:
        res = tab_IMC[3]
    elif IMC>=IMC_2 and IMC<IMC_3:
        res = tab_IMC[2]
    elif IMC>=IMC_1 and IMC<IMC_2:
        res = tab_IMC[1]
    return res

#print(message_IMC(41))

def test_imc():
    
    """Test de la fonction message_imc"""
    
    print(message_IMC(10))
    print(message_IMC(17))
    print(message_IMC(19))
    print(message_IMC(26))
    print(message_IMC(34))
    print(message_IMC(35))
    print(message_IMC(42))
    
#test_imc()   

#Exercice 2

def bissextile(annee:int) -> bool:
    
    """Detemrmine si l'année passée en paramètre des bissextile ou non et renvoie un booléen (True si oui, False si non)"""
    
    div_4=annee%4
    div_100=annee%100
    div_400=annee%400
    
    
    if (div_4==0 and div_100!=0) or div_400==0 :
        res=True
    else:
        res=False
        
    return res

def test_bissextile():
    
    """Test de la fonction bissextile"""
    
    print(bissextile(2014))
    print(bissextile(2016))
    print(bissextile(2020))
    print(bissextile(2000))
    
#test_bissextile()


#Exercice 3

def discriminant(a:float, b:float, c:float) -> float:
    
    """Renvoie le discriminant à partir de 3 paramètres"""
    
    delta=b^2-4*a*c
    return delta

def racine_unique(a:float, b:float) -> float:
    
    """Renvoie la racine unique à partir de 2 paramètres"""
    
    x=(-b)/(2*a)
    return x

def racine_double(a:float, b:float, delta:float, num:int) -> float:
    
    """Renvoie la racine double à partir de 4 paramètres"""
    
    if num==1:
        x=((-b)+sqrt(delta))/2*a
        
    elif num==2:
        x=((-b)-sqrt(delta))/2*a
    
    return x


def str_equation(a:float, b:float, c:float) -> str:
    
    """Renvoie une chaine de caractères avec l'equation associée à partir des paramètres """
    
    if a==0:
        str1=''
    elif a==1:
        str1='x²'
    elif a<0:
        str1='-'+str(abs(a))+'x²'
    else:
        str1=str(a)+'x²'
    if b<0:
        str2='-'+str(abs(b))+'x'
    elif b==0:
        str2=''
    elif b==1:
        str2='+x'
    else:
        str2='+'+str(b)+'x'
    if c<0:
        str3='-'+str(abs(c))
    elif c==0:
        str3=''
    else:
        str3='+'+str(c)
    return str1+str2+str3

#print(str_equation(1, -1, 0))

def solution_equation(a:float, b:float, c:float) -> str:
    
    """Renvoie une chaine de caractères représentant un message qui indique si l'équation est résolvable"""
    
    message="Solution de l'équation "+str_equation(a, b, c)  
    delta=discriminant(a, b, c)
    
    if delta>0:
        x1=racine_double(a, b, delta, 1)
        x2=racine_double(a, b, delta, 2)
        res=message+"\nDeux racines : \n x1 = {} \n x2 = {}".format(x1, x2)
    elif delta==0:
        x=racine_unique(a, b)
        res=message+"\nRacine unique : x = {}".format(x)
    else:
        res=message+"\nPas de racine réelle" 
    return res    
    
#print(solution_equation(1, 2, 0))

def equation(a:float, b:float, c:float):
    
    """Affiche la fonction solution_equation"""
    
    print(solution_equation(a, b, c))
    
#equation(1, 2, 0)

def test_equation():
    
    equation(0, 1, 2)
    equation(1, 0, 4)
    equation(2, 4, 0)
    equation(-1, 1, -2)
    
#test_equation()

#Exercice 4

def date_est_valide(jour:int, mois:int, annee:int) -> bool:
    
    
    """Renvoie un booléen indiquant si la date est valide."""
    
    res=True
    
    if jour<1 or jour>31:
        
        res=False
        
    elif mois<1 or mois>12:
        
        res=False
    elif annee<1:
        
        res=False
        
    elif mois==2 and jour>28 and bissextile(annee)==False:
        
        res=False
        
    elif mois==2 and jour>29 and bissextile(annee):
        
        res=False
        
    elif mois==8 and jour==31:
        res=True
    
    for i in range(1,6):
        if mois==i+1 and jour>30:
            res=False
            
    for i in range(8,10):
        if mois==i+1 and jour>30:
            res=False
    
            
    return res

#print(date_est_valide(31, 9, 2021))

def saisie_date_naissance() -> date:
    
    """Assure la saisie au clavier
d'une date de naissance par la saisie de trois entiers annee, mois et jour et renvoie
une valeur de type date"""
    
    jour=int(input("Saisissez le jour"))
    mois=int(input("Saisissez le mois"))
    annee=int(input("Saisissez l'année"))
    
    if date_est_valide(jour, mois, annee):
        res=date.date(annee, mois, jour)
    else:
        res="Erreur dans la saisie de la date"
    
    return res

#print(saisie_date_naissance())


def age(date_naissance:date) -> int:
    
    """Renvoie un entier correspondant à l’âge de la personne à la date du jour."""
    
    jour_n=date_naissance.day
    mois_n=date_naissance.month
    annee_n=date_naissance.year
    
    jour_a=date.date.today().day
    mois_a=date.date.today().month
    annee_a=date.date.today().year
    
    if mois_n-mois_a<0:
        res=annee_a-annee_n
    elif jour_n<jour_a and mois_n==mois_a:
        res=annee_a-annee_n-1
    else:
        res=annee_a-annee_n-1
        
    return res
    
#print(age(date.date(2001, 11, 14))) 

def estmajeur(date_naissance) -> bool:
    
    res=True
    if age(date_naissance)<18:
        res=False
    return res
    
#print(estmajeur(date.date(2001, 11, 14)))


def test_acces() -> str:
    
    """saisie d'une date de naissance
et renvoie un message"""
    
    date_naissance=saisie_date_naissance()
    age1=age(date_naissance)

    if estmajeur(date_naissance):
        res='Bonjour, vous avez {} ans, Accès autorisé'.format(age1)
    else:
        res='Désolé, vous avez {} ans, Accès interdit'.format(age1)
    return res

#print(test_acces())
    
    
    
    


    
    
    
    
    

    
    
    






        
        
        
    
    