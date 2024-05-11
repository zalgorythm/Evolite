<<<<<<<<<<<<<<  ✨ Codeium Command 🌟 >>>>>>>>>>>>>>>>
import random
import tkinter as tk
from typing import List, Dict, Union


class Organism:
    """
    Represents an organism with a DNA sequence and properties related to its fitness and lifespan.
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
        Calculates the fitness of the organism based on its DNA sequence and the environment.

        Args:
            environment (Environment): The environment in which the organism is living.
        """
        self.fitness = sum(self.dna)
        if environment and environment.temperature > 30:
            self.fitness += 1

    def decrease_lifespan(self) -> None:
        """
        Decreases the lifespan of the organism by 1.
        """
        if self.lifespan > 0:
            self.lifespan -= 1


class Environment:
    """
    Represents an environment with resources and predators.
    """

    def __init__(self, resources: Dict[str, int], predators: Dict[str, int], temperature: int = 25) -> None:
        """
        Initializes an Environment instance with resources and predators.

        Args:
            resources (Dict[str, int]): The resources available in the environment.
            predators (Dict[str, int]): The predators present in the environment.
            temperature (int, optional): The temperature of the environment. Defaults to 25.
        """
        self.resources = resources
        self.predators = predators
        self.temperature = temperature

    def cycle_day(self) -> None:
        """
        Cycles a day in the environment, updating the resources and predators.
        """
        if self:
            self.temperature += random.choice([-1, 1])
            self.resources['food'] = max(0, self.resources['food'] + random.randint(-10, 10))
            self.predators['number'] = max(0, self.predators['number'] + random.choice([-1, 1]))


def generate_population(population_size: int, dna_length: int) -> List[Organism]:
    """
    Generates a population of organisms with random DNA sequences.

    Args:
        population_size (int): The number of organisms in the population.
        dna_length (int): The length of the DNA sequence of each organism.

    Returns:
        List[Organism]: The generated population of organisms.
    """
    return [Organism([random.choice([0, 1]) for _ in range(dna_length)])
            for _ in range(population_size)]


def simulate(
    num_generations: int,  # number of generations to run the simulation for
    population_size: int,  # size of the population
    dna_length: int,  # length of the DNA sequence
    output_text: tk.Text  # text widget to display the simulation output
) -> None:
    """
    Runs a simulation for a given number of generations.

    Args:
        num_generations (int): The number of generations to run the simulation for.
        population_size (int): The size of the population.
        dna_length (int): The length of the DNA sequence.
        output_text (tk.Text): The text widget to display the simulation output.

    Returns:
        None
    """
    environment = Environment({'food': 100}, {'number': 5})
    population = generate_population(population_size, dna_length)
    for generation in range(num_generations):
        previous_generation = population.copy()
        for organism in population:
            organism.calculate_fitness(environment)
            organism.decrease_lifespan()
        population = next_generation(previous_generation)
        display_population(population, output_text)
        environment.cycle_day()


def next_generation(previous_generation: List[Organism]) -> List[Organism]:
    """
    Generates the next generation of organisms based on the previous generation.

    Args:
        previous_generation (List[Organism]): The previous generation of organisms.

    Returns:
        List[Organism]: The next generation of organisms.
    """
    fittest = max(previous_generation, key=lambda organism: organism.fitness)
    new_generation = [fittest.reproduce(random.choice(previous_generation)).mutate() for _ in range(len(previous_generation))]
    return new_generation


def display_population(population: List[Organism], output_text: tk.Text) -> None:
    """
    Displays the population of organisms in the given text widget.

    Args:
        population (List[Organism]): The population of organisms to display.
        output_text (tk.Text): The text widget to display the population.
    """
    output_text.delete("1.0", tk.END)
    for organism in population:
        if organism:
            output_text.insert(tk.END, f"Organism DNA: {organism.dna} Fitness: {organism.fitness} Lifespan: {organism.lifespan}\n")
    output_text.insert(tk.END, "\n")


def start_simulation() -> None:
    """
    Starts the simulation by creating a GUI window and starting the simulation.
    """
    num_generations = 100
    pop_size = 50
    dna_len = 10

    root = tk.Tk()
    root.title("Evolution Simulation")
    output_text = tk.Text(root)
    output_text.pack()
    start_button = tk.Button(root, text="Start", command=lambda: simulate(num_generations, pop_size, dna_len, output_text))
    start_button.pack()
    root.mainloop()


start_simulation()



<<<<<<<  09936a9c-3231-406c-88ae-1029865245af  >>>>>>>