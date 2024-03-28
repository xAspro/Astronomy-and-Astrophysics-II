import numpy as np
import matplotlib.pyplot as plt

# Constants
e=1.602e-19
c=3e8
k=1.381e-23
h=6.626e-34

m=2*9.109e-31

def P(T,nu,Z,ne,ni,geff):
    return 32*np.pi*e**6*geff/(3*m*c**3)*np.sqrt(2*np.pi/(3*k*m))*np.exp(-h*nu/(k*T))*1/np.sqrt(T)*Z**2*ne*ni


nuValues=np.logspace(2,13,num=1000,base=10)

# Parameters in SI Units(Given)
TValues=[1000,10**5]
ne=1e5
ni=1e5

#Lets choose these Parameters to be 1
Z=1
geff=1

#Holds the P for both the temperatures
p2=[]
for T in TValues:
    p2.append([P(T,nu,Z,ne,ni,geff) for nu in nuValues])


plt.figure(figsize=(10,6))
for i,T in enumerate(TValues):
    plt.plot(nuValues/1e6,p2[i],'o-',label=f'T={T}K')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency(MHz)')
plt.ylabel('Emission Power(W/m^3/Hz)')
plt.title('Bremsstrahhlung Emission Power Spectrum')
plt.legend()
plt.grid(True)
plt.show()
