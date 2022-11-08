from random import random

def crossover(individual1, individual2, crossover_rate):
    if crossover_rate == 0:
        return individual1, individual2

    crossover_amount = int(crossover_rate * len(individual1.chromosome))

    if crossover_amount == 0:
        crossover_amount = 1

    # Find crossover_amount random crossover points without repetition.

    for crossover_times in range(crossover_amount):
        crossover_index = int(random() * len(individual1.chromosome))
        temp = individual1.chromosome[crossover_index]
        individual1.chromosome[crossover_index] = individual2.chromosome[crossover_index]
        individual2.chromosome[crossover_index] = temp

    # Return the new individual.
    return individual1, individual2


def mutate(individual, mutation_rate):
    if mutation_rate == 0:
        return individual
    mutation_amount = int(mutation_rate * len(individual.chromosome))
    if mutation_amount == 0:
        mutation_amount = 1

    # mutation_amount is how many times blocks are picked to be mutated.
    for mutation_times in range(mutation_amount):
        # Pick a random block to mutate.
        mutation_index = int(random() * len(individual.chromosome))
        # Mutate the block.
        for i in range(len(individual.chromosome[mutation_index])):
            if random() < mutation_rate:
                if individual.chromosome[mutation_index][i] == 0:
                    individual.chromosome[mutation_index][i] = 1
                else:
                    individual.chromosome[mutation_index][i] = 0
    return individual