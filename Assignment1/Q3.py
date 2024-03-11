import numpy as np
import matplotlib.pyplot as plt 

L=1
T=500

def T_b(T_b0,T,tau_nu):
    return T_b0*np.exp(-tau_nu)+T*(1-np.exp(-tau_nu))


r=np.linspace(0.1*L,L,1000)

plt.plot(r,T_b(100,T,(r**2)/2))
plt.ylabel('Brightness Temperature')
plt.xlabel('r')
plt.title('Brightness Temperature = 100K and 1st part of Q2')
plt.show()

plt.plot(r,T_b(100,T,L**2-L*(r+L)*np.exp(-r/L)))
plt.ylabel('Brightness Temperature')
plt.xlabel('r')
plt.title('Brightness Temperature = 100K and 2nd part of Q2')
plt.show()


plt.plot(r,T_b(10000,T,(r**2)/2))
plt.ylabel('Brightness Temperature')
plt.xlabel('r')
plt.title('Brightness Temperature = 10000K and 1st part of Q2')
plt.show()

plt.plot(r,T_b(10000,T,L**2-(L*r+L**2)*np.exp(-r/L)))
plt.ylabel('Brightness Temperature')
plt.xlabel('r')
plt.title('Brightness Temperature = 10000K and 2nd part of Q2')
plt.show()