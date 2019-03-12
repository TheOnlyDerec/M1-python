from torsNvect import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class pendule(object):
    def __init__(self, masse=1, l=1, angleit=np.pi/2, dangleit=0, comm=0):
        self.masse = masse
        self.l = l
        self.angle = np.array([angleit])
        self.dangle = np.array([dangleit])
        self.ddangle = np.array([0])
        self.comm = comm
    def actu(self, pas=0.001):
        self.ddangle[0] = self.dev(self.angle[0])
        self.angle[0] += self.dangle[0] * pas
        self.dangle[0] += self.ddangle[0] * pas
    def jacobienne(self, ang):
        T = np.array([-np.cos(ang), -np.sin(ang), 0])
        return T
    def MGD(self, ang):
        return np.array([-np.sin(ang), np.cos(ang), 0])
    def dev(self, ang):
        return (self.comm - self.masse * 9.81 * self.l * np.sin(ang)) / (self.masse * self.l * self.l)


class pendule2(object):
    def __init__(self, masse=1, l=1, angleit=np.pi/2, dangleit=0, comm=0):
        self.masse = masse
        self.l = l
        self.angle = angleit
        self.dangle = dangleit
        self.ddangle = 0
        self.comm = comm
    def actu(self, pas=0.001):
        self.ddangle = self.dev(self.angle)
        self.angle += self.dangle * pas
        self.dangle += self.ddangle * pas
    def jacobienne(self, ang):
        T = np.array([-np.cos(ang), -np.sin(ang), 0])
        return T
    def MGD(self, ang):
        return np.array([-np.sin(ang), np.cos(ang), 0])
    def dev(self, ang):
        return (self.comm - self.masse * 9.81 * self.l * np.sin(ang)) / (self.masse * self.l * self.l)

if __name__ == '__main__':
    xpos = []
    ypos = []
    P = pendule2()
    for i in range(10000):
        XY = P.MGD(P.angle)
        xpos.append(XY[0])
        ypos.append(XY[1])
        P.actu()
    fig = plt.figure('Pendule')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(xpos, ypos)
    plt.show()