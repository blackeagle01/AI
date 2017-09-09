import numpy as np
m=200
k=3
learningrate=1
X=[10*np.random.random(1) for i in range(m)]
y=[]
for x in X:
	if x[0]<3:
		y.append(0)
	elif x[0]<6:
		y.append(1)
	else:
		y.append(2)
for i,_ in enumerate(X):
	X[i]=np.insert(X[i],0,1)
X=np.array(X)
y=np.array(y)
theta=np.array([np.random.random(2) for i in range(k)])
def output(cl):
	global X
	if cl<=1:
		return np.array(list(map(int,X.sum(axis=1)<3*cl+4))).reshape(1,m)
	else:
		return np.array(list(map(int,X.sum(axis=1)>3*cl+1))).reshape(1,m)
def sigmoid(z):
	return 1/(1+np.exp(-z))
def hyp(X,cl):
	global theta
	return sigmoid(np.dot(theta[cl],X.T)).reshape(1,len(X))
#print(output(2))
def loss(X,cl):
	l=-output(cl)*np.log(hyp(X, cl))-(1-output(cl))*np.log(1-hyp(X,cl))
	return np.sum(l)/(2*m)
def train():
	global k,theta,learningrate
	for cl in range(k):
		for _ in range(1000):
			theta1=theta[cl].copy()
			theta1=theta1-learningrate*((hyp(X, cl)-output(cl))*X.T).sum(axis=1)/m
			theta[cl]=theta1
def predict(x):
	global k
	x=np.array(x).reshape(1,2)
	l=[]
	for cl in range(k):
		l.append(hyp(x, cl))
	return l.index(max(l)) 

train()
print(predict([1,3.89]))
print(loss(X, 2))
