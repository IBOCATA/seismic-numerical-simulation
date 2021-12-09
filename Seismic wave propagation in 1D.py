# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:13:41 2021

@author: ilias bounsir
"""

import numpy as np
import pandas as pd
from scipy import stats
from pylab import *
import matplotlib.pyplot as plt



#Données statistiques des séismes
#onde P
sigmap=0.1
mup=0.0

#onde S
sigmas=0.154
mus=0.08


#génération du signal sismique
d = np.concatenate((stats.norm.rvs(mup,sigmap,90), stats.norm.rvs(mus,sigmas,350),np.random.normal(0.01,1.2 , 310)))


temps=np.linspace(0,200,750)

d=exp(-(temps-100)**2/100**2)*d
plot(temps,d)
plt.ylabel('acceleration(m/s2')
plt.xlabel('time(s)')
show()
#vitesse en m/S
Vs= np.concatenate((np.full(200,100), np.full(450,290),np.full(350, 320)))


#Profondeur en m
h=1000
f=linspace(0,h,1000)
plot(f,Vs)
plt.ylabel('Velocity(m/s2)')
plt.xlabel('depth (m)')
show()
#duree de simulation en s
T=200
#Maillage

Nt=750
Nz=10
t=T/Nt
z=h/Nz
# Initialisation
s=(Nt,Nz)
U=np.zeros(s)
Z=np.linspace(0,h,Nz)
U[0,:]=1
U[:,0]=d
U[1,:]=U[0,:]
for i in range(1,Nt-2):
    for j in range(1,Nz-2):
        U[i+1,j]=2*U[i,j]-U[i-1,j]+(t/z)**2*(Vs[j+1]**2*(U[i,j+1]-U[i,j])-Vs[j]**2*(U[i,j]-U[i,j-1]))
        
#Condition de Neumann
for i in range(1,Nt-2):
    U[i+1,Nz-1]=2*U[i,Nz-1]-U[i-1,Nz-1]+2*(t/z)**2*Vs[Nz-1]**2*(U[i,Nz-2]- U[i,Nz-1]) 
Onde=np.transpose(U)           



plt.plot(temps, U[:,1], label='depth 100m')   # Signal sismique à 100m
plt.plot(temps, U[:,2], label='depth 200m')  
plt.plot(temps, U[:,3], label='depth 300m') 
plt.plot(temps, U[:,4], label='depth 400m') 
plt.plot(temps, U[:,5], label='depth 500m') 
plt.plot(temps, U[:,6], label='depth 600m') 
plt.plot(temps, U[:,7], label='depth 700m') 
plt.title('Seismic amplification in heterogenous soil media')      # Titre
plt.xlabel('time(s)')                      # Légende abscisse
plt.ylabel('acceleration (m/s2)')                      # Légende ordonnée
plt.legend()                         # Ajout de la légende
plt.grid()                           # Ajout d'une grille
plt.show()                           # Affichage




  

#Description statistique du signal à 700m
df = pd.DataFrame(data=U[:,7].flatten())
stats=df.describe()  