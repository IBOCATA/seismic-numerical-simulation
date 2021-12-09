# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt


import time
import warnings

# Number of samplepoints
N =200
# sample spacing
T = 20 #durée enregistrée de séisme en s
L=699
U=np.zeros((L))
V=np.zeros((L))
A=np.zeros((L))
I=0
for k in range(0, L):
#Données statistiques des séismes
#onde P
    sigmap=0.15
    mup=0.0

#onde S
    sigmas=0.34
    mus=0.01


#génération du signal sismique
    d = np.concatenate((stats.norm.rvs(mup,sigmap,49), stats.norm.rvs(mus,sigmas,75),np.random.normal(0.01,1.3 , 76)))

#génération du signal sismique
    temps=np.linspace(0,10,200)

    d=exp(-(temps-3)**2/5**2)*d

  



#Génération du spectre de réponse

#amortissement 
    x=0.05

#incrément de temps
    delta_T=temps[2]-temps[1]
#initialisation

    u=np.zeros((N))
    v=np.zeros((N))
    a=np.zeros((N))

    T=np.arange(1,1000,1)

    Su=np.zeros(shape(T))
    Sv=np.zeros(shape(T))
    Sa=np.zeros(shape(T))
#shéma explicite de newmark
    beta=1/6
    gamma=1/2
    for i in range(0, 999):
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


    U[k]=Su[998]
    V[k]=Sv[0]
    A[k]=Sa[0]
    if A[k]>1.6:
        I=I+1

        
X=np.arange(1,L+1,1)

plot(X,U)
xlabel('Nsample')
plt.show()
plot(X,V)
xlabel('Nsample')
plt.show()
plot(X,A)
xlabel('Nsample')
plt.show()

am=np.mean(A)
print(am)
sa=np.std(A)
print(sa)
#Failure probability 
pf=I/(L+1) 
print(pf)
#Confidence interval
inf=am-stats.t.ppf(0.975,L)*sa/sqrt(L+1) 
print(inf)
sup=am+stats.t.ppf(0.975,L)*sa/sqrt(L+1)
print(sup) 