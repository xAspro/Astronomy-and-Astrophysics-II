import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
L = 10
alpha = 0.3
sigma = 0.5

def I_nu(r):
    return I_nu_0 * np.exp(- (alpha + sigma) * (r ** 3) / 3)

def I_nu2(r):
    return I_nu_0 * np.exp(- (alpha + sigma) * (r*np.log(r)-r)) 

def tau_nu(r):
    return - (alpha + sigma) * (r ** 3) / 3

def tau_nu2(r):
    return - (alpha + sigma) * (r*np.log(r)-r)

r_values = np.linspace(0.1 * L, L, 100)

I_nu_0 = 1000 

I_nu_values = I_nu(r_values)
I_nu_values2 = I_nu2(r_values)

tau_nu_values = tau_nu(r_values)
tau_nu_values2 = tau_nu2(r_values)

plt.plot(r_values, I_nu_values)
plt.xlabel('r')
plt.ylabel('$I_\\nu(r)$')
plt.title('Intensity profile for $r^2$')
plt.grid(True)
plt.show()

plt.plot(r_values, I_nu_values2)
plt.xlabel('r')
plt.ylabel('$I_\\nu(r)$')
plt.title('Intensity profile for $\ln(r)$')
plt.grid(True)
plt.show()

plt.plot(r_values, tau_nu_values)
plt.xlabel('r')
plt.ylabel('$\\tau_\\nu(r)$')
plt.title('Optical Depth for $r^2$')
plt.grid(True)
plt.show()

plt.plot(r_values, tau_nu_values2)
plt.xlabel('r')
plt.ylabel('$\\tau_\\nu(r)$')
plt.title('Optical Depth for $\ln(r)$')
plt.grid(True)
plt.show()

