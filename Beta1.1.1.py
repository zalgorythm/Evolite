import tkinter as tk
import random
import tkinter.font as tkFont
from tkinter import ttk


class Organism:
    """
    Represents an organism with a DNA sequence and lifespan.
    """
    def __init__(self, dna_sequence: list, lifespan: int = 100) -> None:
        """
        Initializes an Organism instance.

        Args:
            dna_sequence (list): The DNA sequence of the organism.
            lifespan (int, optional): The lifespan of the organism. Defaults to 100.
        """
        self.dna = dna_sequence.copy()
        self.fitness = 0
        self.lifespan = lifespan

    def calculate_fitness(self, environment):
        """
        Calculates the fitness of the organism based on its DNA sequence and the environment.

        Args:
            environment: The environment object.
        """
        self.fitness = sum(self.dna)
        if environment.temperature > 30:
            self.fitness += 1

    def mutate(self):
        """
        Mutates the DNA sequence of the organism by performing a random mutation.
        """
        mutation_type = random.choice(['point', 'duplication', 'deletion'])
        if mutation_type == 'point':
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + (not self.dna[index],) + self.dna[index+1:]
        elif mutation_type == 'duplication' and len(self.dna) < 20:
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + (self.dna[index], self.dna[index]) + self.dna[index+1:]
        elif mutation_type == 'deletion' and len(self.dna) > 1:
            index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:index] + self.dna[index+1:]

    def age(self):
        """
        Decreases the lifespan of the organism by 1.
        """
        self.lifespan -= 1


class Environment:
    """
    Represents the environment with resources and predators.
    """
    def __init__(self, resources, predators):
        """
        Initializes an Environment instance.

        Args:
            resources (dict): The resources in the environment.
            predators (dict): The predators in the environment.
        """
        self.resources = resources
        self.predators = predators
        self.temperature = 25

    def cycle_day(self):
        """
        Cycles the day in the environment by updating the temperature and resources/predators.
        """
        self.temperature += random.choice([-1, 1])
        self.resources['food'] = max(0, self.resources['food'] + random.choice([-10, 10]))
        self.predators['number'] = max(0, self.predators['number'] + random.choice([-1, 1]))


def create_population(size, dna_length):
    """
    Creates a population of Organism instances with random DNA sequences.

    Args:
        size (int): The size of the population.
        dna_length (int): The length of the DNA sequence.

    Returns:
        list: The population of Organism instances.
    """
    return [Organism([random.randint(0, 1) for _ in range(dna_length)]) for _ in range(size)]


def run_simulation(generations, population_size, dna_length, output_text):
    """
    Runs a simulation for a given number of generations.

    Args:
        generations (int): The number of generations to run the simulation for.
        population_size (int): The size of the population.
        dna_length (int): The length of the DNA sequence.
        output_text (tk.Text): The text widget to display the simulation output.
    """
    environment = Environment({'food': 100}, {'number': 5})
    population = create_population(population_size, dna_length)
    previous_generation = []
    for generation in range(generations):
        environment.cycle_day()
        for organism in population:
            organism.calculate_fitness(environment)
            organism.age()
        population = [org for org in population if org.lifespan > 0]
        if population:
            fittest = max(population, key=lambda o: o.fitness)
        else:
            break
        new_generation = []
        for _ in range(population_size):
            if random.random() < (fittest.fitness / 10):
                offspring = Organism(fittest.dna)
                offspring.mutate()
                new_generation.append(offspring)
        previous_generation.append(population)
        population = new_generation
        output_text.insert(tk.END, f"Generation {generation+1}:\nFittest Organism: {fittest.fitness}\n\n")


def start_simulation(output_text, generations_slider, population_size_slider, dna_length_slider):
    """
    Starts the simulation by clearing the output text widget and running the simulation.

    Args:
        output_text (tk.Text): The text widget to display the simulation output.
        generations_slider (ttk.Scale): The slider for the number of generations.
        population_size_slider (ttk.Scale): The slider for the population size.
        dna_length_slider (ttk.Scale): The slider for the DNA length.
    """
    output_text.delete('1.0', tk.END)
    generations = int(generations_slider.get())
    population_size = int(population_size_slider.get())
    dna_length = int(dna_length_slider.get())
    run_simulation(generations, population_size, dna_length, output_text)


# UI setup with custom fonts and colors
root = tk.Tk()
root.title("Evolites Life Simulation")
root.configure(bg="#f0f0f0")

custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

instructions_label = tk.Label(root, text="Instructions:\n- Adjust the sliders to change the simulation parameters.\n- Click the 'Start Simulation' button to run the simulation.", font=custom_font, bg="#f0f0f0", fg="#333333")
instructions_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

generations_label = tk.Label(root, text="Generations:", font=custom_font, bg="#f0f0f0", fg="#333333")
generations_label.grid(row=1, column=0, padx=10, pady=10)

generations_slider = ttk.Scale(root, from_=1, to=1000, orient=tk.HORIZONTAL, command=lambda x: output_text.delete('1.0', tk.END))
generations_slider.grid(row=1, column=1, padx=10, pady=10)

population_size_label = tk.Label(root, text="Population Size:", font=custom_font, bg="#f0f0f0", fg="#333333")
population_size_label.grid(row=2, column=0, padx=10, pady=10)

population_size_slider = ttk.Scale(root, from_=1, to=1000, orient=tk.HORIZONTAL, command=lambda x: output_text.delete('1.0', tk.END))
population_size_slider

