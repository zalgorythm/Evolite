import tkinter as tk
import random
import tkinter.font as tkFont
from tkinter import Scale, ttk

# Define the root window
root = tk.Tk()

# Define the custom font
custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

# Create the label for the number of generations
generations_label = tk.Label(root, text="Number of Generations:", font=custom_font, bg="lightgreen", fg="darkgreen")
generations_label.pack()

# Create the Entry widget for population size
population_size_entry = tk.Entry(root, font=custom_font)
population_size_entry.pack()

# Create the Entry widget for DNA length
dna_length_entry = tk.Entry(root, font=custom_font)
dna_length_entry.pack()

# Define the function to start the simulation
def start_simulation():
    output_text.delete('1.0', tk.END)
    try:
        generations = int(generations_entry.get())
        population_size = int(population_size_entry.get())
        dna_length = int(dna_length_entry.get())
        run_simulation(generations, population_size, dna_length, output_text)
    except ValueError:
        output_text.insert(tk.END, "Please enter valid numbers for generations, population size, and DNA length.\n")

# Create the start button
start_button = tk.Button(root, text="Start Simulation", command=start_simulation, font=custom_font, bg="#4CAF50", fg="white")
start_button.pack()

# Create the label for the number of generations
generations_label = tk.Label(root, text="Number of Generations:", font=custom_font, bg="lightgreen", fg="darkgreen")
generations_label.pack()

# Create the Entry widget for population size
population_size_entry = tk.Entry(root, font=custom_font)
population_size_entry.pack()

# Create the Entry widget for DNA length
dna_length_entry = tk.Entry(root, font=custom_font)
dna_length_entry.pack()

# Define the function to run the simulation
def run_simulation(generations, population_size, dna_length, output_text):
    # Your simulation code here
    pass

# Run the main loop
root.mainloop()

# Define the function to create a population
def create_population(size, dna_length):
    return [Organism([random.randint(0, 1) for _ in range(dna_length)]) for _ in range(size)]

# Define the Organism class
class Organism:
    def __init__(self, dna, lifespan=100):
        self.dna = dna
        self.fitness = 0
        self.lifespan = lifespan

    def calculate_fitness(self, environment):
        self.fitness = sum(self.dna)
        if environment.temperature > 30:
            self.fitness += 1

    def mutate(self):
        mutation_type = random.choice(['point', 'duplication', 'deletion'])
        if mutation_type == 'point':
            gene_index = random.randint(0, len(self.dna) - 1)
            self.dna[gene_index] = self.dna[gene_index] ^ 1
        elif mutation_type == 'duplication' and len(self.dna) < 20:
            gene_index = random.randint(0, len(self.dna))
            self.dna = self.dna[:gene_index] + self.dna[gene_index:]
        elif mutation_type == 'deletion' and len(self.dna) > 1:
            gene_index = random.randint(0, len(self.dna) - 1)
            self.dna = self.dna[:gene_index] + self.dna[gene_index + 1:]