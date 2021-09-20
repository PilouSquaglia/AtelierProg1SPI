# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:21:53 2021

@author: Pilou
"""


import re 
import random

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
    maj=str_arg.strip()
    maj = maj.split(" ")
    while '' in maj:
        maj.remove('')
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
    regex="^[_a-z0-9A-Z-]{2,}(\.[_a-zA-Z0-9-]+)*$"

    if not("@" in mail):
        return "[0, 2] le mail n’est pas valide, il manque l’@"
        
    #est-ce que le corps est valide? (composé uniquement d'alphanum,
    # tirets et tirets bas, avec au moins 1 caractères et ne se finit pas par un point)
    if re.match(regex, string_elements[0]) is None:
            return "[0, 1] le mail n’est pas valide, le corps n’est pas valide"
        

    #"y a-t-il un point?"
    second_part = string_elements[1].split(".")
    if "." not in string_elements[1] or len(string_elements) != 2:
        return "[0, 4] le mail n’est pas valide, il manque le ."

    #le nom de domaine est-il valide ? (composé uniquement d'alphanum,
    # tirets et tirets bas, avec au moins 1 caractères et ne se finit pas par un point)
    if re.match(regex, second_part[0]) is None:
       
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
    for mot in lst_mot:
        if len(mot) == n:
            res.append(mot)
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
    f=open(fichier+".txt","r",encoding=("utf8"))
    c=f.readline() #lecture d'une ligne dans une chaine
    # de caractères
    print("** Contenu du fichier **")
    while c!="" :
        print(c)
        c=f.readline()
    print("** fin **")
    

#dictionnaire("littre")

#Exercice 3

def places_lettre(ch:str,mot:str)->list:
    """
    cherche le caractere 'ch' dans la string 'mot' et renvoie une liste des indices 
    renvoie une liste vide si 'ch' absent
    Parameters
    ----------
    ch : str
        caractere a chercher
    mot : str
        mot dans lequel la recherche est effectuée
    Returns
    -------
    list
        liste des indices de ch dans mot, liste vide si ch absent
    """
    res=[]
    for i in range(len(mot)):
        if mot[i]==ch:
            res.append(i)
    return res

def outputStr(mot:str,lpos:list)->str:
    """
    renvoie une chaine de caractere contenant le mot avec 0 ou plusieurs caracteres remplacés
    par des "_"
    Parameters
    ----------
    mot : str
        mot a afficher
    lpos : list
        liste d'entiers representant les indices des caracteres du mot a afficher'
    Returns
    -------
    str
        le mot avec 0 ou plusieurs caracteres remplacés par des "_"
    """
    mot_out=""
    for i in range(len(mot)):
        if i in lpos:
            mot_out+=mot[i]+" "
        else:
            mot_out+="_ "
    return mot_out

def runGame():
    """
    programme principal, lance le jeu du pendu
    Returns
    -------
    None.
    """
    #liste de mots
    MOTS=build_list("mots.txt")
    #elements de la potence
    PENDU=["","|______","| / \\ ","|  T","|  O", "|----]"]
    #initialisations
    ind_pendu=0 #pour affichage de la potence    
    #rd_int=random.randint(0,len(MOTS)-1)#choisit un entier aleatoire
   #mot=MOTS[rd_int]#selection aleatoire du mot    
    lpos=[]
    
    
    
    win=False
    erreurs=0
    nb_coups_max=5
    longueur_mot=0
    
    print("Difficulté 1 : mot -7 lettres")
    print("Difficulté 2 : mot entre 6 et 9 lettres")
    print("Difficulté 3 : mot plsu de 9 lettres")
    
    difficulte=int(input("Entrez le niveau de difficulté"))
    
    if(difficulte == 1):
       longueur_mot = 6
    elif(difficulte == 2):
        longueur_mot = random.randint(6,9)
    else:
        longueur_mot = 9
        
    mot=select_word(build_dict(MOTS),longueur_mot)
    
    print(outputStr(mot, lpos))#affiche "_ _ _ _ _ _"
    msg_fin="Perdu le mot était : "+str(mot)
    #boucle principale, saisie des lettre, mise a jour des erreurs et affichage de l'avancement,
    #controle de la condition de victoire
    while not win and erreurs<nb_coups_max:
        print(erreurs, "erreur(s)")
        print("Il reste : "+str(nb_coups_max-erreurs)+" coup(s)")
        lettre=input("entrez une lettre: ").lower()
        new_lettre_pos=places_lettre(lettre, mot)
        if not new_lettre_pos:#la lettre n'est pas dans le mot, +1 erreur,
            erreurs+=1
            ind_pendu+=1 #on rajoute un element a la potence            
        lpos+=(new_lettre_pos)#mise a jour des lettres révélées
        mot_out=outputStr(mot, lpos)#mise a jour du mot avec le nouveau lpos
        print(mot_out)
        #affichage du pendu
        for i in range(ind_pendu,0,-1):
            print(PENDU[i])
        res=mot_out.replace(" ","")#retrait des espaces pour comparer a mot
        #controle de la condition de victoire
        if res==mot:
            win=True
            msg_fin="Gagné!"
            
    print(msg_fin)
        
    

def build_list(fileName:str)->list:
    file=open(fileName,"r", encoding=("utf8"))
    content=file.readlines()
    res=[]
    for i in content:
        part_1=i.split("\t")
        capital=part_1[1].split("\n")
        content=capital[0]
        res.append(content)
    return res
    file.close() 



#build_list("mots.txt")

def build_dict(lst: list) -> dict:
    
    """
    qui prend en paramètre une liste de mots et construit
automatiquement un dictionnaire

    Parameters
    ----------
    lst : list

    Returns
    -------
    dictionnaire_mots : dict

    """
    dictionnaire_mots={}
    for i in lst:
        if not len(i) in dictionnaire_mots:
            dictionnaire_mots[len(i)]=[i]
        else:
            dictionnaire_mots[len(i)].append(i)
    return dictionnaire_mots

#print(build_dict(["bonjour","demain","bientot","matin","universite","pandemie","soleil","tableau","bouteille"]))
                                      
    
def select_word(sorted_words:dict, word_len:int)->str:
    """
    prend en paramètre le dictionnaire précédemment créé et retourne un mot choisi 
     au hasard dans la liste des mots de taille word_len
       

    Parameters
    ----------
    sorted_words : dict
    word_len : int

    Returns
    -------
    res : str


    """
    nb_alea=random.randint(0, len(sorted_words[word_len])-1)
    return sorted_words[word_len][nb_alea]


#dic={5:['paris'],6:['madrid','berlin'],7:['londres','newyork']}
#print(select_word(dic, 6))



#runGame() 





