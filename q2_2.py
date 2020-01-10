from MMSK.mathAnalysis import *
from MMSK.simulation import *
import matplotlib.pyplot as plt
import math

mu = 6
s = 2
k = 8
x = []
Wqy = []
simWqy = []
for i in range(2, 8):
	x.append(i)
	quSim = queueSim(i, mu, s, k, 10000)
	quSim.simRun()
	simWqy.append(quSim.avgWaitQuTime)
	Wqy.append(Wq(i, mu, s, k)*60)
print('MATH:x = ', x, ', y = ', Wqy)
print('SIM :x = ', x, ', y = ', simWqy)
plt.plot(x, simWqy, 'ro-', label='sim')
plt.plot(x, Wqy, 'g^-', label='math')
plt.title('Wq')
plt.xlabel('lambda')
plt.ylabel('Wq(min)')
tempX = x
for x, y in zip(x, Wqy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(tempX, simWqy):
	plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
plt.legend()
plt.show()