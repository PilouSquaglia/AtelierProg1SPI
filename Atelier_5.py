# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:34:34 2021

@author: Pilou
"""

import random as rd
import time 
import matplotlib.pyplot as plt
import numpy as np

def gen_list_random(int_nbr:int=10,int_binf:int=0, int_bsup:int=9) -> list:
    """
    retourne une liste de nombres aléatoires
int_nbr compris entre int_binf et int_bsup. Si aucun paramètre n'est passé à la fonction alors
gen_list_random_int génèrera par défaut 10 nombres compris entre 0 (inclus) et 10 (exclus).

    Parameters
    ----------
    int_binf : int |borne inférieure de la liste retournée
    int_bsup : int |borne supérieure de la liste retournée

    Returns
    -------
    lst_res : list liste retournée avec 10 nombres aléatoires
                compris entre int_binf et int_bsup

    """
    lst_res=[]*int_nbr
    for i in range(int_nbr):
        lst_res.append(rd.randint(int_binf, int_bsup))
    return lst_res

#print(gen_list_random())

#Exercice 2

def mix_list(list_to_mix:list) -> list:
    """
    prend en paramètre une liste list_to_mix de n'importe quoi
potentiellement triée et qui retourne la liste mélangée

    Parameters
    ----------
    list_to_mix : list |liste potentiellement triée

    Returns
    -------
    lst_res : list |liste passée en paramètre mélangée

    """
    longueur=len(list_to_mix)
    lst_res=[0]*longueur    #initialisation de lst_res
    lst_new_indice=[] #liste des cases de lst_res qui ont deja ete remplies
    for indice in range(longueur):#parcours les indices de la liste d'entree
        new_indice=rd.randint(0, longueur-1)#recherche aleatoire d'un indice pour insertion dans la liste retournee
        while new_indice in lst_new_indice:#on verifie que new_indice n'a pas deja ete utilise
            new_indice=rd.randint(0, longueur-1)#sinon on en genere un autre
        lst_res[new_indice]=list_to_mix[indice]#l'element est place dans une case de lst_res choisie au hasard
        lst_new_indice.append(new_indice)#on ajoute new_indice a la liste pour ne pas le réutiliser
    return lst_res




#lst_test=gen_list_random()
#print(lst_test)
#print(mix_list(lst_test))


#Exercice 3

       
def choose_element_list(list_in_which_to_choose:list) -> any:
    """
    prend en paramètre une liste
    list_in_which_to_choose de n'importe quoi et qui retourne un élément de cette liste choisi au hasard

    Parameters
    ----------
    list_in_which_to_choose : list
    Returns
    -------
    res : any

    """       
    longueur=len(list_in_which_to_choose)
    ind_elt_random=rd.randint(0,longueur-1) #On choisi un indice aléatoire compris entre 0 et l'indice max de la liste
    res=list_in_which_to_choose[ind_elt_random]    
    return res

#print(choose_element_list([6, 6, 3, 2, 8, 5, 4, 5, 4, 5]))
#print(choose_element_list(["test","test2","test3","test4","test5"]))

def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int) -> list:
    """
    prend en paramètre une liste
    list_in_which_to_choose de n'importe quoi, un int_nbr_of_element_to_extract et qui retourne
    une liste composée de int_nbr_of_element_to_extract éléments de la liste de départ choisis au
    hasard

    Parameters
    ----------
    list_in_which_to_choose : list
    int_nbr_of_element_to_extract : int

    Returns
    -------
    lst_res : list

    """
    longueur=len(list_in_which_to_choose)
    lst_res=[]
    lst_indice=[]
    for indice in range(0, int_nbr_of_element_to_extract): #Boucle servant à répéter l'opération int_nbr_of_element_to_extract fois
         ind_elt_random=rd.randint(0,longueur-1) #On choisi un indice aléatoire compris entre 0 et l'indice max de la liste 
         while ind_elt_random in lst_indice: #Verification que l'indice n'est pas deja utilisé en verfiant qu'il n'est pas dans a liste qui contient les indices utilisé
             ind_elt_random=rd.randint(0,longueur-1)
         lst_indice.append(ind_elt_random) #On l'ajoute dans une liste pour ne pas le reutilisé
         elt=list_in_which_to_choose[ind_elt_random] #On prend un element de la liste avec l'indice choisi aléatoirement
         lst_res.append(elt)
    return lst_res

#print(extract_elements_list(["test","test2","test3","test4","test5"], 2))
         
#Exercice 5

def perf_mix(f1:callable, f2:callable, list_int:list, iteration:int) -> tuple:
    """
    permet de calculer le temps d’exécution moyen des deux fonctions
