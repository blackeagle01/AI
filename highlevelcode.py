import threading
import pxssh
import time
import os
import fileparser
class Server(threading.Thread):
	def __init__(self,credentials):
		threading.Thread .__init__(self)
		self.hostname=credentials['hostname']
		self.username=credentials['username']
		self.password=credentials['password']
	def login(self):
		s=pxssh.pxssh()
		s.login(self.hostname,self.username,self.password)
		self.server=s

	def monitor(self):
		self.server.sendline('free -m')
		self.server.prompt()
		self.savelog(self.server.before)

	def run(self):
		self.login()
		self.monitor()
database=fileparser.datadict()
threads=[Server(data) for data in database]
for thread in threads:
	thread.start()

