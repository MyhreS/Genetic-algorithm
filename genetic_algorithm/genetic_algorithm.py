import population as pop
import matplotlib.pyplot as plt

"""
A class that is used to represent the generic algorithm.
It craetes a population and evolves it by applying the genetic operators.
It performes elitism, and reproduction by selection, crossover and mutation.
"""

def plot(log, title):
    x = range(len(log))
    plt.plot(x, log)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()



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
            if population.log_best_fitness[-1] == population.bit_string_length:
                break

        plot(population.log_best_fitness, "Best fitness")
        plot(population.log_average_fitness, "Average fitness")
        plot(population.log_std_dev_fitness, "Standard deviation of fitness")





if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(200, 200, 100, 0.1, 0.2, 0.2)
    genetic_algorithm.evolve()


