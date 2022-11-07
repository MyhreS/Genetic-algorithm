from random import random

"""
Individual is a class that represents a single individual in a population.
It contains a list of genes, which are represented as 0 and 1.
The genes are randomly generated when the individual is created.
The individual recieves a fitness score when it is created or changed in some way.
"""
#
#
class Individual:
    def __init__(self, bit_string_length):
        self.genes = []
        for i in range(bit_string_length):
            if random() < 0.5:
                self.genes.append(0)
            else:
                self.genes.append(1)
        self.fitness = self.calculate_fitness()


    """
    This method is used to calculate the fitness of the individual.
    Fitness is calculated by the amount of 1's in the genes.
    """
    def calculate_fitness(self):
        self.fitness = 0
        for gene in self.genes:
            if gene == 1:
                self.fitness += 1
        return self.fitness

    """
    This method copies the individual.
    """
    def __copy__(self):
        new_individual = Individual(len(self.genes))
        new_individual.genes = self.genes.copy()
        new_individual.fitness = self.fitness
        return new_individual


