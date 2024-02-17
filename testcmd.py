from cmdkit import Command

def methodout(a):
	return a**2

class testcmd(Command):
	def exec(self):
		print("test cmd")
		print("multi line print statements")

		def method(a):
			return a + 2
		
		print(method(3))
		print(methodout(6))
