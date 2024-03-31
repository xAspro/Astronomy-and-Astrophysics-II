import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt

#Constants
alpha=np.pi/2  # Angle alpha is pi/2, sin(alpha) = 1

e=1.602e-19
C=1 #Constant in N(E)=C E^-p
c=3.0e8 
m=9.109e-31

def Power(B,p,omega):
    return (np.sqrt(3)*e**3*C*B*np.sin(alpha))/(2*np.pi*m*c**2*(p+1))*gamma(p/4+19/12)*gamma(p/4-1/12)*(np.power(((m*c*omega)/(3*e*B*np.sin(alpha))),((1-p)/2)))


Question={
    'a':{'B':1e-9,'beta':0.999},
    'c':{'B':1e2,'beta':0.1}
}

p_values=[2.5,4]
omega=np.linspace(10e9,1e12,10000)


for p in p_values:

    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,6))

    print(f"For p = {p}:")
    for key,val in Question.items():
        B=val['B']
        beta=val['beta']
        P_tot=Power(B,p,omega)

        ax1.plot(omega,P_tot,label=f"Q5 Part {key}")
        ax2.plot(omega,P_tot,label=f"Q5 Part {key}")

    fig.suptitle(f'Total Power Emitted vs. Angular Frequency for p = {p}')

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