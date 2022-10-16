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
 
