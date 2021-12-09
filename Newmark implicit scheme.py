# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 17:33:31 2021

@author: ilias bounsir
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt




# Number of samplepoints
N =200
# sample spacing
T = 20 #durée enregistrée de séisme en s


#Données statistiques des séismes
#onde P
sigmap=0.15
mup=0.0

#onde S
sigmas=0.34
mus=0.01
X=np.arange(1,100,1)
#génération du signal sismique
d = np.concatenate((stats.norm.rvs(mup,sigmap,49), stats.norm.rvs(mus,sigmas,75),np.random.normal(0.01,1.1 , 76)))


temps=np.linspace(0,20,200)

d=exp(-(temps-10)**2/10**2)*d

plot(temps,d)
ylabel('acceleration(m/s2)')
xlabel('time(s)')
plt.show()

#Génération du spectre de réponse

#amortissement 
x=0.05

#incrément de temps
delta_T=temps[2]-temps[1]
#initialisation

u=np.zeros((N))
v=np.zeros((N))
a=np.zeros((N))

T=np.arange(1,100,0.1)
f=1/T
Su=np.zeros(shape(T))
Sv=np.zeros(shape(T))
Sa=np.zeros(shape(T))
#shéma implicite de newmark
beta=1/6
gamma=1/2
for i in range(0, 990):
    w=2*pi/T[i]
    for j in range(0,N-1):
        a[j+1]=(d[j+1]-w**2*u[j]-(2*x*w+2*delta_T*w**2)*v[j]-w*delta_T*(2*x*(1-gamma)+w*delta_T*(1-2*beta)/2)*a[j])/(1+((w*delta_T)**2)*beta+2*x*w*gamma)
        v[j+1]=v[j]+delta_T*((1-gamma)*a[j]+gamma*a[j+1])
        u[j+1]=u[j]+delta_T*v[j]+(delta_T**2/2)*((1-2*beta)*a[j]+2*beta*a[j+1])
    Sa[i]=np.max(abs(a))
    Sv[i]=np.max(abs(v))
    Su[i]=np.max(abs(u))
    u=np.zeros((N))
    v=np.zeros((N))
    a=np.zeros((N))
    
#génération du spectre de réponse

plot(T,Sa)
plt.xscale('log')
plt.xlabel('periode en s')
plt.ylabel('acceleration en m/s2')
plt.show()

plot(T,Su)
plt.xlabel('periode en s')
plt.ylabel('displacement en m')
plt.xscale('log')
plt.show()

plot(T,Sv)
plt.xlabel('periode en s')
plt.ylabel('velocity en m/s')
plt.xscale('log')
plt.show()
    