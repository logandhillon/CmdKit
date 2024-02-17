from abc import ABC, abstractmethod

commands = {}

class Command(ABC):
	def __init__(self) -> None:
		commands[self.__class__.__name__] = self.exec

	@abstractmethod
	def exec(self):
		pass
