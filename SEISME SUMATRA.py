# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:12:03 2020

@author: ilias
""" 

import numpy as np
from scipy import stats
from pylab import *
import scipy.fftpack
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
from scipy import fftpack
from scipy.integrate import odeint

# Number of samplepoints
N = 1400
# sample spacing
T = 300#durée enregistrée de séisme 
x = np.linspace(0.0, T, N)
e=exp(-(x-150)**2/150**2)
#Données statistiques des séismes
#onde P
sigmap=0.16
mup=0

#onde S
sigmas=0.354
mus=0.20


#génération du signal sismique
d = np.concatenate((stats.norm.rvs(mup,sigmap,200), stats.norm.rvs(mus,sigmas,500),np.random.normal(0.3,2 , 700)))

d=d*e
df = pd.DataFrame(data=d.flatten())
stats=df.describe()
# Tracé du signal sismique sample N 
f=linspace(0,T,N)
plot(f,d)
plt.ylabel('accélération')
plt.xlabel('time  s')
show()

#Transformé de fourrier: fonction de transfert
yf = scipy.fftpack.fft(d)

xf = np.linspace(0.0, 33, N)
fig, ax = plt.subplots()
plot(xf, np.abs(yf[:N]))
plt.show()
omega=2*pi/3500
dt = 2*np.pi / omega / 25
fft_d = fftpack.fft(d)
freq = fftpack.fftfreq(len(d), dt)
plt.plot(freq, np.abs(fft_d), lw=3)
plt.show()

#Fréquences sismiques:
FenAcq = d.size
PerEch=5
signal_FFT = abs(fft(d))
signal_freq = fftfreq(FenAcq,PerEch)
signal_FFT = signal_FFT[0:len(signal_FFT)//2]
signal_freq = signal_freq[0:len(signal_freq)//2]

plt.plot(signal_freq,signal_FFT)
plt.show()
#
k=[0.6*1000000000]
m=[1056,2000,3000,4000,5000,6000,7000,8000]
temps=linspace(0,800*2*np.pi*sqrt(m[0]/k[0]),N)
D=[0.002,0.003,0.004,0.005,0.006]
import scipy
# L'équation différentielle sous forme de fonction

def forced_pendulum_equations(y, t, q, acc, omega):
    theta, theta_dot = y
    return [theta_dot, acc * np.sin(omega * t) -\
                   k[0]/m[0]*np.sin(theta) - q * theta_dot]
def forced_pendulum(t_end, t_space, theta_init, theta_dot_init=0, q=0.1,
                            acc=1, omega=1):
    t_range = np.arange(0, t_end, t_space)
    sol = odeint(forced_pendulum_equations, [theta_init, theta_dot_init],
                            t_range, args=(q, acc, omega))
    return np.vstack((t_range, sol.T))

# Pour que odeint renvoit séparément les valeurs de Y et de Y', il faut rajouter .T à la fin
for i in range(0,7):
    def equation(Y,temps):
        # On décompose notre Y en (y,dy) :
        (y,dy)= Y
        # On renvoie ce que vaut Y' :
        return [dy,-sqrt(k[0]/m[i])*y]
    Y,dY=odeint(equation, [0,6], temps).T
    plt.plot(temps,Y)
    plt.title("Déplacement en mètre en fonction du temps en s pour un système non amorti")
    plt.ylabel('amplitude')
    plt.xlabel('time')
    plt.show()
omega=2*pi/3500
dt = 0.2*np.pi / (omega)
tf = 3500
t, theta_0, theta_dot_0 = forced_pendulum(tf, dt,0, 0,
     q=2*sqrt(k[0]*m[0])*D[1],acc=6, omega=omega)
import matplotlib.pyplot as plt
plt.plot(t, theta_0) 
plt.title("Déplacement en m en fonction de temps en seconde pour ONDE DE SURFACE ac=6*g et une période de 3500s")
plt.ylabel('amplitude')
plt.xlabel('time')
plt.show()
plt.plot(t, theta_dot_0)
plt.title("vitesses en fonction de temps accmax=6*g T=3500s")
plt.ylabel('amplitude')
plt.xlabel('time')
plt.show()
t, theta_1, theta_dot_1 = forced_pendulum(tf, dt, 0, 0,
    q=2*sqrt(k[0]*m[0])*D[4], acc=6, omega=omega)
plt.plot(t, theta_1) 
plt.show()
t, theta_2, theta_dot_2 = forced_pendulum(tf, dt,0, 0,
    q=2*sqrt(k[0]*m[0])*D[2],acc=6, omega=omega)
plt.plot(t, theta_2) 
plt.show()
t, theta_3, theta_dot_3 = forced_pendulum(tf, dt, 0, 0,
    q=2*sqrt(k[0]*m[0])*D[1],acc=6, omega=omega)
plt.plot(t, theta_2) 
plt.show()
t, theta_4, theta_dot_4 = forced_pendulum(tf, dt, 0, 0,
    q=2*sqrt(k[0]*m[0])*D[0],acc=6, omega=omega)
plt.plot(t, theta_2) 
plt.show()

