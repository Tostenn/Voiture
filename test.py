from module import *
effter()


# récueil des donner ------------

print('''bienvenue dans l'entreprise T_xOx_T pour l'achat 
de votre voiture
''')

format = ['petit','moyen','grand']
cl = ['rouge','bleu','vert']
choix = ["main voiture",'red','moyen']

'''
choix.append(input('entrer le nom de votre voiture : '+vt))

choix.append(
    verch(f'{bl}{"-":-^50}\nchoisir la couleur de votre voiture\n'+'\n'.join(cl)
        +'\nindiquer le numero de la couleur -> ',
        deb=1,
        erro=f'{rg}{"valeur innatendu!":-^50}{bl}'
    )
)

choix.append(
    verch(f'{"-":-^50}\nchoisir le format de votre voiture\n'+'\n'.join(format)
        +'\nindiquer le numero du format -> ',
        deb=1,
        erro=f'{rg}{"valeur innatendu!":-^50}{bl}'
    )
)

loadAnnim()
input('votre voiture est désormais prête! (appuyer sur entrer pour continuer)')
'''

v = Voiture(choix[0],choix[1],choix[2])
position = Poistion()

infoVoiture = f'''tableau de bord {v.nom}
1 - voir les information relative a la voiture
2 - vérifier le niveau d'essence
3 - ajouter de l'essence
4 - changer la couleur de la voture
5 - etat de ma voiture
0 - fin des vérification
-> '''
info = '''Ou on va
1 - verifier l'etat de ma voiture
2 - ou je suis actuellement
3 - lieux disponible 
4 - aller à
5 - sotir de la voiture
-> '''

# mise en place du traitement --------------

