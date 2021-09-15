# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:21:53 2021

@author: Pilou
"""


import re 

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


def is_mail(mail:str) -> str:
    """
    prend en paramètre une chaine de
caractère de type adresse mail ‘bisgambiglia@univ-corse.fr’ et qui renvoie un tuple composé
des codes suivants : (validité, code erreur)

    Parameters
    ----------
    str_arg : str

    Returns
    -------
    res : str

    """
    string_elements = mail.split("@")


    if not("@" in mail):
        return "[0, 2] le mail n’est pas valide, il manque l’@"
        
    #est-ce que le corps est valide? (composé uniquement d'alphanum,
    # tirets et tirets bas, avec au moins 1 caractères et ne se finit pas par un point)
    if re.match("^[_a-z0-9A-Z-]{2,}(\.[_a-zA-Z0-9-]+)*$", string_elements[0]) is None:
            return "[0, 1] le mail n’est pas valide, le corp n’est pas valide"
        

    #"y a-t-il un point?"
    second_part = string_elements[1].split(".")
    if "." not in string_elements[1] or len(string_elements) != 2:
        return "[0, 4] le mail n’est pas valide, il manque le ."

    #le nom de domaine est-il "univ-corse" ?
    if second_part[0] != "univ-corse":
       
            return "[0, 3] le mail n’est pas valide, le domaine n’est pas valide"

    return "[1, 38] le mail est valide"



#Exercice 2

def mots_Nlettres(list_words: list, n: int):
    corrects = []
    for s in list_words:
        if len(s) == n:
            corrects.append(s)
    return corrects


def commence_par(mot: str, prefixe: str):
    prefix_len = len(prefixe)
    return mot[:prefix_len] == prefixe


def finit_par(mot: str, suffixe: str):
    suffixe_len = len(suffixe)
    return mot[-suffixe_len:] == suffixe


