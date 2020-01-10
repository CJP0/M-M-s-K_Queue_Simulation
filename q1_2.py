from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math
    
lam = 2
mu = 1.5
k = 8
x = []
Wy = []
simWy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(lam, mu, i, k, 10000)
	quSim.simRun()
	simWy.append(quSim.avgWaitTime)
	Wy.append(W_(lam, mu, i, k)*60)
print('MATH:x = ', x, ', y = ', Wy)
print('SIM :x = ', x, ', y = ', simWy)
plt.plot(x, simWy, 'ro-', label='sim')
plt.plot(x, Wy, 'g^-', label='math')
plt.title('W')
plt.xlabel('s')
plt.ylabel('W(min)')
tempX = x
for x, y in zip(x, Wy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX, simWy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()