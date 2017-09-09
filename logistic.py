import numpy as np
x=10*np.random.random(100)
y=np.array(list(map(int,x>5)))
m,c=np.random.random(2)
learningrate=0.2
def sigmoid(x):
	return 1/(1+np.exp(-x))
def hyp(x):
	global m,c
	z=m*x+c
	return sigmoid(z)
def loss(x,y):
	l=-y*np.log(hyp(x))-(1-y)*np.log(1-hyp(x))
	return np.sum(l)/200
def train():
	global m,c,learningrate
	for i in range(30000):
		m=m- learningrate*np.sum((hyp(x)-y)*x)/100
		c=c- learningrate*np.sum((hyp(x)-y))/100
def predict(x):
	return np.round(hyp(x))
train()
print(loss(x, y))
print(predict(8))
