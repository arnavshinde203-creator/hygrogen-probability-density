import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from scipy.special import genlaguerre
from scipy.special import lpmv
from mpl_toolkits.mplot3d import Axes3D

a0 =1  #bohr radius in angstrom
def R(n,l,r):                     #radial wavefunction
    rho = (2*r)/(n*a0)
    norm = np.sqrt(((2/(n*a0))**3) * factorial(n-l-1)/(2*n*factorial(n+l)))  #normalization constant
    Lag_poly = genlaguerre(n-l-1,2*l+1)                                 #associated laguerre polynomial 
    R = norm*(rho**l)*np.exp(-rho/2)*Lag_poly(rho)
    return R 

def rp(n,l,r):                        #radial probability density
    Rnl = R(n,l,r)
    return (r**(2))*(abs(Rnl)**2)


def Ylm(l,m,theta,phi):
    norm = np.sqrt(((2*l+1)/(4*np.pi))*(factorial(l-m)/factorial(l+m))) 
    x = np.cos(theta)
    Legendre_polynomial = lpmv(m,l,x)

    return norm*Legendre_polynomial*np.exp(1j*m*phi)

def angular_prob(l,m,theta,phi):
    Y = Ylm(l,m,theta,phi)
    return np.abs(Y)**2

x = np.linspace(-30,30,2000)
z = np.linspace(-30,30,2000)
X,Z = np.meshgrid(x,z)

r = np.sqrt(X**2 + Z**2)
theta = np.arccos(Z/(r+1e-12))
phi = 0

n,l,m = 3,2,0
Rnl = R(n,l,r)
Y_prob = Ylm(l,m,theta,phi)

psi_2 = np.abs(Rnl*Y_prob)**2

plt.figure(figsize=(10,10))
plt.imshow(np.sqrt(psi_2),extent=[-20,20,-20,20],origin='lower',cmap='inferno')
plt.xlabel("x")
plt.ylabel("z")
plt.title("Hydrogen orbital density")
plt.colorbar(label="|ψ|²")
plt.show()




