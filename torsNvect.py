class Vecteur3d(object):
    def __init__(self, a=0, b=0, c=0):
        self.x=a
        self.y=b
        self.z=c
    def affiche(self):
        print(self.x, self.y, self.z)
    def __add__(self, other):
        return Vecteur3d(self.x+other.x, self.y+other.y, self.z+other.z)
    def __str__(self):
        return "Vecteur3d(%g, %g, %g)" % (self.x, self.y, self.z)
    def __pow__(self, other):
        if type(other)==Vecteur3d:
            return self.x*other.x + self.y*other.y + self.z*other.z
        else:
            return Vecteur3d(other*self.x, other*self.y, other*self.z)
    def __rpow__(self, other):
        return self*other
    def __neg__(self):
        return Vecteur3d(-self.x, -self.y, -self.z)
    def __sub__(self, other):
        return self+(-other)
    def __repr__(self):
        return "Vecteur3d(%g, %g, %g)" % (self.x, self.y, self.z)
    def __mul__(self, other):
        if type(other)==Vecteur3d:
            x1=self.x
            x2=other.x
            y1=self.y
            y2=other.y
            z1=self.z
            z2=other.z
            return Vecteur3d(y1*z2-y2*z1, z1*x2-z2*x1, x1*y2-x2*y1)
        else:
            return Vecteur3d(other*self.x, other*self.y, other*self.z)
    def mod(self):
        return (self.x**2+self.y**2+self.z**2)**0.5  #(self**self)**0.5
    def norme(self):
        N=self.mod()
        return self*(1/N)
    def __rmul__(self, other):
        return self*other
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y and self.z==other.z
    def __gt__(self, other):
        return self.mod()>other.mod()
    def __lt__(self, other):
        return self.mod() < other.mod()
    def __ge__(self, other):
        return not self<other
    def __le__(self, other):
        return not self>other
    def __truediv__(self, other):
        return Vecteur3d(self.x/other, self.y/other, self.z/other)  #self*(1/other)
    def normed(self):
        M=self.norme()
        self.x=M.x
        self.y=M.y
        self.z=M.z

def inputVect(msg=''):
    print(msg)
    x = float(input('x :\n'))
    y = float(input('y :\n'))
    z = float(input('z :\n'))
    return Vecteur3d(x, y, z)

def inputVect2(msg=''):
    print(msg)
    liste = input('Donner le vecteur sous la forme (x,y,z)\n')
    liste=liste[1:-1]
    liste.split(',')
    x=float(liste[0])
    y=float(liste[2])
    z=float(liste[4])
    return Vecteur3d(x, y, z)


class torseur(object):
    """Point, résultante, moment"""
    def __init__(self, pt=Vecteur3d(), res=Vecteur3d(), mt=Vecteur3d()):
        self.pt=pt
        self.res=res
        self.mt=mt
    def trans(self, pt):
        self.mt=self.mt+(pt-self.pt)*self.res
        self.pt=pt
    def __add__(self, other):
        if self.pt==other.pt:
            return torseur(other.pt, self.res+other.res, self.mt+other.mt)
        else:
            temp=torseur(other.pt, other.res, other.mt)
            temp.trans(self.pt)
            return self+temp
    def __str__(self):
        return 'Point : '+self.pt.__str__()+', Résultante : '+self.res.__str__()+', Moment : '+self.mt.__str__()
    def __repr__(self):
        return 'Point : '+self.pt.__str__()+', Résultante : '+self.res.__str__()+', Moment : '+self.mt.__str__()
    def __mul__(self, other):
        if type(other) == torseur:
            return self.mt**other.res+self.res**other.mt
        else:
            return torseur(self.pt, other*self.res, other*self.mt)
    def __rmul__(self, other):
        return self*other
    def __sub__(self, other):
        return self+(-other)
    def __neg__(self):
        return torseur(self.pt, -self.res, -self.mt)

def inputTors():
    pt=inputVect2('Entrez le point :')
    res = inputVect2('Entrez la resultante :')
    mt = inputVect2('Entrez le moment :')

    return torseur(pt, res, mt)

if __name__=="__main__": #False lors d'un import
#    print(dir(Vecteur3d))

    V1=Vecteur3d(1,0,0)
    V3=Vecteur3d(0,1,0)
    V2=Vecteur3d(0,0,1)
    V=Vecteur3d(0,1,0)
    U=Vecteur3d(1,0,0)
    W=Vecteur3d(0,0,1)
    U1=Vecteur3d(0,0,0)
    T1=torseur(U,V,W)
    T2=torseur(U1,V,W)
    T1.trans(V2)
    print(T1)