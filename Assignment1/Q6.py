import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

h=6.626e-34
k=1.38e-23

# Defining the parameters
L = 10
alpha = 0.3
sigma = 0.5

def dI_nu(r,I_nu_values,T):
    return -(alpha+sigma)*r**2*I_nu_values+alpha*B(T)

def dI_nu2(r,I_nu_values,T):
    return -(alpha+sigma)*np.log(r)*I_nu_values+alpha*B(T)

def dI_nu3(r,I_nu_values,T):
    return -(alpha+sigma)*r**2*(I_nu_values-B(T))

def dI_nu4(r,I_nu_values,T):
    return -(alpha+sigma)*np.log(r)*(I_nu_values-B(T))

def B(T,nu=5.08e14):    #Sodium vapour frequency
    return (8*np.pi*h*nu)/(np.exp((h*nu)/(k*T))-1)


#Numerically solving it
r0 = 0.1*L
r_end = L

T = 2.73 #Because CMB
I_nu0 = [1000]  
sol = solve_ivp(dI_nu, [r0, r_end], I_nu0, args=(T,), t_eval=np.linspace(r0, r_end, 100))


plt.plot(sol.t, sol.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (r^2 and Free Space)')
plt.grid(True)
plt.show()

I_nu0 = [1000]  
sol = solve_ivp(dI_nu2, [r0, r_end], I_nu0, args=(T,), t_eval=np.linspace(r0, r_end, 100))


plt.plot(sol.t, sol.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (ln r and Free Space)')
plt.grid(True)
plt.show()


T = 500
I_nu0 = [1000]  
sol = solve_ivp(dI_nu3, [r0, r_end], I_nu0, args=(T,), t_eval=np.linspace(r0, r_end, 100))


plt.plot(sol.t, sol.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (r^2 and T=500K)')
plt.grid(True)
plt.show()

I_nu0 = [1000]  
sol = solve_ivp(dI_nu4, [r0, r_end], I_nu0, args=(T,), t_eval=np.linspace(r0, r_end, 100))


plt.plot(sol.t, sol.y[0], label='Intensity Profile')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity profile vs r (ln r and T=500K)')
plt.grid(True)
plt.show()