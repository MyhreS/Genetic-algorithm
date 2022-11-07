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

    def __str__(self):
        return "{}".format(self.genes)

