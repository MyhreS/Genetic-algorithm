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
    This method is used to change a gene in the chromosome.
    It takes the index of the gene to change and the new value of the gene.
    It returns the old value of the gene.
    """
    def change_gene(self, index, value):
        old_gene = self.genes[index]
        self.genes[index] = value
        self.calculate_fitness()
        return old_gene


    """
    This method is used to mutate a chromosome.
    It takes the mutation rate as a parameter.
    It returns the chromosome with the mutated genes.
    """
    def mutate_chromosome(self, mutation_rate):
        for i in range(len(self.genes)):
            if random() < mutation_rate:
                if self.genes[i] == 0:
                    self.genes[i] = 1
                else:
                    self.genes[i] = 0
        self.calculate_fitness()


    """
    This method is used to print the chromosome.
    It returns a string of the chromosome.
    """
    def __str__(self):
        return "{}".format(self.genes)

