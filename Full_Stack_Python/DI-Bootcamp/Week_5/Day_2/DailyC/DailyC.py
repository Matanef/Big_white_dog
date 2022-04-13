import random



class Gene():
	def __init__(self):
        value_list = [0,1]
	    self.value = random.choice(value_list)

	def mutate(self):
            if self.value == 0:
               self.value = 1
        else:
           self.value = 0
		
	def __repr__(self):	
		return str(self.value)

	def __str__(self):	
		return f"Gene {self.__repr__()}"

	
class Chromosome():
	def __init__(self):
		self.genes = [Gene() for i in range(5)]
		
	def mutate(self):
		for gene in self.genes:
			if random.choice([True, False]):
				gene.mutate()

	def __repr__(self):
		return str(self.value)

chromosome = Chromosome()
print(chromosome.genes)


# class DNA():
# 	def __init__(self):
# 		self.value = [Chromosome() for i in range(3)]

# 	def mutate(self):
# 		for chromosome in self.value:
# 			if random.choice([True, False]):
# 				chromosome.mutate()

# 	def __repr__(self):
# 		return str(self.value)


# def