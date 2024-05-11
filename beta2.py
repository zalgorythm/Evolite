    def mutate(self) -> 'Organism':
        """
        Mutates the DNA sequence of the organism by performing a random mutation.

        This function randomly selects a mutation type from ['point', 'duplication', 'deletion']
        and performs the corresponding mutation on the DNA sequence.

        Returns:
            Organism: The mutated organism.
        """
        mutation_types = ['point', 'duplication', 'deletion']
        mutation_type = random.choice(mutation_types)

        if mutation_type == 'point':
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + (not self.dna[index],) + self.dna[index+1:]
        elif mutation_type == 'duplication' and len(self.dna) < 20:
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + (self.dna[index], self.dna[index]) + self.dna[index+1:]
        elif mutation_type == 'deletion' and len(self.dna) > 1:
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + self.dna[index+1:]

        return self


def next_generation(population: list) -> list:
    """
    Generates the next generation of organisms from the current population.

    Args:
        population (list): The current population of organisms.

    Returns:
        list: The next generation of organisms.
    """
    fittest = max(population, key=lambda organism: organism.fitness)
    return [fittest.reproduce(random.choice(population)).mutate() for _ in range(len(population))]


