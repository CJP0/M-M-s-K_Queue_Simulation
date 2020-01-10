import numpy as np
import random
import math 
import queue

class customer:
	departTime = 0
	def __init__(self, at, st, s):
		self.arrivalTime = at
		self.serviceTime = st
		self.event = s

class simEventList:
	def __init__(self, lam, mu, n = 0):
		tempServiceTime = int(np.random.exponential(1/mu)*60)
		self.list = [customer(0, tempServiceTime, 'arrival')]
		for i in range(n-1):
			tempServiceTime = int(np.random.exponential(1/mu)*60)
			tempInterArrivalTime = int(np.random.exponential(1/lam)*60)
			self.list.append(customer(self.list[i].arrivalTime+tempInterArrivalTime, tempServiceTime, 'arrival'))
	
	def printList(self):
		print('=======printList======')
		for i in range(len(self.list)):
			print('arrival=', self.list[i].arrivalTime, 'serverT=', self.list[i].serviceTime, 'event=', self.list[i].event)
	
	def insertC(self, temp):
		i = 0
		for i in range(len(self.list)+1):
			if len(self.list) == i:
				break
			if self.list[i].arrivalTime > temp.arrivalTime:
				break
		
		self.list.insert(i, temp)
		
class queueSim:
	def __init__(self, lam, mu, s, k, n):
		self.lam = lam
		self.mu = mu
		self.s = s
		self.k = k
		self.availableServer = s
		self.customerNum = n
		self.waitQueue = queue.Queue(k-s)
		self.eventList = simEventList(lam, mu, n)
		self.currentTime = 0
		self.waitTimeAcc = 0
		self.waitQuTimeAcc = 0
		self.waitLenAcc = 0
		self.waitQuLenAcc = 0
		self.completedNum = 0
		self.servingNum = 0
		self.previousTime = 0
		#self.eventList.printList()
		#print('\n')
		
	def simRun(self):
		while(self.eventList.list):
			temp = self.eventList.list.pop(0)
			self.waitLenAcc += ((self.currentTime - self.previousTime) * (self.servingNum + self.waitQueue.qsize()))
			self.waitQuLenAcc += ((self.currentTime - self.previousTime) * self.waitQueue.qsize())
			self.previousTime = self.currentTime
			self.currentTime = temp.arrivalTime
			if temp.event == 'depart':
				if not self.waitQueue.empty():
					temp2 = self.waitQueue.get()
					self.waitQuTimeAcc += self.currentTime - temp2.arrivalTime
					self.waitTimeAcc += (self.currentTime - temp2.arrivalTime) + temp2.serviceTime
					temp2.arrivalTime = self.currentTime + temp2.serviceTime
					temp2.event = 'depart'
					self.eventList.insertC(temp2)
				else:
					self.servingNum -= 1
					self.availableServer += 1
				self.completedNum += 1
			elif temp.event == 'arrival':
				if self.availableServer > 0:
					temp.arrivalTime += temp.serviceTime
					temp.event = 'depart'
					self.eventList.insertC(temp)
					self.waitTimeAcc += temp.serviceTime
					self.servingNum += 1
					self.availableServer -= 1
				else:
					if not self.waitQueue.full():
						self.waitQueue.put(temp)
			#print('\n--waitQueueSize=', self.waitQueue.qsize(), 'servingNum=', self.servingNum)
			#self.eventList.printList()
		self.avgWaitTime = self.waitTimeAcc/self.completedNum
		self.avgWaitQuTime = self.waitQuTimeAcc/self.completedNum
		self.avgWaitLen = (self.waitLenAcc/self.currentTime)
		self.avgWaitQuLen = (self.waitQuLenAcc/self.currentTime)
		
		