import population as pop
import matplotlib.pyplot as plt

"""
A class that is used to represent the generic algorithm.
It creates a population and evolves it by applyng the given rates.
"""

# Global variables.
GENERATIONS = 100
POPULATION_SIZE = 100
BIT_STRING_LENGTH = 100
ELITE_RATE = 0.1
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1


def plot(log, title, ylabel):
    x = range(len(log))
    plt.plot(x, log)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel(ylabel)
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
    This methods saved the best, average and std dev to their own files.
    """
    def save(self, best, average, std_dev):
        # Save name of the run to a txt file. If not empty, add a new line.
        run_name = "Generations: " + str(self.generations) + ", Population size: " + str(self.population_size) + ", Bit string length: " + str(self.bit_string_length) + ", Elite rate: " + str(self.elite_rate) + ", Crossover rate: " + str(self.crossover_rate) + ", Mutation rate: " + str(self.mutation_rate)
        with open("logs/run_names.txt", "a") as f:
            f.write(run_name)
            f.write("\n")

        # Save the best, average and std dev to their own files.
        with open("logs/best.txt", "a") as f:
            f.write(str(best))
            f.write("\n")

        with open("logs/average.txt", "a") as f:
            f.write(str(average))
            f.write("\n")


        with open("logs/std_dev.txt", "a") as f:
            f.write(str(std_dev))
            f.write("\n")





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

        plot(population.log_best_fitness, "Best fitness", "Fitness")
        plot(population.log_average_fitness, "Average fitness", "Fitness")
        plot(population.log_std_dev_fitness, "Standard deviation of fitness", "Fitness deviation")

        self.save(population.log_best_fitness, population.log_average_fitness, population.log_std_dev_fitness)


if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(GENERATIONS, POPULATION_SIZE, BIT_STRING_LENGTH, ELITE_RATE, CROSSOVER_RATE, MUTATION_RATE)
    genetic_algorithm.evolve()


