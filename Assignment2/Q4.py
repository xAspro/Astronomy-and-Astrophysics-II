import numpy as np
import matplotlib.pyplot as plt


#Constants
e=1.602e-19
h=6.626e-34
c=3e8
k=1.381e-23 
m=9.109e-31

#defining variables
w0=2.47e15 #Lyman Alpha line for hydrogen
ni=50e-6
ne=ni
geff=1   #Gaunt factor

def alpha(nu,T,Z,ne,ni):

    return (4*e**6/(3*m*h*c))*geff*((2*np.pi)/(3*k*m))**0.5*(1/(T**0.5))*(Z**2*ne*ni/nu**3)*(1-np.exp(-h*nu/(k*T)))

nu=np.linspace(10e8,10e15,1000) 
temperatures=[1000,1e5] 
lengths=[10e5,10e13] 

plt.figure(figsize=(10,6))

for T in temperatures:
    for L in lengths:
        tau=alpha(nu,T,1,ne,ni)*L       #Taking Z=1
        plt.plot(nu,tau,label=f'Length={L}m,T={T}K')

plt.xlabel('Frequency(Hz)')
plt.ylabel('Optical Depth')
plt.title('Optical Depth vs Frequency')
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()
plt.show()