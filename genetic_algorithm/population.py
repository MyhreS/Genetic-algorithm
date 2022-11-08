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
    Method used to evolve the population one generation.
    It takes the elite amount, reproduction amount, crossover rate and mutation rate as parameters.
    """
    def evolve(self, elite_amount, crossover_amount, mutation_amount, mutation_rate):
        # Select the elite population.
        elite = self.select_elite(elite_amount)

        # Select parents to reproduce.
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
            # Calculate the fitness of the offsprings
            offspring1.calculate_fitness()
            offspring2.calculate_fitness()
            # Add the fittest offspring to the population.
            if offspring1.fitness > offspring2.fitness:
                self.population.append(offspring1)
            else:
                self.population.append(offspring2)

        # Calculate the populations fitness and sort the population.
        self.calculate_fitness()
        self.sort_population()

        # Print the fittest individual in the population.
        print(self.population[0])


    """
    This method is used to print the population.
    """
    def __str__(self):
        string = ""
        for i in range(self.population_size):
            string += str(self.population[i]) + "\n"
        return string













