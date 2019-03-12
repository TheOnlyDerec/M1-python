import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)

fig = plt.figure("Exemple de plot simple")

plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy

plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")

plt.ion()
plt.show()

print("on peut faire autre chose sans attendre la fermeture du plot")

for i in range(100):
    
    plt.clf() # Efface le contenu
    y = np.sin(x+i/10)
    plt.plot(x,y)  # on retrace
    fig.canvas.flush_events() # on affiche
        

input("Press a key") # pour empecher la fin du programme et fermeture du plot
