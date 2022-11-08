
import population as pop

"""
A class that is used to represent the generic algorithm.
It craetes a population and evolves it by applying the genetic operators.
It performes elitism, and reproduction by selection, crossover and mutation.
"""
class GeneticAlgorithm:

    def __init__(self, generations, population_size, bit_string_length, elite_rate, selection_rate, crossover_rate, mutation_rate):
        self.generations = generations
        self.population_size = population_size
        self.bit_string_length = bit_string_length
        self.elite_amount = int(elite_rate * population_size)
        self.selection_amount = int(selection_rate * population_size)
        self.crossover_amount = int(crossover_rate * bit_string_length)
        self.mutation_rate = mutation_rate
        self.mutation_amount = 2
        self.population = pop.Population(population_size, bit_string_length)

    """
    A method that evolves the population by selecting, crossover and mutation.
    """
    def evolve(self):
        for i in range(self.generations):
            self.population.evolve(self.elite_amount, self.crossover_amount, self.mutation_amount, self.mutation_rate)




if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm(30, 100, 50, 0.1, 0.3, 0.4, 0.8)
    genetic_algorithm.evolve()


