import unittest
import population as pop
import individual as ind

class TestPopulationMethods(unittest.TestCase):
    def test_create_population(self):
        population = pop.Population(10, 10)

        # Check that the population_size is correct. That is, 10.
        self.assertEqual(population.population_size, 10)
        # Check that the bit_string_length of the bit string is correct. That is, 10.
        self.assertEqual(population.bit_string_length, 10)
        # Check that amount of population is correct. That is, 10.
        self.assertEqual(len(population.population), 10)
        # Check if the population fitness is correct.
        total_fitness = 0
        for i in range(10):
            total_fitness += population.population[i].fitness
        self.assertEqual(population.population_fitness, total_fitness)
        # Check that the type of the population in the population list is correct. That is, type: Individual.
        a_individual = ind.Individual(10)
        self.assertEqual(type(population.population[0]), type(a_individual))

    def test_calculate_fitness(self):
        population = pop.Population(2, 10)

        # Change individuals in the populations to only have 1's in the chromosome.
        # The fitness should be 10 for each individual.
        # The population fitness should be 10 + 10 = 20.
        for individual in population.population:
            for i in range(len(individual.chromosome)):
                for j in range(len(individual.chromosome[i])):
                    individual.chromosome[i][j] = 1

        population.calculate_fitness()
        # Check that the fitness of the individuals are correct.
        self.assertEqual(population.population[0].fitness, 10)
        self.assertEqual(population.population[1].fitness, 10)
        # Check that the population fitness is correct.
        self.assertEqual(population.population_fitness, 20)




    def test_sort_population(self):
        population = pop.Population(2, 10)
        population.population[0].fitness = 1 # Set the fitness of the first individual to 1.
        population.population[1].fitness = 2 # Set the fitness of the second individual to 2.
        population.sort_population() # Sort the population by fitness.

        # Check that the population is sorted by fitness. That is, the individual with the highest fitness is first, which is = 2.
        self.assertEqual(population.population[0].fitness, 2)

    def test_select_elite(self):
        population = pop.Population(2, 10)
        population.population[0].fitness = 1
        population.population[1].fitness = 2
        population.sort_population()

        elites = population.select_elite(1) # Select the first individual.

        self.assertEqual(len(elites), 1) # Check that the bit_string_length of the list is correct. That is, 1.
        self.assertEqual(elites[0].fitness, 2) # Check that the individual in the list is correct. That is, the individual with the highest fitness.

    def test_evolve(self):
        population = pop.Population(100, 100)
        for i in range(100):
            population.evolve(1, 2, 1, 1, 0.2)

        # Check that the population size is correct.
        self.assertEqual(len(population.population), 100)




















if __name__ == '__main__':
    unittest.main()
