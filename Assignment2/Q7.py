import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

#Constants
alpha=np.pi/2  # Angle alpha is pi/2, sin(alpha) = 1

e=1.602e-19
C=1 #Constant in N(E)=C E^-p
c=3.0e8 
m=9.109e-31

def Alpha_nu(B,p,omega):
    nu=omega/(2*np.pi)
    return (np.sqrt(3)*e**3)/(8*np.pi*m)*pow((3*e)/(2*np.pi*m**3*c**5),(p/2))*C*pow((B*np.sin(alpha)),((p+2)/2))*gamma((3*p+2)/12)*gamma((3*p+22)/12)*np.power(nu,(-(p+4)/2))

def optical_depth(alpha_nu,l):
    return alpha_nu*l

Question={
    'a':{'B':1e-9,'beta':0.999},
    'c':{'B':1e2,'beta':0.1}
}

p_values=[2.5, 4]
L=[10**2,10**10]
omega=np.linspace(10e9, 1e12, 10000)


for p in p_values:
    print(f"For p = {p}:")

    for l in L:
        print(f"For l = {l}:")
        fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,6))

        for key,val in Question.items():
            B=val['B']
            beta=val['beta']
            alpha_nu=Alpha_nu(B,p,omega)
            tau=optical_depth(alpha_nu,l)

            ax1.plot(omega,tau,label=f"Q5 Part {key}")
            ax2.plot(omega,tau,label=f"Q5 Part {key}")

        fig.suptitle(f'Total Power Emitted vs. Angular Frequency for p = {p} and l = {l} Km')

        ax1.set_xlabel('Frequency (Hz)')
        ax1.set_ylabel('Total Power (W)')
        ax1.legend()
        ax1.grid(True)

        ax2.set_xlabel('Frequency (Hz)')
        ax2.set_ylabel('Total Power (W)')
        ax2.set_title('loglog plot')
        ax2.legend()
        ax2.grid(True)
        ax2.set_yscale('log')
        ax2.set_xscale('log')

        plt.tight_layout()
        plt.show()