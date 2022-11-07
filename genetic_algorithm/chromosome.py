from random import random


# Chromosome is a class that represents a single chromosome.
# It has genes that are 0 or 1. When creates, this is random.
class Chromosome:
    def __init__(self, bit_string_length):
        self.genes = []
        for i in range(bit_string_length):
            if random() < 0.5:
                self.genes.append(0)
            else:
                self.genes.append(1)

    def change_gene(self, index, value):
        old_gene = self.genes[index]
        self.genes[index] = value
        return old_gene

    def mutate_chromosome(self, mutation_rate):
        for i in range(len(self.genes)):
            if random() < mutation_rate:
                if self.genes[i] == 0:
                    self.genes[i] = 1
                else:
                    self.genes[i] = 0

    def __str__(self):
        return "{}".format(self.genes)

