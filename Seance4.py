import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig, (ax1, ax2) = plt.subplots(2,1)
fig.subplots_adjust(hspace=0.5)

ax1.plot(X, C)
ax2.plot(X, S)

plt.show()