import population as pop

"""
A class that is used to represent the generic algorithm.
It craetes a population and evolves it by applying the genetic operators.
It performes elitism, and reproduction by selection, crossover and mutation.
"""

class GeneticAlgorithm:

    def __init__(self, generations, population_size, bit_string_length, elite_rate, crossover_rate, mutation_rate):
        self.generations = generations
        self.population_size = population_size
        self.bit_string_length = bit_string_length
        self.elite_rate = elite_rate
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate


    """
    A method that evolves the population by selecting, crossover and mutation.
    """
    def evolve(self):
        # Create the population.
        population = pop.Population(self.population_size, self.bit_string_length)

        for i in range(self.generations):
            population.evolve(self.elite_rate, self.crossover_rate, self.mutation_rate)

            if population.log_best_fitness[-1] == population.population_size:
                break
        # Print the best results log.
        for fitness in population.log_best_fitness:
            print(fitness)




if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(20, 20, 20, 0.1, 0.2, 0.2)
    genetic_algorithm.evolve()