while choix != 5:
    effter()
    choix = verch(info,erro=f'{rg}{"valeur innatendu!":-^50}{bl}',deb=1,fin=5)
    
    if choix == 1: #verifier l'etat de ma voiture
        while choix !=0:
            effter()    
            choix = verch(infoVoiture,erro=f'{rg}{"valeur innatendu!":-^50}{bl}',deb=1,fin=5,exp=[0])

            if choix == 1: #voir les information relative a la voiture
                effter()
                input(v) # voir les information relative a la voiture

            elif choix == 2: #vérifier le niveau d'essence
                effter()
                e = v.essance()
                if e[0] < 50:input(logo+'\nil faut qu\'on se depéche pour faire le plein on sera bientot a sec ')
                elif 50 <= e[0] < 250: input(f'{logo}\npensez a refait le plein d\'essanse\nil vous reste {e[0]} litres sur {e[1]}')
                else:input(f'{logo}\non peut faire encore plusieur kilometre avec nos {e[0]} litres')
            
            elif choix == 3: #ajouter de l'essence
                effter()
                e = v.essance()
                if e[0] < 50:print(f'bonne idée de remplit le reservoiir d\'essance il nous restait que {e[0]} ouff')
                elif 50 <= e[0] < 250: print(f'pile poule le bon momoent pour refait le plein on va augmenter nos {e[0]} litres')
                else:print(f'il n\'y a pas a se presser on a encore de l\'enssece\n on peut parcourir {e[0]/50} KM')
                
                rlt()
                if e[0]==e[1]:input(logo+"\nj'ai suis allez vérifié le reservoir et tu sais quoi il est plein")
                else:
                    choix = verch(
                        'combien de litre on la dans la voiture (plein pour faire le plein) ?',
                        erro=f'{rg}{f"niveau d essance {e[0]}/{e[1]} ":-^50}{bl}',
                        deb=1,fin=e[1]-e[0],exp=['plein']
                    )
                    e = v.essance()
                    if choix == 'plein':
                        v.Rempliresv(e[1]-e[0])
                        loadAnnim(msg="entrain de faire le plein de la voiture",nb=20)
                        input(logo+"\nc'est toujours bien de faire le plein ;)")
                    else:
                        v.Rempliresv(choix)
                        loadAnnim(msg="un peu d'essence dans la voiture",nb=20)
                        input(f'{logo}\nregarde le nouveau niveau d\'essance est de {(e[0]/e[1])*100}%')

            elif choix == 4: #changer la couleur de la voture
                effter()
                print("t'aime plus l'ancien couleur pas de probleme dis moi")
                choix = input("quel couleur tu veut : ")
                loadAnnim(msg='mise en place de la nouvelle couleur')
                v.cl = choix
                msgColor = ['la nouvelle couleur de ta voiture déchire trop cool :)','pas mal la nouvelle couleur :|',"c'etait mieux avant :("]
                input(f'{logo}\n{choice(msgColor)}')

            elif choix == 5: #etat de ma voiture
                effter()
                input(f'{logo}\nah la voiture est encore en bonne etat :)')
    
    elif choix == 2: #ou je suis actuellement
        effter()
        if v.roule:input(f'{logo}\nnous nous trouvons sur la route de la {jg}{position.actuel()}{bl}')
        else:input(f'{logo}\nnous nous trouvons actellement à {jg}{position.actuel()}{bl}')

    elif choix == 3: #lieux disponible
        effter()
        e = position.actuel()
        print(f'{"lieu disponible ":-^50}')
        for i in position.destination().values():
            print(f'''nom du lieux : {i[0] if e != i[0] else f'{i[0]} {vt}(emplacement actuelle){bl}'}
description : {i[1]}
disante par rapport a la position actuelle : {i[2] if e == i[0] else position.calculeDistance(i[0])} KM
{"T_xOx_T":-^50}''')
            rlt()
        input()
    
    elif choix == 4: # aller à
        effter()
        e = position.actuel()

        print(f'{"on va rouler super":-^50}')
        if v.reservoir <= 0:input('oh oh plus d\'essence tu viens on va faire le plein') 
        else:
            if not v.roule: # dans le cas ou la voiture demare maintenant
                lieux = position.destination().values()
                nomLieu = [i[0] for i in lieux if i[0] != e]
                choix = verch(f'ou on va avec la voiture actuellement nous somme à {vt}{e}{bl} \n'+'\n'.join(nomLieu)
                    +'\nindiquer le numero du lieux -> ',
                    deb=1,fin=len(nomLieu),
                    erro=f'{rg}{"valeur innatendu!":-^50}{bl}'
                )
                lieux = [i for i in lieux if nomLieu[choix-1] in i][0]
                effter()
                print(f'en avant pour {lieux[1]}')
                rlt()
            else : #dans le cas d'une reprise d'essence en route
                lieux = position.destination().values()
                lieux = [i for i in lieux if e in i][0]
                print(f'{"il est temps de reprendre la route":-^50}')
                rlt()

            if v.reservoir < lieux[-1]:
                print(f'regarde le niveau d\'essance on devra s\'arret au moin {lieux[-1]//v.reservoir} sauf si on fait le plein avant d\'y allé')
                choix = input('on met un peu de jus dans la caisse [o/n] :')
                if choix == 'o':break

            debi = v.reservoir - lieux[-1]
            loadAnnim(msg='roule doucement')
            if debi >0: #arriver a bon port
                input(f"le trajet etait court mais on arrivée par la grace de Dieu nous voila à {lieux[1]}")
                position.positionPre = position.position
                position.updatePos(lieux[0])
                v.viderres(lieux[-1])
                v.roule = False
            else: #manque d'ensence
                v.roule = True
                position.positionPre = position.position
                position.updatePos(lieux[0])
                v.viderres(v.reservoir)
                print(f"on dirait que nous sommes a court d'essence")
                rlt()
                input("ah sauve j'aperçcoir une station allons vite faire le plein")
            choix = 0
    
    elif choix == 5: #sotir de la voiture
        effter()
        print(f'{logo}\nallons prendre un peu d\'air mon ami :)')
        exit()

