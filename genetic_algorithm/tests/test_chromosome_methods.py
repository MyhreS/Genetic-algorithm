import unittest
import individual as ind

class TestChromosomeMethods(unittest.TestCase):
    def test_create_individual(self):
        chromosome = ind.Individual(10)
        self.assertEqual(len(chromosome.genes), 10)

    def test_change_individual(self):
        chromosome = ind.Individual(2)
        copy_of_chromosome_genes = chromosome.genes.copy()

        if chromosome.genes[0] == 0:
            new_gene_value = 1
        else:
            new_gene_value = 0
        gene_return = chromosome.change_gene(0, new_gene_value)

        # If the gene was 0, it should now be 1.
        self.assertEqual(chromosome.genes[0], new_gene_value)
        # The other gene should not have changed.
        self.assertEqual(chromosome.genes[1], copy_of_chromosome_genes[1])
        # The return value should be the old gene value.
        self.assertEqual(gene_return, copy_of_chromosome_genes[0])

    def test_mutate_individual(self):
        chromosome = ind.Individual(2)
        copy_of_chromosome_genes = chromosome.genes.copy()
        chromosome.mutate_chromosome(1) # 100% chance of mutation

        # The genes should be different.
        self.assertNotEqual(chromosome.genes, copy_of_chromosome_genes)


if __name__ == '__main__':
    unittest.main()
