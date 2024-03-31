import numpy as np

#Constants
sigma_T=6.652e-29
c=3e8
m=9.109e-31 

def func(B,beta,gamma):
    pow=(sigma_T/(6*np.pi))*c*beta**2*gamma**2*B**2
    t_cool=(gamma*m*c**2)/pow
    return pow,t_cool

#Given values for B and v in terms of c
Question={
    'a':{'B':1e-9,'beta':0.999},
    'b':{'B':1e2,'beta':0.999},
    'c':{'B':1e2,'beta':0.1}
}

for key,val in Question.items():
    B=val['B']
    beta=val['beta']
    gamma=1/np.sqrt(1-beta**2)
    Pow,t_cool=func(B,beta,gamma)
    print(f"For case {key}:")
    print("Synchrotron Power: {:.2e} W".format(Pow))
    print("Cooling Timescale: {:.2e} s".format(t_cool))


