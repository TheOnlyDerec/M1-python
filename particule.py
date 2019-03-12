from torsNvect import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


class particule(object):
    def __init__(self, pos=Vecteur3d(), vit=Vecteur3d(), acc=Vecteur3d(), nom='a', m=1):
        self.pos = [pos]
        self.vit = [vit]
        self.acc = [acc]
        self.nom = nom
        self.masse = m
    def __str__(self):
        print('Particule ' + nom + ' en ' + str(self.pos) + '\n')
    def __repr__(self):
        print('Particule ' + nom + ' en ' + str(self.pos) + '\n')
    def setForce(self, F):
        self.acc.append(F/self.masse)
    def ajoutForce(self, F):
        try:
            self.acc.append(self.acc[-1]+F/self.masse)
        except:
            self.setForce(F)
    def simule(self, pas):
        self.pos.append(self.pos[-1] + self.vit[-1]*pas)
        self.vit.append(self.vit[-1] + self.acc[-1]*pas)
    def choc(self, Perp="z", R=0.8):
            if Perp == "x":
                self.vit.append(Vecteur3d(-R*self.vit[-1].x, self.vit[-1].y, self.vit[-1].z))
            if Perp == "y":
                self.vit.append(Vecteur3d(self.vit[-1].x, -R*self.vit[-1].y, self.vit[-1].z))
            if Perp == "z":
                self.vit.append(Vecteur3d(self.vit[-1].x, self.vit[-1].y, -R*self.vit[-1].z))
    def afficheP(self):
        historix = [P.x for P in self.pos]
        history = [P.y for P in self.pos]
        histoz = [P.z for P in self.pos]

        fig = plt.figure('Points')
        ax = fig.gca(projection='3d')

        ax.scatter(historix, history, histoz, c='red', marker='*')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()
    def animeP(self, X=[-1.2, 1.2], Y=[-1.2, 1.2]):
        fig = plt.figure()
        ax = plt.axes(xlim=(X[0], X[1]), ylim=(Y[0], Y[1]))
        line, = ax.plot([], [], lw=2)

        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            x = self.pos[i].x
            y = self.pos[i].y
            line.set_data(x, y)
            return line,

        ani = animation.FuncAnimation(fig, animate, init_func=init, frames=1000, blit=True, interval=1, repeat=False)

        plt.show()


class moteur(object):
    Particules = []
    def __init__(self, nom='t'):
        self.nom = nom
    def ajouterPart(self, part=particule()):
        self.Particules.append(part)
    def removePart(self, nom):
        for P in self.Particules:
            if P.nom == nom:
                self.Particules.remove(P)
    def actu(self, pas):
        for P in self.Particules:
            P.simule(pas)
    def affiche(self):
        xs = [P.pos[-1].x for P in self.Particules]
        ys = [P.pos[-1].y for P in self.Particules]
        zs = [P.pos[-1].z for P in self.Particules]

        fig = plt.figure('Points')
        ax = fig.gca(projection='3d')

        ax.scatter(xs, ys, zs, c='red', marker='*')

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()
    def gravite(self):
        for P in self.Particules:
            P.setForce(Vecteur3d(0, 0, -9.81*P.masse))
    def plotAll(self):
        for Part in self.Particules:
            historix = [P.x for P in Part.pos]
            history = [P.y for P in Part.pos]
            histoz = [P.z for P in Part.pos]

            fig = plt.figure('Points')
            ax = fig.gca(projection='3d')

            ax.scatter(historix, history, histoz, c='red')#, marker='*')

            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')

        plt.show()

# class sysStellaire(object):
#     def __init__(self, centre=particule(), satellites=[]):
#         self.centre=centre
#         self.satellites=satellites
#     def addSat(self, sat):
#         self.satellites.append(sat)
#     def orbite(self, sat):
#         if sat not in self.satellites:
#             pass
#         else:
#             pass

class pendule2(object):
    def __init__(self, pend=particule(), long=1, angleit=np.pi/2, dangleit=0):
        self.pend=pend
        self.long=long
        self.angle = np.array([angleit])
        self.dangle = np.array([dangleit])
        self.ddangle = np.array([0])
    def balance(self, N=10000, pas=0.001):
        for i in range(N):
            self.ddangle[0] = -9.81*np.sin(self.angle[0])/self.long
            self.angle[0] += self.dangle[0]*pas
            self.dangle[0] += self.ddangle[0]*pas
            self.pend.pos.append(Vecteur3d(-np.sin(self.angle[0]),np.cos(self.angle[0]),0))
            self.pend.vit.append(Vecteur3d(-np.cos(self.angle[0])*self.dangle[0],-np.sin(self.angle[0])*self.dangle[0],0))


class pendule(object):
    def __init__(self, pend=particule(), long=1, angleit=np.pi/2, dangleit=0, tau=0):
        self.pend = pend
        self.long = long
        self.angle = angleit
        self.dangle = dangleit
        self.ddangle = 0
        self.tau = tau
    def balance(self, N=1000, pas=0.001):
        for i in range(N):
            self.ddangle = self.dev(self.angle)
            self.angle += self.dangle*pas
            self.dangle += self.ddangle*pas
            self.pend.pos.append(self.jacobienne(self.angle))
            self.pend.vit.append(Vecteur3d(-np.cos(self.angle)*self.dangle,-np.sin(self.angle)*self.dangle,0))
    def jacobienne(self, ang):
        T = Vecteur3d(-np.cos(ang),-np.sin(ang),0)
        return T
    def MGD(self, ang):
        return Vecteur3d(-np.sin(ang), np.cos(ang), 0)
    def dev(self, ang):
        return (self.tau - self.pend.masse*9.81*self.long*np.sin(ang)) / (self.pend.masse*self.long*self.long)

if __name__ == "__main__":
    # A = particule(pos=Vecteur3d(0,0,0), vit=Vecteur3d(1,0,1))
    # B = particule(pos=Vecteur3d(1,0,0), vit=Vecteur3d(0,0,0))
    # C = particule(pos=Vecteur3d(0,1,0), vit=Vecteur3d(0,1,10))
    # D = particule(pos=Vecteur3d(0,0,1), vit=Vecteur3d(2,1,0))
    # A.setForce(Vecteur3d(2,0,0))
    # M = moteur()
    # M.ajouterPart(A)
    # M.ajouterPart(B)
    # M.ajouterPart(C)
    # #M.ajouterPart(D)
    # M.gravite()
    # rebond = True
    # while rebond:
    #     M.actu(0.01)
    #     rebond = False
    #     for P in M.Particules:
    #         if P.pos[-1].z <= 0:
    #             P.choc('z', 0.8)
    #             P.nom = P.nom + '_r'
    #         if not P.nom[-2:] == '_r':
    #             rebond = True
    #
    # M.plotAll()
    A = particule(m=1)
    P = pendule(pend=A)
    P.balance()
    P.pend.afficheP()
