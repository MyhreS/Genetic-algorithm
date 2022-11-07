import unittest
import individual as ind

class TestIndividualMethods(unittest.TestCase):
    def test_genes_when_create_individual(self):
        individual = ind.Individual(10)

        fitness = 0
        for gene in individual.genes:
            if gene == 1:
                fitness += 1

        self.assertEqual(individual.fitness, fitness)

    def test_calculate_fitness(self):
        individual = ind.Individual(10)
        fitness = 0
        for gene in individual.genes:
            if gene == 1:
                fitness += 1

        self.assertEqual(individual.calculate_fitness(), fitness)

    def test_copy_individual(self):
        individual = ind.Individual(10)
        new_individual = individual.__copy__()

        self.assertEqual(individual.genes, new_individual.genes)
        self.assertEqual(individual.fitness, new_individual.fitness)





if __name__ == '__main__':
    unittest.main()
