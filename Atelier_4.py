# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:21:53 2021

@author: Pilou
"""

def full_name(str_arg:str) -> str:
    """
    prend en paramètre une chaine de caractère
de type ‘nom prenom’ et qui renvoie la même chaîne avec le nom en majuscule et le prénom
avec la première lettre seulement en majuscule.

    Parameters
    ----------
    str_arg : str
        DESCRIPTION.

    Returns
    -------
    ch_res : str
        DESCRIPTION.

    """
    maj = str_arg.split(" ")
    return maj[0].upper() + " " + maj[1].capitalize()



print(full_name("bisgambiglia paul"))            


def is_mail(str_arg:str) -> (int,int):
    """
    prend en paramètre une chaine de
caractère de type adresse mail ‘bisgambiglia@univ-corse.fr’ et qui renvoie un tuple composé
des codes suivants : (validité, code erreur)

    Parameters
    ----------
    str_arg : str

    Returns
    -------
    res : (int,int)

    """
    