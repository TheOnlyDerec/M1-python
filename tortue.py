from torsNvect import *
from math import sin,cos,pi
import matplotlib.pyplot as plt
import socket
from struct import unpack


class Tortue(object):
    def __init__(self,nom='toto',position=Vecteur3d(),orientation=0,color='red'):
        self.nom=nom
        self.color=color
        self.positions=[position]
        self.orientations=[orientation]
        
    def __str__(self):
        msg = self.nom+'('+str(self.positions[-1])+','+str(self.orientations[-1])+')'+self.color
        return msg
        
    def __repr__(self):
        msg = self.nom+'('+str(self.positions[-1])+','+str(self.orientations[-1])+')'+self.color
        return msg
        
    def tourne(self,rad):
        self.positions.append(self.positions[-1])
        self.orientations.append(self.orientations[-1]+rad)
        
    def marche(self,dist):
        a = self.orientations[-1]
        v = Vecteur3d(dist*cos(a),dist*sin(a))
        self.positions.append(self.positions[-1]+v)
        self.orientations.append(self.orientations[-1])
        
    def teleport(self,position=Vecteur3d(),orientation=0):
        self.positions.append(position)
        self.orientations.append(orientation)
        
    def plot(self):
        X=[]
        Y=[]
        plt.figure("La route de "+self.nom)
        for i in self.positions:
            X.append(i.x)
            Y.append(i.y)
            
        plt.plot(X,Y,color=self.color)  
        plt.show(block=False)

    def save(self, file='_|_'):
        if file == '_|_':
            file = self.nom + '.trt'
        f = open(file, "at")
        f.write(self.nom + ' ' + self.color + '\n')
        f.write('Positions : ' + str(self.positions) + '\n')
        f.write('Orientations : ' + str(self.orientations) + '\n')
        f.close()

    def strToTort(self, S):
        T = S.replace('(', ')')
        D = T.replace('\n', '')
        nom, osef1, coord, angle, couleur = D.split(')')
        self.color = couleur
        self.nom = nom
        self.angle = float(angle[1:])
        C = coord.split(',')
        x = float(C[0].replace(' ', ''))
        y = float(C[1].replace(' ', ''))
        z = float(C[2].replace(' ', ''))
        self.position = Vecteur3d(x, y, z)

    def load(self, file = 'save'):
        f = open(file, "rt")
        S = f.readline()
        f.close()
        self.strToTort(S)

    @staticmethod
    def load2(file = 'save'):
        T = Tortue()
        T.load(file)
        return T


class Plage(object):
    
    Tortues=[]
    
    def __init__(self, nom = 'Omaha Beach'):
        self.nom=nom
    
    def ajoutTortue(self,T=Tortue()):
        self.Tortues.append(T)
    
    def enleveTortue(self,nom):
        for t in self.Tortues:
            if t.nom==nom:
                self.Tortues.remove(t)
    
    def trace(self):
        plt.figure('La plage de '+self.nom)
        for t in self.Tortues:
            X=[]
            Y=[]
            for i in t.positions:
                X.append(i.x)
                Y.append(i.y)
            plt.plot(X,Y,color=t.color,label=t.nom)  
            plt.legend()
        plt.show()

    def loadAll(self, file='save'):
        f = open(file, "rt")
        S = f.readlines()
        f.close()
        for str in S:
            T = Tortue()
            T.strToTort(str)
            self.ajoutTortue(T)

    def ile(self, rad, dist):
        for tort in self.Tortues:
            tort.orientations.append(rad)
            tort.positions.append(tort.positions[-1])
            tort.marche(dist)

    def listen(self):
        UDPSock = socket.socket(type=socket.SOCK_DGRAM)
        listen_addr = (socket.gethostname(), 12345)
        UDPSock.bind(listen_addr)
        while True:
            data, addr = UDPSock.recvfrom(1024)
            (num, rad, dist) = unpack('idd', data)
            self.Tortues[num].tourne(rad)
            self.Tortues[num].marche(dist)
            self.trace()


if __name__ == "__main__": # false lors d'un import
    # A = Tortue('Angelo', Vecteur3d(0,0,0), 0, 'blue')
    # A.save()
    # B = Plage()
    # B.loadAll('aaa')
    # print(B.Tortues)


    bob = Tortue('bob')
    mimi = Tortue('mimi',Vecteur3d(2,4),pi/4,'blue')
    Paris=Plage('Paris')

    Franklin = Tortue('Franklin')
    TortueGeniale = Tortue('TortueGeniale', color = 'yellow')
    Donatello = Tortue('Donatello', color = 'purple')
    MichelAngelo = Tortue('MichelAngelo', color = 'green')
    Leonardo = Tortue('Leonardo', color = 'orange')
    Raphael = Tortue('Raphael')

    Paris.ajoutTortue(Franklin)
    Paris.ajoutTortue(TortueGeniale)
    Paris.ajoutTortue(Donatello)
    Paris.ajoutTortue(MichelAngelo)
    Paris.ajoutTortue(Leonardo)
    Paris.ajoutTortue(Raphael)

    Paris.ajoutTortue(bob)
    Paris.ajoutTortue(mimi)
    Paris.Tortues[0].marche(3)
    #
    # bob.tourne(pi/5)
    # bob.marche(10)
    # bob.tourne(-pi/3)
    # bob.marche(4)
    # bob.tourne(pi/9)
    # bob.marche(6)
    # #~ bob.plot()
    #
    #
    # mimi.marche(4)
    # mimi.tourne(pi/2)
    # mimi.teleport(Vecteur3d(1,1))
    # mimi.tourne(pi/.15)
    # mimi.marche(8)
    #~ mimi.plot()

     #~ input()

    # Paris.ile(pi/2, 15)

    Paris.listen()
    #
    # Paris.trace()