import numpy as np
import matplotlib.pyplot as plt


#defining variables
w0=2.47e15 #Lyman Alpha line for hydrogen
ni=50e-6

def sigma(w,w0,tau,sigmaT=6.652e-29):
    return sigmaT*(np.power(w,4)/(np.power(np.power(w,2)-np.power(w0,2),2)+np.power(np.power(w0,3)*tau,2)))

w=np.linspace(w0/10000,100*w0,100000)

tau=1/(100*w0)
opticalDepth=sigma(w,w0,tau)*ni*1 #1 because 1 meter

plt.plot(w,opticalDepth,'o-')
plt.plot(w,np.zeros(len(w)),'r-')
plt.xlabel('omega')
plt.ylabel('Optical Depth')
plt.title('Optical Depth vs Omega')
plt.legend(['sigma','0'])
plt.grid(True)
plt.show()



plt.plot(w,opticalDepth,'o-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('omega')

plt.ylabel('Optical Depth')
plt.title('Optical Depth vs Omega Log-Log Plot')

plt.grid(True)
plt.show()