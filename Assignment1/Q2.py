import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

# Define the parameters
L=10

def dI_nu(r,I_nu_values):
    return -I_nu_values*r+1/r**2

def tau_nu(r,L):
    return (r**2)/2

def dI_nu2(r,I_nu_values):
    return -I_nu_values*r*np.exp(-r/L)+np.log(r/L)

def tau_nu2(r,L):
    return L**2-L*(r+L)*np.exp(-r/L)



#Range
r0 = 0.1*L
r_end = L

r = np.linspace(r0,r_end, 1000)


I_nu0 = [1000]  
sol = solve_ivp(dI_nu, [r0, r_end], I_nu0, t_eval=np.linspace(r0, r_end, 100))
sol2 = solve_ivp(dI_nu2, [r0, r_end], I_nu0, t_eval=np.linspace(r0, r_end, 100))


plt.plot(sol.t, sol.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (Part 1)')
plt.legend()
plt.show()

plt.plot(r, tau_nu(r, L))
plt.ylabel('Optical depth')
plt.xlabel('r')
plt.title('Optical depth for L = 10m (Part 1)')
plt.legend()
plt.show()

plt.plot(sol2.t, sol2.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (Part 2)')
plt.legend()
plt.show()

plt.plot(r, tau_nu2(r, L))
plt.ylabel('Optical depth')
plt.xlabel('r')
plt.title('Optical depth for L = 10m (Part 2)')
plt.legend()
plt.show()
