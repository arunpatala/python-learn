
class IOString():

	def __init__(self):
		self.s = ""

	def read(self):
		self.s = raw_input()

	def write(self):
		print self.s


ios = IOString()
ios.read()
ios.write()
	


