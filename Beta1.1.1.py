import tkinter as tk
import random
import tkinter.font as tkFont

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
            self.dna += [random.choice(self.dna)]
        elif mutation_type == 'deletion' and len(self.dna) > 1:
            self.dna.pop(random.randint(0, len(self.dna) - 1))

    def age(self):
        self.lifespan -= 1

class Environment:
    def __init__(self, resources, predators):
        self.resources = resources
        self.predators = predators
        self.temperature = 25

    def cycle_day(self):
        self.temperature += random.choice([-1, 1])
        self.resources['food'] = max(0, self.resources['food'] + random.choice([-10, 10]))
        self.predators['number'] = max(0, self.predators['number'] + random.choice([-1, 1]))

def create_population(size, dna_length):
    return [Organism([random.randint(0, 1) for _ in range(dna_length)]) for _ in range(size)]

def run_simulation(generations, population_size, dna_length, output_text):
    environment = Environment({'food': 100}, {'number': 5})
    population = create_population(population_size, dna_length)
    for generation in range(generations):
        output_text.insert(tk.END, f"Generation {generation + 1}\n")
        environment.cycle_day()
        for organism in population:
            organism.calculate_fitness(environment)
            organism.age()
            output_text.insert(tk.END, f"Organism DNA: {organism.dna} Fitness: {organism.fitness} Lifespan: {organism.lifespan}\n")
        population = [org for org in population if org.lifespan > 0]
        
        # Check if the population is empty before finding the fittest organism
        if population:
            fittest = max(population, key=lambda o: o.fitness)
            output_text.insert(tk.END, f"Fittest DNA: {fittest.dna} Fitness: {fittest.fitness}\n")
        else:
            output_text.insert(tk.END, "No organisms left in the population.\n")
            break  # Exit the loop if there are no organisms left
        
        new_generation = []
        for _ in range(population_size):
            if population and random.random() < (fittest.fitness / 10):
                offspring = Organism(fittest.dna)
                offspring.mutate()
                new_generation.append(offspring)
        population = new_generation
        output_text.insert(tk.END, "\n")

# UI setup with custom fonts and colors
root = tk.Tk()
root.title("Evolites Life Simulation")

# Define a custom font
custom_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

# Add a text widget to display the simulation output
output_text = tk.Text(root, height=20, width=80, bg="#f0f0f0", fg="#333333", font=custom_font)
output_text.pack()

# Function to start the simulation and update the UI
def start_simulation():
    output_text.delete('1.0', tk.END)
    generations = 100
    population_size = 50
    dna_length = 10
    run_simulation(generations, population_size, dna_length, output_text)

# Add a start button to the UI
start_button = tk.Button(root, text="Start Simulation", command=start_simulation, font=custom_font, bg="#4CAF50", fg="white")
start_button.pack()

# Run the Tkinter event loop
root.mainloop()

# Pause at the end of the script
input("Press Enter to exit...")

