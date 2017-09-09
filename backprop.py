import numpy as np
#np.random.seed(9)
class NeuralNet(object):
	def __init__(self):
		self.inputlayer=4
		self.hiddenlayer=5
		self.outputlayer=1
		self.theta1=2*np.random.rand(self.hiddenlayer,self.inputlayer)-1
		self.theta2=2*np.random.rand(self.outputlayer,self.hiddenlayer)-1
		self.delta1=np.zeros(20).reshape(5,4)
		self.delta2=np.zeros(5).reshape(1,5)
	def activation(self,z,deriv=False):
		if deriv==True:
			return z*(1-z)
		else:
			a=1/(1+np.exp(-z))
			return a
	def predict(self,input):
		#input is a 1*4 matrix
		z2=np.dot(input,self.theta1.T)
		a2=self.activation(z2)
		z3=np.dot(a2,self.theta2.T)
		a3=self.activation(z3)
		print(a3) 
	def train(self,inputs,outputs):
		m=len(inputs)
		for _ in range(500):	
			for x,y in zip(inputs,outputs):
				x.resize(1,len(x))
				#print(x.shape)
				z2=np.dot(x,self.theta1.T)
				a2=self.activation(z2)
				z3=np.dot(a2,self.theta2.T)
				a3=self.activation(z3)
				error3=a3-y
				#print(error3.shape)
				error2=np.dot(error3,self.theta2)*self.activation(a2,deriv=True)
				#print(error2.shape)
				self.delta1+=np.dot(error2.T,x)
				self.delta2+=np.dot(error3.T,a2)
			self.theta1-=self.delta1/m
			self.theta2-=self.delta2/m
n=NeuralNet()
inputs=np.random.randint(0,2,200).reshape(50,4)
for x in inputs:
	x[0]=1
outputs=np.array([x[1]^x[2]^x[3] for x in inputs]).reshape(50,1)
n.train(inputs, outputs)
n.predict([[1,0,1,0]])	
