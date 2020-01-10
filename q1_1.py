from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math
    
lam = 2
mu = 1.5
k = 8
x = []
Ly = []
simLy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, mu, i, k, 20000)
	quSim.simRun()
	simLy.append(quSim.avgWaitLen)
	Ly.append(L_(lam, mu, i, k))
print('MATH:x = ', x, ', y = ', Ly)
print('SIM :x = ', x, ', y = ', simLy)
plt.plot(x, simLy, 'ro-', label='sim')
plt.plot(x, Ly, 'g^-', label='math')
plt.title('L')
plt.xlabel('s')
plt.ylabel('L')
tempX = x
for x, y in zip(x, Ly):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX, simLy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()