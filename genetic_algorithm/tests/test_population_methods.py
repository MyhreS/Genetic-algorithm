import unittest
import population as pop
import individual as ind

class TestPopulationMethods(unittest.TestCase):
    def test_create_population(self):
        population = pop.Population(10, 10)

        # Check that the population_size is correct. That is, 10.
        self.assertEqual(population.population_size, 10)
        # Check that the length of the bit string is correct. That is, 10.
        self.assertEqual(population.bit_string_length, 10)
        # Check that amount of individuals is correct. That is, 10.
        self.assertEqual(len(population.individuals), 10)

        a_individual = ind.Individual(2)
        # Check that the type of the individuals in the population list is correct. That is, type: Individual.
        self.assertEqual(type(population.individuals[0]), type(a_individual))

    def test_sort_population(self):
        population = pop.Population(2, 2)
        population.individuals[0].fitness = 1 # Set the fitness of the first individual to 1.
        population.individuals[1].fitness = 2 # Set the fitness of the second individual to 2.
        population.sort_population() # Sort the population by fitness.

        # Check that the population is sorted by fitness. That is, the individual with the highest fitness is first, which is = 2.
        self.assertEqual(population.individuals[0].fitness, 2)

    def test_select_elite(self):
        population = pop.Population(2, 2)
        first = population.select_elite(1) # Select the first individual.

        self.assertEqual(len(first), 1) # Check that the length of the list is correct. That is, 1.





if __name__ == '__main__':
    unittest.main()
