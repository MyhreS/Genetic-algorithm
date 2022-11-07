import unittest
import chromosome as ch

class TestChromosomeMethods(unittest.TestCase):
    def test_create_chromosome(self):
        chromosome = ch.Chromosome(10)
        self.assertEqual(len(chromosome.genes), 10)


if __name__ == '__main__':
    unittest.main()
