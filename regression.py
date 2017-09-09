import threading,time,sys
from daemon import Daemon
import sys
class job(threading.Thread,Daemon):
	def __init__(self,Id):
		threading.Thread.__init__(self)
		self.Id=Id
	def run(self):
		while True:
			f=open('log.txt','a')
			f.write('hello')
			time.sleep(1)
			
thread=job(7)
thread.start()

