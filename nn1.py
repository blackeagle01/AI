import numpy as np
np.random.seed(1)
class NeuralNet(object):
	def __init__(self):
		self.inputlayer=6
		self.hiddenlayer=4
		self.hiddenlayer1=4
		self.outputlayer=1
	def nonlin(self,z,deriv=False):
		if deriv==True:
			return z*(1-z)
		else:
			return 1/(1+np.exp(-z))
	def train(self,inputs,outputs):
		self.syn0=2*np.random.rand(self.inputlayer,self.hiddenlayer)-1
		self.syn2=2*np.random.rand(self.hiddenlayer1,self.outputlayer)-1
		self.syn1=2*np.random.rand(self.hiddenlayer,self.hiddenlayer1)-1
		for i in range(60000):
			le=np.dot(inputs,self.syn0)
			l1=self.nonlin(le)
			lf=np.dot(l1,self.syn1)
			l2=self.nonlin(lf)
			l3=self.nonlin(np.dot(l2,self.syn2))
			l3_error=outputs-l3
			'''if i%59999==0:
				print("Error matrix:",l3_error)'''
			l3_delta=l3_error*self.nonlin(l3,True)
			l2_error=np.dot(l3_delta,self.syn2.T)
			l2_delta=l2_error*self.nonlin(l2,True)
			l1_error=np.dot(l2_delta,self.syn1)
			l1_delta=l1_error*self.nonlin(l1,True)
			self.syn2+=np.dot(l2.T,l3_delta)
			self.syn1+=np.dot(l1.T,l2_delta)
			self.syn0+=np.dot(inputs.T,l1_delta)
			
	def think(self,a):
		l1=self.nonlin(np.dot(a,self.syn0))
		l2=self.nonlin(np.dot(l1,self.syn1))
		l3=self.nonlin(np.dot(l2,self.syn2))
		return l3
nn=NeuralNet()
#inputs=np.array([[1,1,1],[0,0,1],[0,1,1],[1,0,1]])
inputs=np.random.randint(0,2,1200).reshape(200,6)
#print(inputs)
outputs=np.array([[i[0] or i[1] for i in inputs]]).T
nn.train(inputs,outputs)
testinput=np.array(np.random.randint(0,2,300).reshape(50,6))
testoutput=np.array([[i[0] or i[1] for i in testinput]]).T
netoutput=nn.think(testinput)
error=netoutput- testoutput
print(np.std(error.ravel()))
