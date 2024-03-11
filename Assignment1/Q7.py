import numpy as np
import matplotlib.pyplot as plt

stefanconst=5.67e-8

# Defining the parameters
L = 10
alpha = 0.3
sigma = 0.5


def F(r, T):
    return -16*stefanconst*(T**3)*900/(3*(alpha+sigma)*r**2*L)


def F2(r, T):
    return -16*stefanconst*(T**3)*900/(3*(alpha+sigma)*np.log(r)*L)

T = np.linspace(100,1000,10)
print(T)
r = np.linspace(0.1*L, L,1000)

for Ti in T:
    plt.plot(r,F(r,Ti),label=('Temp= '+str(Ti)+' K'))
plt.legend()
plt.xlabel('r')
plt.ylabel('F')
plt.title('Energy Flux vs Distance graph(r^2)')
plt.show()

for Ti in T:
    plt.plot(r,F2(r,Ti),label=('Temp= '+str(Ti)+' K'))
plt.legend()
plt.xlabel('r')
plt.ylabel('F')
plt.title('Energy Flux vs Distance graph(ln r)')
plt.show()