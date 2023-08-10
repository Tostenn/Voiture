from repertoire import effter,verch,rlt,recujson
from random import randint,choice
effter()


# couleur -------
rg = '\x1b[31m' #rouge
vt = '\x1b[32m' #vert
jg = '\x1b[33m' #jaune
bl = '\x1b[37m' #blanc
logo = f'{"T_xOx_T":-^50}'
# chargement ----------
def loadAnnim(ch = '#',msg = 'confection de votre voiture',nb=25,t=0.3):
    point = [i*'.' for i in range(1,4)]
    for i in range(nb):
        ch +='#'
        print(f'{msg} {point[randint(0,2)]} \n{vt}{ch}{bl}')
        rlt(t)
        effter()

class Voiture:
    '''la voituere T_xOx_T\n
    propriete
        - nom
        - couleur
        - format
        - serie (automatique)
        - marque (automatique)
        - matricule (automatique)\n 
    option
        - possibilité de comparer deux voitures
        - possibilité d'afficher tous les informations d'une voiture 
    '''
    marque = 'T_xOx_T'
    nbv = 0
    roule = False
    def __init__(self,nom,couleur,format) -> None:

        self.nom  = nom
        self.cl = couleur
        self.format = format
        Voiture.nbv += 1
        self.serie = self.marque +'-'+str(randint(51,1594))+'-'+str(randint(51,1594))
        self.matr = f'{self.nom[:2]if len(self.nom)>=2 else self.nom}{randint(0,99)}-CI-{Voiture.nbv}'
        if format == 'petit':self.Mreservoir = 500
        elif format == 'moyen':self.Mreservoir =1000
        else:self.Mreservoir = 1500
        self.reservoir = self.Mreservoir//2
    
    def deco(func):
        print(f'{"_"*7:_^50}')
        print(f'{"T_xOx_T":=^50}')
        # print(f'{"-"*7:-^50}')
        return func
    
    def __eq__(self, other) -> bool:
        '''
        deux voiture sont identique si ils sont le meme format et la meme serie
        '''
        return self.format == other.format and self.serie == other.serie
    
    # @deco
    def __repr__(self) -> str:
        return f'''information lié votre véhicule
marque : {self.marque}
serie : {self.serie}
nom : {self.nom.upper()}
couleur : {self.cl.upper()}
format : {self.format.upper()}
matricule : {self.matr}
'''

    def Rempliresv(self,l):

        if self.reservoir> self.Mreservoir:
            return False
        self.reservoir+=l
        return self.reservoir
    
    def viderres(self,l):
        if self.reservoir <=0:
            return False
        self.reservoir-=l
        return self.reservoir

    def essance(self):return self.reservoir,self.Mreservoir

class Poistion:
    '''gestion de la position et des deplacements'''
    positionPre = ''
    position = 'entreprise T_xOx_T'
    def __init__(self) -> None:
        pass
    
    def actuel(self) ->str:
        '''position actuel'''
        return Poistion.position
    
    def updatePos(self,pos) -> bool:
        '''actualisation de la position'''
        for i,j in self.destination().items():
            if pos in j:
                Poistion.position = pos
                return True
        return False

    def destination(self) -> dict:
        """destination disponible dans l'univers"""
        return recujson('lieux.json')

    def calculeDistance(self,goto) -> int:
        '''calcule la distance entre deux lieux'''
        p = self.actuel()
        dataVille = ''
        for j in self.destination().values():
            if goto in j:
                dataVille = j
            elif p in j:p = j
        return abs(dataVille[-1]-p[-1])
  
'''
creer un reservoir pour la voiture en litre (L)
faire un systeme de vide/rempli
faire roule la voiture
1km = 10L
faire un classe lieux
'''
