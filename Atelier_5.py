# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 08:34:34 2021

@author: Pilou
"""

import random as rd
import time 

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
    lst_res=[]
    len_lst=len(list_to_mix)
    for i in range(len_lst-1):
        
        
