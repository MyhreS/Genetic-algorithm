from random import random

import individual as ind

"""
This class is used to create a population of individuals.
It contains a list of individuals.
It can perform selection, crossover, and mutation on the population.
"""
class Population:
    def __init__(self, population_size, bit_string_length):
        self.population_size = population_size
        self.bit_string_length = bit_string_length
        self.individuals = []
        for i in range(population_size):
            self.individuals.append(ind.Individual(bit_string_length))

    """
    This method is used to select the best individuals from the population.
    Sorts the population by fitness.
    """
    def sort_population(self):
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)



    It takes the number of individuals to select as a parameter.
    It returns a list of the selected individuals.
    """
    def selection(self, number_of_individuals_to_select):
        pass

    """
    This method is used to select an individual from the population.
    It returns the selected individual.
    """
    def select_single_individual(self):
        pass

    """
    This method is used to perform crossover on the population.
    It takes the crossover rate as a parameter.
    It returns the population with the crossed over individuals.
    """
    def crossover(self, crossover_rate):
        pass

    """
    This method is used to perform mutation on the population.
    It takes the mutation rate as a parameter.
    It returns the population with the mutated individuals.
    """
    def mutation(self, mutation_rate):
        pass

