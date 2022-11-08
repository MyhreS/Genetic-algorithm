import unittest
import individual as ind

class TestIndividualMethods(unittest.TestCase):
    def test_genes_when_create_individual(self):
        individual = ind.Individual(20)

        amount_of_blocks = 0
        amount_of_genes = 0
        for block in individual.chromosome:
            amount_of_blocks += 1
            amount_of_genes += len(block)
        self.assertEqual(amount_of_genes, 20)


    def test_calculate_fitness(self):
        individual = ind.Individual(10)
        fitness = 0
        for block in individual.chromosome:
            for gene in block:
                if gene == 1:
                    fitness += 1
        self.assertEqual(individual.calculate_fitness(), fitness)

    def test_copy_individual(self):
        individual = ind.Individual(10)
        new_individual = individual.__copy__()

        self.assertEqual(individual.chromosome, new_individual.chromosome)
        self.assertEqual(individual.fitness, new_individual.fitness)





if __name__ == '__main__':
    unittest.main()
