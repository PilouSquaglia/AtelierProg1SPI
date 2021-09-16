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



#print(full_name("bisgambiglia paul"))            


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
            return "[0, 1] le mail n’est pas valide, le corps n’est pas valide"
        

    #"y a-t-il un point?"
    second_part = string_elements[1].split(".")
    if "." not in string_elements[1] or len(string_elements) != 2:
        return "[0, 4] le mail n’est pas valide, il manque le ."

    #le nom de domaine est-il "univ-corse" ?
    if re.match("^[_a-z0-9A-Z-]{2,}(\.[_a-zA-Z0-9-]+)*$", second_part[0]) is None:
       
            return "[0, 3] le mail n’est pas valide, le domaine n’est pas valide"

    return "[1, 0] le mail est valide"



#Exercice 2

def mots_Nlettres(lst_mot: list, n: int) -> list:
    """
    prend une liste de mots (lst_mot) en
argument et qui renvoie la liste des mots contenant exactement n lettres.

    Parameters
    ----------
    lst_mot : list
    n : int
        DESCRIPTION.

    Returns
    -------
    res : list

    """
    res = []
    for s in lst_mot:
        if len(s) == n:
            res.append(s)
    return res

#print(mots_Nlettres(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"], 5))

def commence_par(mot: str, prefixe: str) -> bool:
    """
    renvoie True si l'argument mot
commence par prefixe et False sinon.

    Parameters
    ----------
    mot : str
    prefixe : str

    Returns
    -------
    bool

    """
    prefixe_len = len(prefixe)
    return mot[:prefixe_len] == prefixe

#(commence_par("auevoir", "aure"))

def finit_par(mot: str, suffixe: str) -> bool:
    """
    renvoie True si l'argument mot se termine
par suffixe et False sinon.

    Parameters
    ----------
    mot : str
    suffixe : str

    Returns
    -------
    bool

    """
    suffixe_len = len(suffixe)
    return mot[-suffixe_len:] == suffixe

#print(finit_par("aurevoir", "voi"))

def finissent_par(lst_mot:list, suffixe:str) -> list:
    """
    renvoie la liste des mots présents
dans la liste lst_mot qui se terminent par suffixe.

    Parameters
    ----------
    lst_mot : list

    suffixe : str

    Returns
    -------
    res : list

    """
    res=[]
    for i in lst_mot:
       suffixe_len = len(suffixe)
       if i[-suffixe_len:] == suffixe:
            res.append(i)
    return res
   
#print(finissent_par(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"], "jour"))


def commencent_par(lst_mot:list, prefixe:str) -> list:
    """
    renvoie la liste des mots présents
dans la liste lst_mot qui se terminent par suffixe.

    Parameters
    ----------
    lst_mot : list

    suffixe : str

    Returns
    -------
    res : list

    """
    res=[]
    for i in lst_mot:
       prefixe_len = len(prefixe)
       if i[:prefixe_len] == prefixe:
            res.append(i)
    return res

#print(commencent_par(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"], "a"))


def liste_mots (lst_mot:list, prefixe:str, suffixe:str, n:int) -> list:
    """
    renvoie la liste des mots
présents dans lst_mot qui commencent par prefixe, se terminent par suffixe et contiennent
exactement n lettres (sans boucle for, ni de if)

    Parameters
    ----------
    lst_mot : list
    prefixe : str
    suffixe : str
    n : int

    Returns
    -------
    res : list

    """
    res=finissent_par(commencent_par(mots_Nlettres(lst_mot,n),prefixe),suffixe)
    return res
        
#print(liste_mots(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer","aruoiryr"],"a","r",7))        
    

def dictionnaire(fichier:str) -> str:
    """
    admet en paramètre une chaine de
caractères représentant un nom de fichier de texte (ex :littre.txt ) et renvoie la liste des mots
présents dans ce fichier.

    Parameters
    ----------
    fichier : str

    Returns
    -------
    res : str

    """
    f=open(fichier+".txt","r")
    c=f.readline() #lecture d'une ligne dans une chaine
    # de caractères
    print("** Contenu du fichier **")
    while c!="" :
        print(c)
        c=f.readline()
    print("** fin **")
    

#dictionnaire("littre")

















