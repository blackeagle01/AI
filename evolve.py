import string
import random
target='cat'
def calfit(strr):
	global target
	l=zip(strr,target)
	count=0
	for x in l:
		if x[0]==x[1]:
			count+=1
	return (count*100)/len(strr)
def allsame(l):
	for x in l[1:]:
		if x!=l[0]:
			return False
	return True
def selectparents(fitness):
	l=[]
	for x in fitness.keys():
		for y in range(fitness[x]):
			l.append(x)
	parents=[]
	if allsame(l):
		return l[0],l[1]
	while len(parents)!=2:
		x=random.choice(l)
		if x not in parents:
			parents.append(x)
	return tuple(parents)
def select(generation):
	fitness={}
	for x in generation:
		fitness[x]=calfit(x)
	parents=selectparents(fitness)
	return parents
def reproduce(parents):
	l1,l2=map(list,parents)
	child=''
	for i in range(len(l1)):
		x=random.randint(0,2)
		if x==0:
			child+=l1[i]
		else:
			child+=l2[i]
	child=mutate(child)
	return child
def mutate(child):
	child=list(child)
	l=list(string.ascii_lowercase)
	for i in range(len(child)):
		x=random.randint(1,101)
		if x==5:
			c=random.choice(l)
			child[i]=c
	return ''.join(child)
def createnewgeneration(generation):
	newgen=[]
	while len(newgen)!=len(generation):
		parents=select(generation)
		child=reproduce(parents)
		newgen.append(child)	 
	return newgen
def optimum(generation):
	fitness={}
	for x in generation:
		fitness[x]=calfit(x)
	maxx=max(fitness.values())
	l=[x for x in fitness.keys() if fitness[x]==maxx]
	return l[0]
'''for i in range(10):
	l=list(target)
	generation=[]
	for i in range(len(l)):
		x=random.randint(1,101)
		if x in range(1,30):
			l[i]='''


if __name__ == '__main__':
	generation=['car','hay','bot','rat']
	for i in range(1,6000):
		generation=createnewgeneration(generation)
		if target in generation:
			print(i)
			print(generation)
			break
	print(optimum(generation))


