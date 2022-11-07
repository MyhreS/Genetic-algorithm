import unittest
import individual as ind

class TestIndividualMethods(unittest.TestCase):
    def test_genes_when_create_individual(self):
        individual = ind.Individual(10)
        self.assertEqual(len(individual.genes), 10)

    def test_fitness_score_when_create_individual(self):
        individual = ind.Individual(10)
        individuals_fitness = 0
        for gene in individual.genes:
            if gene == 1:
                individuals_fitness += 1
        # The fitness score should be the same as the number of 1's in the genes.
        self.assertEqual(individual.fitness, individuals_fitness)

    def test_genes_when_change_individual_genes(self):
        individual = ind.Individual(2)
        individual.genes = [0, 1]

        # Change genes from 0, 1 to 1, 1
        return_gene = individual.change_gene(0, 1)

        # If the gene was 0, it should now be 1.
        self.assertEqual(individual.genes, [1, 1])
        # The return value should be 0 (its old gene value).
        self.assertEqual(return_gene, 0)

    def test_mutate_individual_genes(self):
        individual = ind.Individual(2)
        individual.genes = [0, 1]
        individual.mutate_chromosome(1) # 100% chance of mutation

        # The genes should be the oposite of what they were. That is 1, 0.
        self.assertEqual(individual.genes, [1, 0])


if __name__ == '__main__':
    unittest.main()
