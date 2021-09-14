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
    ch_res=""
    for e in str_arg:
        print(e)
        while e!=' ':
            ch_res+=e.upper()
            print(ch_res)
    return ch_res

print(full_name("bisgambiglia paul"))            