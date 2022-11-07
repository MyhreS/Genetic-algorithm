from random import random

import individual as ind

"""
This class is used to create a population of individuals.
It contains a list of individuals, the pupulation size, bit string length and the population fitness score.
"""
class Population:
    def __init__(self, population_size, bit_string_length):
        self.population_size = population_size
        self.bit_string_length = bit_string_length
        self.individuals = []
        for i in range(population_size):
            self.individuals.append(ind.Individual(bit_string_length))
        self.population_fitness_score = self.calculate_pupulation_fitness_score()


    """
    This method is used to calculate the pupulation fitness score.
    """
    def calculate_pupulation_fitness_score(self):
        self.population_fitness_score = 0
        for i in range(self.population_size):
            self.population_fitness_score += self.individuals[i].fitness
        return self.population_fitness_score

    """
    Sorts the population by fitness.
    """
    def sort_population(self):
        self.individuals.sort(key=lambda x: x.fitness, reverse=True)


    """
    This method is used to get the first (after sorting, fittest) individuals in the population.
    It takes elite amount as a parameter, which is the number of elite individuals to return.
    """
    def select_elite(self, elite_amount):
        self.sort_population()
        if elite_amount > self.population_size:
            raise Exception("elite_amount is larger than population_size")
        return self.individuals[:elite_amount]


    """
    This method is used to select the individuals from the population to reproduce.
    It takes the number of individuals to select as a parameter.
    It returns a list of the selected individuals.
    An individuals chance of being selected is proportional to its fitness.
    It is done by roulette wheel selection.
    """
    def selection(self, number_of_individuals_to_select):
        # Check that the number of individuals to select is not larger than the population size.
        if number_of_individuals_to_select > self.population_size:
            raise Exception("number_of_individuals_to_select is larger than population_size")

        # Calculate the total fitness score of the population.
        total_fitness_score = self.calculate_pupulation_fitness_score()

        # Create a list of the selected individuals.
        selected_individuals = []

        # Select the individuals.
        while len(selected_individuals) < number_of_individuals_to_select:
            # Select a random individual.
            random_individual = self.individuals[int(random() * self.population_size)]

            # Calculate the probability of selecting the individual.
            probability = random_individual.fitness / total_fitness_score

            # Select or not select based on the probability.
            if random() < probability:
                selected_individuals.append(random_individual)

        # Return the list of selected individuals.
        return selected_individuals

