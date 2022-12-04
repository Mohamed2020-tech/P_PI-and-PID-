import numpy as np
import matplotlib.pyplot as plt
from control.matlab import*


k = 1.2
tau = 0.4
N = 1000
m =0.6865
Wn = 22.511
tau1 = 1/Wn
kr = 12
T =np.linspace(0,10, N)
T0 = 0.26


#systeme 3eme ordre
num3 =np.array([k*Wn**2])
den3 = np.convolve([tau,1],[1,2*m*Wn,Wn**2])
H3 =tf (num3,den3)
print("H3(s)",H3)
HBF3 = feedback(kr*H3,1)
Ys3,T = step (H3, T)
YS3BF,T = impulse(HBF3,T)


#sys_BF_ordre3_corr_P
KrP = 0.5*kr

HBF3P = feedback(KrP*H3,1)
HBF3CP,T = step(HBF3P,T)
plt.figure(1)

#plt.plot(T,HBF3CP)


#sys_BF_ordre3_corr_PI
KrPI =0.45*kr
TauPI = 0.83*T0
numPI =KrPI*np.array([TauPI,1])
denPI = np.array([TauPI,0])
CorrPI = tf(numPI,denPI)
HBF3PI = feedback(CorrPI*H3,1)
HBF3CPI,T = step(HBF3PI,T)
print("PI",CorrPI)


#sys_BF_ordre3_corr_PID
KrPID = 0.6*kr
TauIPID = 0.5*T0
TauDPID = 0.125*T0
numPID =KrPID*np.array([TauIPID*TauDPID,TauIPID,1])
denPID = np.array([TauIPID,0])
CorrPID = tf(numPID,denPID)
HBF3PID = feedback(CorrPID*H3,1)
HBF3CPID,T = step(HBF3PID,T)
print("PID",CorrPID)

plt.title('Réponse impulsionnelle')

plt.plot(T,HBF3CP,label = "P")
plt.plot(T,HBF3CPI,label = "PI")
plt.plot(T,HBF3CPID,label = "PID")
plt.grid()
plt.legend()

plt.show()