de mélange (mix_list et random.shuffle) passées en paramètre dans une même configuration

    Parameters
    ----------
    f1 : callable , 1ère fonction à tester
    f2 : callable , 2ème fonction à tester
    list_int : list , liste d’entiers représentant les tailles de liste pour lesquelles on effectue la comparaison. 
    iteration : int , nombre d'opération à effectuer

    Returns
    -------
    res : tuple 

    """
    res=()
    lst_perf_f1=[]
    lst_perf_f2=[]
    
    for taille in list_int:
        print("Test en cours", taille)
        moy_f1=0
        moy_f2=0
        lst_test=gen_list_random(taille)
        for iteration in range(iteration):
            #test pour f1
            start_pc = time.perf_counter()
            f1(lst_test)
            end_pc = time.perf_counter()
            temps = end_pc-start_pc
            moy_f1+=temps
            #test pour f2
            start_pc = time.perf_counter()
            f2(lst_test)
            end_pc = time.perf_counter()
            temps = end_pc-start_pc
            moy_f2+=temps 
        moy_f1/=iteration
        lst_perf_f1.append(moy_f1)
        moy_f2/=iteration
        lst_perf_f2.append(moy_f2)
    res+=(lst_perf_f1,lst_perf_f2)
    #matplotlib
    fig, ax = plt.subplots()
    ax.plot(list_int,lst_perf_f1, 'r*-', label='mix_list')
    ax.plot(list_int,lst_perf_f2,'g*-', label='shuffle')
    ax.set(xlabel='taille de liste', ylabel='temps execution',
     title='Fonctions identité, mix_list et shuffle')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()
    return res


     
#print(perf_mix(mix_list, rd.shuffle, [10, 500, 5000, 10000], 10))

        
def perf_extract(f1:callable, f2:callable, list_int:list, iteration:int) -> tuple:
    """
    permet de calculer le temps d’exécution moyen des deux fonctions permettant d'extraire
    aléatoirement int_nbr_of_element_to_extract éléments

    Parameters
    ----------
    f1 : callable , 1ère fonction à tester
    f2 : callable , 2ème fonction à tester
    list_int : list , liste d’entiers représentant les tailles de liste pour lesquelles on effectue la comparaison. 
    iteration : int , nombre d'opération à effectuer

    Returns
    -------
    res : tuple 
    
    """
    res=()
    lst_perf_f1=[]
    lst_perf_f2=[]
    
    for taille in list_int:
        print("Test en cours", taille)
        moy_f1=0
        moy_f2=0
        lst_test=gen_list_random(taille)
        for iteration in range(iteration):
            #test pour f1
            start_pc = time.perf_counter()
            f1(lst_test, 5)
            end_pc = time.perf_counter()
            temps = end_pc-start_pc
            moy_f1+=temps
            #test pour f2
            start_pc = time.perf_counter()
            f2(lst_test, 5)
            end_pc = time.perf_counter()
            temps = end_pc-start_pc
            moy_f2+=temps 
        moy_f1/=iteration
        lst_perf_f1.append(moy_f1)
        moy_f2/=iteration
        lst_perf_f2.append(moy_f2)
    res+=(lst_perf_f1,lst_perf_f2)
    #matplotlib
    fig, ax = plt.subplots()
    ax.plot(list_int,lst_perf_f1, 'r*-', label='mix_extract')
    ax.plot(list_int,lst_perf_f2,'g*-', label='sample')
    ax.set(xlabel='taille de liste', ylabel='temps execution',
     title='Fonctions identité, mix_list et shuffle')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()
    return res


     
#print(perf_extract(extract_elements_list, rd.sample, [10, 500, 5000, 10000], 10))  

#Exercice 6

def sort_list(lst:list) -> list:
    """
    prend en paramètre une liste d'élément et retourne, sans
    modifier la liste de départ, une nouvelle liste constituée des éléments de la liste de départ triés par ordre
    croissant.

    Parameters
    ----------
    lst : list , liste à trier
    Returns
    -------
    res : list , liste triée

    """
    longueur=len(lst)
    if longueur==0:
        res=[]
    else:
        pivot=lst[0]
        plus_petits=[]
        for e in lst:
            if e<pivot:
                plus_petits.append(e)
        plus_grands=[]
        for e in lst[1:]:
            if e>=pivot:
                plus_grands.append(e)
        res=sort_list(plus_petits)+[pivot]+sort_list(plus_grands)
    return res


#lst_test=[4, 3, 5, 0]
#print(sort_list(lst_test))         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    