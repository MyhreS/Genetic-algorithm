from random import random
import individual as ind
import copy
import utils as ut

"""
This class is used to create a population of population.
It contains a list of population, the pupulation size, bit string bit_string_length and the population fitness score.

"""
class Population:
    def __init__(self, population_size, bit_string_length):
        self.population_size = population_size
        self.bit_string_length = bit_string_length
        self.population = []
        for i in range(population_size):
            self.population.append(ind.Individual(bit_string_length))
        self.population_fitness = 0
        self.calculate_fitness()
        self.sort_population()

    """
    This method is used to calculate each individual fitness and the populations fitness.
    """
    def calculate_fitness(self):
        for i in range(self.population_size):
            self.population[i].calculate_fitness()

        self.population_fitness = 0
        for i in range(self.population_size):
            self.population_fitness += self.population[i].fitness


    """
    Sorts the population by fitness.
    """
    def sort_population(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)


    """
    This method is used to get the first (after sorting, fittest) population in the population.
    It takes elite amount as a parameter, which is the number of elite population to return.
    """
    def select_elite(self, elite_amount):
        if elite_amount > self.population_size:
            raise Exception("elite_amount is larger than population_size")
        return self.population[:elite_amount]


    """
    This method is used to select the population from the population to reproduce.
    It takes the number of population to select as a parameter.
    It returns a list of the selected population.
    An population chance of being selected is proportional to its fitness.
    It is done by roulette wheel selection.
    """
    def selection(self, number_of_individuals_to_select):
        # Check that the number of population to select is not larger than the population size.
        if number_of_individuals_to_select > self.population_size:
            raise Exception("number_of_individuals_to_select is larger than population_size")

        # Make number_of_individuals_to_select even.
        if number_of_individuals_to_select % 2 != 0:
            number_of_individuals_to_select += 1

        # Create a list of the selected population.
        selected_individuals = []
        self.calculate_fitness()

        # Select the population.
        while len(selected_individuals) < number_of_individuals_to_select:
            # Select a random individual.
            random_individual = self.population[int(random() * self.population_size)]

            # Calculate the probability of selecting the individual.
            if random_individual.fitness == 0:
                probability = 0
            else:
                probability = random_individual.fitness / self.population_fitness

            # Select or not select based on the probability.
            if random() < probability:
                selected_individuals.append(random_individual)

        # Return the list of selected population.
        return selected_individuals


    """
    Method used to evolve the population one generation.
    It takes the elite amount, reproduction amount, crossover rate and mutation rate as parameters.
    """
    def evolve(self, elite_amount, selection_amount, crossover_amount, mutation_amount, mutation_rate):

        # Select the elite population.
        elite = self.select_elite(elite_amount)
        # Select the population to reproduce.
        select_fittest = self.population[0]
        select_second_fittest = self.population[1]

        # Empty the old population and add the elite population.
        self.population = []
        for individual in elite:
            self.population.append(copy.deepcopy(individual))

        # Create offspring from the selected population.
        while len(self.population) < self.population_size:
            # Crossover two random parents from selected population.
            parent1 = copy.deepcopy(select_fittest)
            parent2 = copy.deepcopy(select_second_fittest)
            offspring1, offspring2 = ut.crossover(parent1, parent2, crossover_amount)

            # Mutate the offspring.
            offspring1 = ut.mutate(offspring1, mutation_amount, mutation_rate)
            offspring2 = ut.mutate(offspring2, mutation_amount, mutation_rate)

            offspring1.calculate_fitness()
            offspring2.calculate_fitness()

            if offspring1.fitness > offspring2.fitness:
                self.population.append(offspring1)
            else:
                self.population.append(offspring2)

        self.calculate_fitness()
        self.sort_population()

        print(self.population[0])


    """
    This method is used to print the population.
    """
    def __str__(self):
        string = ""
        for i in range(self.population_size):
            string += str(self.population[i]) + "\n"
        return string













