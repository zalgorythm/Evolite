import random
import tkinter as tk
from typing import List, Dict, Union


class Organism:
    """
    Represents an organism with a DNA sequence, traits derived from DNA, and properties related to its fitness and lifespan.
    """

    def __init__(self, dna: List[int], lifespan: int = 100) -> None:
        """
        Initializes an Organism instance with a DNA sequence and a lifespan.

        Args:
            dna (List[int]): The DNA sequence of the organism.
            lifespan (int, optional): The lifespan of the organism. Defaults to 100.
        """
        self.dna = dna.copy()
        self.fitness = 0
        self.lifespan = lifespan
        self.traits = self.calculate_traits(self.dna)  # Calculate traits based on DNA

    def calculate_traits(self, dna: List[int]) -> Dict[str, float]:
        """
        Calculates the traits of the organism based on its DNA sequence.

        Args:
            dna (List[int]): The DNA sequence of the organism.

        Returns:
            Dict[str, float]: A dictionary containing the calculated traits (e.g., heat_tolerance, camouflage)
        """
        # Calculate heat tolerance based on average gene value
        heat_tolerance = sum(dna) / len(dna)
        # Calculate camouflage based on percentage of ones in the DNA sequence
        camouflage = len([gene for gene in dna if gene == 1]) / len(dna)
        return {"heat_tolerance": heat_tolerance, "camouflage": camouflage}

    def mutate(self) -> None:
        """
        Mutates the DNA sequence of the organism by performing a random mutation.
        """
        # Choose a mutation type
        mutation_type = random.choice(['point', 'duplication', 'deletion'])
        if mutation_type == 'point':
            # Flip a random gene
            index = random.randint(0, len(self.dna) - 1)
            self.dna[index] = 1 - self.dna[index]
        elif mutation_type == 'duplication' and len(self.dna) < 20:
            # Insert a copy of a random gene
            index = random.randint(0, len(self.dna) - 1)
            self.dna.insert(index, self.dna[index])
        elif mutation_type == 'deletion' and len(self.dna) > 1:
            # Remove a random gene
            index = random.randint(0, len(self.dna) - 1)
            del self.dna[index]

    def reproduce(self, parent: 'Organism') -> 'Organism':
        """
        Reproduces the organism with another parent organism to create a new offspring.

        Args:
            parent (Organism): The parent organism to reproduce with.

        Returns:
            Organism: The offspring organism.
        """
        # Create a new DNA sequence by randomly choosing between this organism's gene or the parent's gene
        child_dna = [random.choice([gene, parent.dna[i]]) for i, gene in enumerate(self.dna)]
        return Organism(child_dna)

    def calculate_fitness(self, environment: 'Environment') -> None:
        """
        Calculates the fitness of the organism based on its DNA-derived traits and the environment.

        Args:
            environment (Environment): The environment in which the organism is living.
        """
        self.fitness = sum(self.traits.values())  # Base fitness on combined traits
        # Adjust fitness based on environment and traits
        self.fitness += self.traits["heat_tolerance"] * (environment.temperature - 25)
        self.fitness += self.traits["camouflage"] * (1 - environment.predators["number"] / 10)

    def decrease_lifespan(self) -> None:
        """
        Decreases the lifespan of the organism by 1.
        """
        if self.lifespan > 0:
            self.lifespan -= 1


class Environment:
    """
    Represents an environment with resources, predators, and temperature.
    """

    def __init__(self, resources: Dict[str, int], predators: Dict[str, int], temperature: int = 25) -> None:
        """
        Initializes an Environment instance with resources and predators.

        Args:
            resources (Dict[str, int]): A dictionary containing the available resources and their quantities.
            predators (Dict[str, int]): A dictionary containing the types of predators and their numbers.
            temperature (int, optional): The temperature of the environment. Defaults to 25.
        """
        self.resources = resources
        self.predators = predators
        self.temperature = temperature


