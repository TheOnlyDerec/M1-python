from torsNvect import *

class Solide(object):
    def __init__(self, M=0, Forces=[], Liaisons=[], S=torseur()):
        self.M=M
        for F in Forces:
            self.ajoutForce(F)
        self.Liaisons=Liaisons
        self.S=S
        CM = Vecteur3d(0,0,0) #CM : Origine du repère du solide et centre de masse
        ResP = Vecteur3d(0,0,-9.81*M)
        MtP = Vecteur3d(0,0,0)
        Poids = Torseur(CM, ResP, MtP)
        self.ajoutForce(Poids) #Ajout du poids
        self.eq()
    def ajoutForce(self, F):
        self.Forces.append(F)
        self.actuS(F)
    def actuS(self, F):
        self.S = self.S - F.trans(Vecteur3d(0,0,0))
    def eq(self):
        Nul = Vecteur3d(0,0,0)
        self.S = torseur(Nul, Nul, Nul)
        for T in Forces:
            self.actuS(T)


def inputSolide():
    M= input('Donner masse du solide : \n')


class Structure(object):
    def __init__(self, posSol=Vecteur3d(), Solides={}):
        """posSol : position du premier solide de la structure
        Solides : Dictionnairedes solides avec leur arborescences"""
        self.posSol=posSol
        self.Solides=Solides