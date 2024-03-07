import numpy as np
import matplotlib.pyplot as plt

# Define length of the system
L = 1.0

# Define range of r values
r_values = np.linspace(0.1 * L, L, 100)

# Define reference coefficients
alpha0 = 1.0
sigma0 = 1.0

# Define the Planck function B_nu for a blackbody
def B_nu(nu, T):
    h = 6.626e-34  # Planck's constant (J s)
    c = 3.0e8      # Speed of light (m/s)
    k = 1.381e-23  # Boltzmann constant (J/K)
    return 2 * h * nu**3 / c**2 / (np.exp(h * nu / (k * T)) - 1)

# Solve the radiative transfer equation numerically for r^2 variation
I_nu_r2 = np.zeros_like(r_values)
tau_r2 = np.zeros_like(r_values)
I_nu_ln = np.zeros_like(r_values)
tau_ln = np.zeros_like(r_values)

for i, r in enumerate(r_values):
    # For r^2 variation
    alpha_nu_r2 = alpha0 * r**2
    sigma_nu_r2 = sigma0 * r**2
    
    # For ln(r) variation
    alpha_nu_ln = alpha0 * np.log(r)
    sigma_nu_ln = sigma0 * np.log(r)
    
    # Define a step size ds
    ds = 0.01
    
    # Initialize variables for r^2 variation
    I_nu_r2_val = 0.0
    tau_nu_r2 = 0.0
    
    # Initialize variables for ln(r) variation
    I_nu_ln_val = 0.0
    tau_nu_ln = 0.0
    
    # Define the range of s from 0 to L
    s_values = np.arange(0, L, ds)
    
    # Iterate over s values and integrate the radiative transfer equation for r^2 variation
    for s in s_values:
        dI_nu_ds_r2 = -alpha_nu_r2 * (I_nu_r2_val - B_nu(nu=1.0, T=300)) - sigma_nu_r2 * (I_nu_r2_val - B_nu(nu=1.0, T=300))
        dtau_nu_ds_r2 = alpha_nu_r2 + sigma_nu_r2
        
        I_nu_r2_val += dI_nu_ds_r2 * ds
        tau_nu_r2 += dtau_nu_ds_r2 * ds
    
    # Iterate over s values and integrate the radiative transfer equation for ln(r) variation
    for s in s_values:
        dI_nu_ds_ln = -alpha_nu_ln * (I_nu_ln_val - B_nu(nu=1.0, T=300)) - sigma_nu_ln * (I_nu_ln_val - B_nu(nu=1.0, T=300))
        dtau_nu_ds_ln = alpha_nu_ln + sigma_nu_ln
        
        I_nu_ln_val += dI_nu_ds_ln * ds
        tau_nu_ln += dtau_nu_ds_ln * ds
    
    # Assign values for r^2 variation
    I_nu_r2[i] = I_nu_r2_val
    tau_r2[i] = tau_nu_r2
    
    # Assign values for ln(r) variation
    I_nu_ln[i] = I_nu_ln_val
    tau_ln[i] = tau_nu_ln

# Plot observed intensity and optical depth as functions of r for r^2 variation
plt.figure()
plt.plot(r_values, I_nu_r2, label='Observed Intensity (with r^2 form)')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Observed Intensity vs. r (with r^2 form)')
plt.legend()

plt.figure()
plt.plot(r_values, tau_r2, label='Optical Depth (with r^2 form)')
plt.xlabel('r')
plt.ylabel('Optical Depth')
plt.title('Optical Depth vs. r (with r^2 form)')
plt.legend()

# Plot observed intensity and optical depth as functions of r for ln(r) variation
plt.figure()
plt.plot(r_values, I_nu_ln, label='Observed Intensity ln(r)')
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Observed Intensity vs. r (with ln(r) form)')
plt.legend()

plt.figure()
plt.plot(r_values, tau_ln, label='Optical Depth (with ln(r) form)')
plt.xlabel('r')
plt.ylabel('Optical Depth')
plt.title('Optical Depth vs. r (with ln(r) form)')
plt.legend()

plt.show()
