import unittest
import population as pop
import individual as ind
import utils as ut


class TestUtilsMethods(unittest.TestCase):
    def test_crossover(self):
        # Create two individuals.
        individual1 = ind.Individual(10)
        individual2 = ind.Individual(10)
        # Set the genes of the individual 1 chromosome to 1's, and the genes of the individual 2 chromosome to 0's.
        for i in range(len(individual1.chromosome)):
            for j in range(len(individual1.chromosome[i])):
                individual1.chromosome[i][j] = 1
        for i in range(len(individual2.chromosome)):
            for j in range(len(individual2.chromosome[i])):
                individual2.chromosome[i][j] = 0
        print(individual1)
        print(individual2)

        # Check if the crossover was correct by checking if individual 2 has any 1's in the chromosome.
        individual1, individual2 = ut.crossover(individual1, individual2, 0.1)
        print("After crossover:")
        print(individual1)
        print(individual2)
        true = False
        for i in range(len(individual2.chromosome)):
            for j in range(len(individual2.chromosome[i])):
                if individual2.chromosome[i][j] == 1:
                    true = True
        self.assertEqual(true, True)

        # Check if amount of genes is correct after crossover.
        amount_of_genes = 0
        for i in range(len(individual1.chromosome)):
            for j in range(len(individual1.chromosome[i])):
                amount_of_genes += 1
        self.assertEqual(amount_of_genes, 10)

    def test_mutate(self):
        # Create one individual.
        individual1 = ind.Individual(10)

        # Set the genes of the individual 1 chromosome to 1's.
        for i in range(len(individual1.chromosome)):
            for j in range(len(individual1.chromosome[i])):
                individual1.chromosome[i][j] = 1
        print(individual1)

        # Check if the mutation was correct by checking if individual 1 has any 0's in the chromosome.
        ut.mutate(individual1, 1.0)
        print("After mutation:")
        print(individual1)
        true = False
        for i in range(len(individual1.chromosome)):
            for j in range(len(individual1.chromosome[i])):
                if individual1.chromosome[i][j] == 0:
                    true = True
        self.assertEqual(true, True)

    def test_standard_deviation(self):
        # Create a population.
        population = pop.Population(10, 10)
        # Set every second individual fitness to 1.
        # Set every other individual fitness to 0.
        for i in range(len(population.population)):
            if i % 2 == 0:
                population.population[i].fitness = 1
            else:
                population.population[i].fitness = 0

        # Calculate the standard deviation.
        standard_deviation = ut.standard_deviation(population.population)
        # Check if the standard deviation is correct.
        self.assertEqual(standard_deviation, 0.5)

















if __name__ == '__main__':
    unittest.main()
