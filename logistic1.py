import numpy as np
m=100;n=2
np.random.seed(1)
X=[np.random.random(2) for i in range(100)]
for i,_ in enumerate(X):
	X[i]=np.insert(X[i],0,1)
X=np.array(X)
X=X**2
learningrate=1.2
y=np.array(list(map(int, X.sum(axis=1)<2)))
theta=np.random.random(3)
def sigmoid(z):
	return 1/(1+np.exp(-z))
def hyp(X):
	global theta
	X=np.array(X)
	return sigmoid(np.dot(theta,X.T))
def loss(X,y):
	return -np.sum(y*np.log(hyp(X))+(1-y)*np.log(1-hyp(X)))/100
def train():
	global theta,learningrate
	for _ in range(30000):
		theta1=theta.copy()
		theta1-= learningrate*((hyp(X)-y).reshape(1,100)*X.T).sum(axis=1)/200
		theta=theta1
def predict(x):
	return np.round(hyp(x))
train()
print(predict([[1,0,0.9]]))
print(loss(X, y))