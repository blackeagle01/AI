import numpy as np
class NeuralNet:
	def __init__(self):
		self.inputlayer=4
		self.hiddenlayer=5
		self.outputlayer=1
		self.theta1=2*np.random.random((self.hiddenlayer,self.inputlayer))-1
		self.theta2=2*np.random.random((self.outputlayer,self.hiddenlayer))-1
		self.delta1=np.zeros(20).reshape(5,4)
		self.delta2=np.zeros(5).reshape(1,5)
	def activation(self,z,deriv=False):
		if deriv==True:
			return z*(1-z)
		else:
			return 1/(1+np.exp(-z))
	def train(self,inputs,outputs):
		m=len(inputs)
		for _ in range(100):
			for x,y in zip(inputs,outputs):
				x.resize(len(x),1)
				y.resize(len(y),1)
				z2=np.dot(self.theta1,x)
				a2=self.activation(z2)
				z3=np.dot(self.theta2,a2)
				a3=self.activation(z3)
				error3=a3-y
				error2=np.dot(self.theta2.T,error3)*self.activation(a2,True)
				self.delta1+=np.dot(error2,x.T)
				self.delta2+=np.dot(error3,a2.T)
			self.theta1-=(self.delta1)/m
			self.theta2-=(self.delta2)/m
	def predict(self,x):
		x=np.array(x)
		x=x.T
		z2=np.dot(self.theta1,x)
		a2=self.activation(z2)
		z3=np.dot(self.theta2,a2)
		a3=self.activation(z3)
		print(a3)
nn=NeuralNet()
inputs=np.random.randint(0,2,200).reshape(50,4)
for x in inputs:
	x[0]=1
outputs=np.array([x[1] and x[2] and x[3] for x in inputs]).reshape(50,1)
print(inputs,outputs)
#nn.train(inputs,outputs)
#nn.predict([[1,1,1,1]])