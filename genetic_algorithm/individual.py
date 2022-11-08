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
    """
    Init the individual with genes, bit string bit_string_length and fitness
    """
    def __init__(self, bit_string_length):
        self.bit_string_length = bit_string_length
        if bit_string_length < 10:
            raise ValueError("Bit string bit_string_length must be at least 10")
        self.chromosome = self.create_genes()
        self.fitness = self.calculate_fitness()

    """
    This method created the population genes that is added to the chromosome.
    A gene is a block of 0 and 1.
    The amount of blocks is determined by the bit string bit_string_length.
    """
    def create_genes(self):
        # Find the amount of blocks to split the chromosone genes into
        if self.bit_string_length >= 100:
            split = int(self.bit_string_length / 10)
        elif self.bit_string_length >= 50:
            split = 6
        elif self.bit_string_length >= 25:
            split = 5
        elif self.bit_string_length >= 10:
            split = 4
        else:
            raise ValueError("Bit string bit_string_length must be at least 10")



        # Add genes to chromosome
        chromosome = []
        for i in range(self.bit_string_length):
            chromosome.append(round(random()))
        temp = [chromosome[i:i+split] for i in range(0, len(chromosome), split)]
        chromosome = temp

        return chromosome



    """
    This method is used to calculate the fitness of the individual.
    Fitness is calculated by the amount of 1's in the genes.
    """
    def calculate_fitness(self):
        self.fitness = 0
        for block in self.chromosome:
            for gene in block:
                if gene == 1:
                    self.fitness += 1
        return self.fitness

    """
    This method copies the individual.
    """
    def __copy__(self):
        new_individual = Individual(self.bit_string_length)
        new_individual.chromosome = self.chromosome.copy()
        new_individual.fitness = self.fitness
        return new_individual

    """
    This methods is a string representation of the individual, by printing the chromosome and fitness.
    """
    def __str__(self):
        return "Fitness: " + str(self.fitness) + ", Chromosome: " + str(self.chromosome)



