from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

mu = 6.0
s = 2
k = 8
x = []
Lqy = []
simLqy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(i, mu, s, k, 10000)
	quSim.simRun()
	simLqy.append(quSim.avgWaitQuLen)
	Lqy.append(Lq(i, mu, s, k))
print('MATH:x = ', x, ', y = ', Lqy)
print('SIM :x = ', x, ', y = ', simLqy)
plt.plot(x, simLqy, 'ro-', label='sim')
plt.plot(x, Lqy, 'g^-', label='math')
plt.title('Lq')
plt.xlabel('lambda')
plt.ylabel('Lq')
tempX = x
for x, y in zip(x, Lqy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX, simLqy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()