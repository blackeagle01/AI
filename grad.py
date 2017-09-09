import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(100)
y=2*x+9
learningrate=0.009
m,c=np.random.random(2)
def hyp(x):
	global m,c
	return m*x+c
def loss(x,y):
	l=np.sum((hyp(x)-y)**2)/200
	return l
lvalues=[]
def train():
	global m,c,learningrate,lvalues
	for i in range(10000):
		m=m- learningrate*np.sum((hyp(x)-y)*x)/100
		c=c- learningrate*np.sum((hyp(x)-y))/100
		lvalues.append(loss(x, y))
train()
y=np.arange(10000)
plt.plot(y,lvalues)
plt.show()