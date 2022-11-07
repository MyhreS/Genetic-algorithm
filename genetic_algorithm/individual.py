
import chromosome as ch

"""
This is a class that represents an individual in a population.
When created it creates a chromosome with the given bit_string_length and calculates fitness.
"""

class Individual:
    def __init__(self, bit_string_length):
        self.chromosome = ch.Chromosome(bit_string_length)
        self.fitness = self.calculate_fitness()

    """
    This method is used to calculate the fitness of the individual.
    It returns the fitness of the individual.
    The fitness is calculated by the number of 1's in the chromosome.
    """
    def calculate_fitness(self):
        fitness = 0
        for gene in self.chromosome.genes:
            if gene == 1:
                fitness += 1
        return fitness

    """
    This method is used to print the individual.
    It returns a string of the individual.
    """
    def __str__(self):
        return "Chromosome: {} Fitness: {}".format(self.chromosome, self.fitness)




