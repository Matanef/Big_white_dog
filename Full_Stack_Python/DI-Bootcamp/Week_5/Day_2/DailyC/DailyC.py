import random



class Gene():
	def __init__(self):
		self.value = random.choice([True, False]) # True = 1, False = 0

	def mutate(self):
		self.value = not self.value

	def __repr__(self):	
		return "1" if self.value else "0"

	def __str__(self):	
		return f"I'm a gene with value {self.__repr__()}"

	
class Chromosome():
	def __init__(self):
		self.value = [Gene() for i in range(3)]
		
	def mutate(self):
		for gene in self.value:
			if random.choice([True, False]):
				gene.mutate()

	def __repr__(self):
		return str(self.value)


class DNA():
	def __init__(self):
		self.value = [Chromosome() for i in range(3)]

	def mutate(self):
		for chromosome in self.value:
			if random.choice([True, False]):
				chromosome.mutate()


	def __repr__(self):
		return str(self.value)