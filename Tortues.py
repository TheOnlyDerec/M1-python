import numpy as np
import matplotlib.pyplot as plt
from torsNvect import *

class tortue(object):
    def __init__(self, nom='Franklin', pos=Vecteur3d(), orient=0, color='red'):
        self.nom = nom
        self.color = color
        self.pos = [pos]
        self.rot = [orient]
    def __str__(self):
        return self.nom + ' la tortue ' + self.color + ' se trouve en ' + str(self.pos) + ' et est orientée de ' + str(self.rot) + ' radians.\n'
    def __repr__(self):
        return self.nom + ' la tortue ' + self.color + ' se trouve en ' + str(self.pos) + ' et est orientée de ' + str(self.rot) + ' radians.\n'
    def marche(self, distance):
        self.pos.x += np.cos(self.rot) * distance
        self.pos.y += np.sin(self.rot) * distance
    def tourne(self, rot):
        self.orient += rot
    def save(self, file="save.txt"):
        f = open(file, "at")
        f.write(str(self)+'\n')
        f.close
#    def load(self, file):


class essaim(object):
    def __init__(self, taille, positions, orientations):
        self.tortues = []
        for i in range(0,taille-1):
            tort = tortue(positions[i], orientations[i])
            self.tortues.append(tort)
    def deplacer(self, numeros, angles, distances):
        for i in numeros:
            self.tortues[i].pas(angles[i], distances[i])
    def places(self):
        X = []
        Y= []
        for i in self.tortues:
            X.append(i.pos[0])
            Y.append(i.pos[1])
        plt.plot(X, Y, 'x')
        plt.show()
    def histoire(self, pas):
        L = len(self.tortues[0].historix)
        t=np.linspace(0, pas*L, L)

if __name__ == '__main__':
    A = tortue('Angelo', Vecteur3d(0,0,0), 0, 'blue')
    A.save()