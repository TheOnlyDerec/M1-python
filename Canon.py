from particule import *
from math import sin, cos, pi

V = float(input("Vitesse : \n"))
theta = float(input("Elev :\n"))
phi = float(input('Visee : \n'))

Vit= V*Vecteur3d(cos(phi)*cos(theta),sin(phi),sin(theta))
Pos = Vecteur3d(0,10,0)
m = 10
pas = 0.001
frot = 0.8

historix = []
history = []

P = particule(Pos, Vit, Vecteur3d(0,-9.81*m,0), 'Boulet', m)

while P.pos[-1].y>0:
    historix.append(P.pos[-1].x)
    history.append(P.pos[-1].y)
    P.simule(pas)

plt.plot(historix, history)
plt.show()