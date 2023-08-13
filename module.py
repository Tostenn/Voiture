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

# class-------------
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
    def __init__(self,nom='',couleur='',formats="moyen") -> None:
        assert not nom.isdigit() and(nom.isalnum() or nom.isalpha()) and len(nom) > 2, 'Voiture.Error: name no int and nom < 2 '
        assert couleur.isalpha(), 'Voiture.Error: couleur str no int ou alnum'
        assert formats.isalpha(), 'Voiture.Error: format str no int ou alnum'

        self.nom  = nom
        self.cl = couleur
        self.format = formats
        Voiture.nbv += 1
        self.serie = self.marque +'-'+str(randint(51,1594))+'-'+str(randint(51,1594))
        self.matr = f'{self.nom[:2]if len(self.nom)>=2 else self.nom}{randint(0,99)}-CI-{Voiture.nbv}'
        if format == 'petit':self.Mreservoir = 500
        elif format == 'moyen':self.Mreservoir =1000
        else:self.Mreservoir = 1500
        self.reservoir = self.Mreservoir//2
    
    def isinstanceVoiture(self,other):
        assert isinstance(other,Voiture) , f"Voiture.Error: {other} no instance of Voiture"
    
    def __eq__(self, other) -> bool:
        '''deux voiture sont identique si ils sont le meme format et la meme serie'''
        self.isinstanceVoiture(other)
        return self.format == other.format and self.serie == other.serie
    
    def __gt__(self,other) -> bool:
        '''une voiture est superieux a une autre si elle a un meilleur format'''
        formatV = ['petit','moyen','grand']
        self.isinstanceVoiture(other)
        return formatV.index(self.format) > formatV.index(other.format)
    
    def __lt__(self,other) -> bool:
        '''une voiture est inférieur a une autre si elle a un faible format'''
        formatV = ['petit','moyen','grand']
        self.isinstanceVoiture(other)
        return formatV.index(self.format) < formatV.index(other.format)

    def __str__(self) -> str:
        '''information lié au vehicule'''
        return f'''information lié votre véhicule
marque : {self.marque}
serie : {self.serie}
nom : {self.nom.upper()}
couleur : {self.cl.upper()}
format : {self.format.upper()}
matricule : {self.matr}
'''

    def __repr__(self) -> str:
        return f'Voiture(nom={self.nom}, couleur={self.cl},format={self.format})'

    def Rempliresv(self,l):
        """remplir le reservoie d'essence"""
        if self.reservoir> self.Mreservoir:
            return False
        self.reservoir+=l
        return self.reservoir
    
    def viderres(self,l):
        """vider le reservoie d'essence"""
        if self.reservoir <=0:
            return False
        self.reservoir-=l
        return self.reservoir

    def essance(self) -> tuple:
        '''essence disponible dans la voiture'''
        return self.reservoir,self.Mreservoir


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

v = Voiture('voiture1','vert','petit')
v2 = Voiture('voiture2','noir')
v3 = Voiture('voiture3','bleu','grand')
print(dir(v))
'''
print('-----------------------------')
print(f'{v}\n{v2}\n{v3}')
print('-----------------------------')
print(f'v > v2 : {v > v2}\nv2 > v3 : {v2 > v3}\nv3 > v : {v3 > v}')
print('-----------------------------')
print(f'v < v2 : {v < v2}\nv2 < v3 : {v2 < v3}\nv3 < v : {v3 < v}')
print('-----------------------------')
print(f'v = v2 : {v == v2}\nv2 = v3 : {v2 == v3}\nv3 = v : {v3 == v}')
'''