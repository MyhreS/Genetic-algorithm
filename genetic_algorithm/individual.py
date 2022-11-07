from random import random

"""
Individual is a class that represents a single individual in a population.
It has genes that are 0 or 1. When created, this is random.
The amount of genes is determined by the user through the bit_string_length parameter in the constructor.
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


    """
    This method is used to change a gene in the chromosome.
    It takes the index of the gene to change and the new value of the gene.
    It returns the old value of the gene.
    """
    def change_gene(self, index, value):
        old_gene = self.genes[index]
        self.genes[index] = value
        return old_gene


    """
    THis method is used to mutate a chromosome.
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


    """
    This method is used to print the chromosome.
    It returns a string of the chromosome.
    """
    def __str__(self):
        return "{}".format(self.genes)

