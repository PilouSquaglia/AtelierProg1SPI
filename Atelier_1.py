# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:23:53 2021

@author: Pilou
"""
#Exercice 1
def salaire():
    
    "Calcule le salaire mensuel d’un employé payé à l’heure à partir de son salaire horaire et du nombre d’heures de travail"
    
    nh=210 #variable pour le nombre d'heure int
    sh=10 #variable pour le salaire horaire int
    heure_sup_25=0 #variable pour les heures supp majoré à 25% initialisé à 0 int
    heure_sup_25=0 #variable pour les heures supp majoré à 50% initialisé à 0 int
    
    if nh>160:
        heure_sup_25=nh-160
        salaire=(sh*nh)+(sh*heure_sup_25*1.25)
        
        if nh>200:
            heure_sup_50=nh-200
            salaire=(sh*nh)+(sh*heure_sup_50*1.5)
    else:
        salaire = sh*nh
        
    return salaire

#print(salaire())

#Exercice 2

def lire_caractere():
    
    "Determine si un caractère est en majuscule, minuscule, un chiffre, ou un caractère spécial"
    
    caractere=' ' #char
    code_ascii = ord(caractere) #On récupere le code ASCII du caractère int
    
    if code_ascii>=48 and code_ascii<=57:
         return "Le caractère est un chiffre"
    if code_ascii>=65 and code_ascii<=90:
         return "Le caractère est en majuscule"
    if code_ascii>=97 and code_ascii<=122:
         return "Le caractère est en minuscule"
    else :
        return "Le caractère est un caractère spécial"
    
#print(lire_caractere())

#Exercice 3

def impots():
    
    "Determine si un habitant est imposable ou pas"
    
    sexe=input("Saisissez le sexe de l'habitant (f ou m) ") #char
    age=int(input("Saisissez l'âge de l'habitant")) #int
    imposable=False #bool
    
    if sexe=='m' and age>20:
        imposable=True
    elif sexe=='f' and age>=18 and age<=35:
        imposable=True
        
    if imposable:
        res="L'habitant est imposable"
    else: res="l'habitant n'est pas imposable"
    
    return res
    
#print(impots())

#Exercice 4

def reprographie():
    
    "Affiche la facture correspondante avec le nombre de photocopies effectuées"
    
    nb_photocopie=int(input("Nombre de photocopie : ")) #int
    PRIX_BASE=0.1 #float
    PRIX_10=0.09 #float
    PRIX_30=0.08 #float
    
    if nb_photocopie>10 and nb_photocopie<=30:
        res=(10*PRIX_BASE)+(nb_photocopie-10)*PRIX_10
    if nb_photocopie>30:
        res=(10*PRIX_BASE)+20*PRIX_10+(nb_photocopie-30)*PRIX_30
    else:
        res=nb_photocopie*PRIX_BASE
        
    return 'Total à payer : ',res,'€'
    
#print(reprographie())

#Exercice 5

def portuaire():
    
    "Calcul les frais portuaire d'un bateau"
    
    nom=input("Saisissez le nom du bateau : ") #str
    longueur=float(input("Saisissez la longueur du bateau : ")) #float
    categorie=int(input("Saisissez la catégorie du bateau (1, 2 ou 3) : ")) #int
    
    if longueur<5:
        res=100
    elif longueur>=5 and longueur<=10:
        res=200
    elif longueur>10 and longueur<=12:
        res=400
    elif longueur>12:
        res=600
        
    cout_mensuel=res #cout mensuel #int
    #       Taxe spécial annuelle     #
    tab_taxe=[100, 150, 200] #tab indice 0 = 100
    taxe=tab_taxe[categorie-1] #On retire 1 car l'indice des tableaux commence à 0 et qu'il n'existe pas de catégorie 0.
    #       Cout annuel               #
    cout_annuel=taxe+cout_mensuel*12
    print('Le coût annuel d’une place au port pour le voilier',nom,'est de',cout_annuel,'euros.')
    
#portuaire() 


#Exercice 6      

def concessionnaire():
    
    "Calcule les frais mensuels d'utilisation des voitures"
    
    CARBURANT='D' #str type du carburant de la voiture
    CYLINDREE=2000 #int cylindrée de la voiture 
    KM=10000 #Nombre de kilometres de la voiture
    P_CARB=1 #float prix du carburant 
    conso=8 #int consommation en L/100km
    res=0 #float
    SURCOUT_E=1.5
    SURCOUT_D=1.7
    if CARBURANT=='E':
        if  CYLINDREE>2000:
            conso=10
        res=(KM/100)*conso*P_CARB*1.5
    else: 
        res=(KM/100)*conso*P_CARB*1.7
    return res

#print(concessionnaire())

#Exercice 7

def elections():
    
    "Determine si le candidat N°1 est élu, battu, s'il se trouve en ballottage favorable ou défavorable "
    
    candidats=[]
    maxi=0 #score maximal parmis les candidats
    for i in range(0, 4):
        c=-1
        while c<0:
            c=float(input("Entrez le % du candidat N° {} ".format(i+1)))
        candidats.append(c)
        
    candidat=candidats[0] #On récupère le candidat N°1
    
    for j in range(0,4):
        if candidats[j]>maxi:
            maxi=candidats[j]
            
    if maxi>=50:    
        if candidat>50:
            print('Le candidat N°1 est élu avec',candidat,'% des voix')
        if candidat<12.5:
            print('Le candidat N°1 est battu avec',candidat,'% des voix')
    else:
        if candidat==maxi:
            print('Le candidat N°1 est en ballotage favorable avec',candidat,'% des voix')
        else:
            print('Le candidat N°1 est en ballotage défavorable avec',candidat,'% des voix')
    
#elections()


#Exercice 8

def assurance():
    
    "Determine le type de tarif du conducteur "
    #Saisit des données
    
    age=int(input("Saisissez l'age : "))
    permis=int(input("Saisissez l'ancienneté du permis : "))
    nb_accident=int(input("Saisissez le nombre d'accidents' : "))
    assurance=int(input("Saisissez l'ancienneté de l'assurance dans la compagnie : "))
    
    tab_tarif=['refus','rouge','orange','vert','bleu']
    score=3 #Correspond a l'indice du tableau des tarifs, l'initialise au tarif vert
    
    if assurance>1:
        score+=1
    if age<25:
        score-=1
    if permis<2:
        score-=1
    if score-nb_accident>=0:
        score-=nb_accident
    else:
        score=0
    return tab_tarif[score]

#print(assurance())
    
    
    
    
    
    
    
    
    
    
    