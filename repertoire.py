from time import sleep
from json import load

import os,sys


def rlt(x = 0.3) -> True:'''renlanti le programme'''; sleep(x)

def effter() :
        '''efface le terminal'''
        os.system("cls") if sys.platform == "win32" else os.system("clear")
        return True

def verch(info,erro = 'valeur innatendu!', deb = 0,fin = 3,arret=True,exp=[]):
    
    l= list(range(deb,fin+1)) if str(fin).isdigit() else []
    veri = True
    arret = arret if str(arret).isdigit() == True else True
    choix = ''
    while veri and arret:
        choix = input(info)
        if choix.isdigit():
            choix = int(choix)
            if ver_t(exp,[]):
                try:
                    el = exp.index(choix)
                    return exp[el]
                except: pass
            if choix in l: 
                veri = False
                break

            if fin == True:
                veri = False
                break
            else: print(erro)
        else:
            if ver_t(exp,[]):
                try:
                    el = exp.index(choix)
                    return exp[el]
                except: pass
            print(erro)
        if not ver_t(arret,True):
            arret -= 1
            if arret <= 0:veri = False 
    return choix
    # cet fonction d'obtenir le temps

def recujson(ch = 'data.json'):
    '''recupere les donners d'un fichier json'''
    try:
        if __veri_chemin__(ch) == 'ficher':
            with open(ch,'r',encoding='utf-8') as file:
                data = load(file)
            return data
    except: return {}
    
