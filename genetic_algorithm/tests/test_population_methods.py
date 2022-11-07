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







if __name__ == '__main__':
    unittest.main()
