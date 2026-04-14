import numpy as np
import matplotlib.pyplot as plt
import time

# Parameters
size = 100               # grid size 100x100
beta = 0.3               # infection probability per contact
gamma = 0.05             # recovery probability
T = 100                  # number of time steps

# Initialize grid: 0 = susceptible, 1 = infected, 2 = recovered
population = np.zeros((size, size), dtype=int)

# Randomly select one initial infected individual
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# Prepare figure
plt.figure(figsize=(6, 4), dpi=150)

# Neighbour offsets (8 directions)
neighbors = [(-1,-1), (-1,0), (-1,1),
             (0,-1),          (0,1),
             (1,-1),  (1,0),  (1,1)]

# Time loop
for t in range(T):
    # Copy current state for simultaneous updates
    new_pop = population.copy()
    
    # Find all infected individuals
    infected = np.argwhere(population == 1)
    
    for (x, y) in infected:
        # Recovery process
        if np.random.rand() < gamma:
            new_pop[x, y] = 2   # recovered
        
        # Infect neighbours
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            # Check boundaries
            if 0 <= nx < size and 0 <= ny < size:
                if population[nx, ny] == 0:   # susceptible
                    if np.random.rand() < beta:
                        new_pop[nx, ny] = 1   # infected
    
    population = new_pop
    
    # Plot every 10 time steps (or final step)
    if t % 10 == 0 or t == T-1:
        plt.clf()
        plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        plt.title(f'Time step {t}')
        plt.colorbar(ticks=[0,1,2], label='0=Susceptible, 1=Infected, 2=Recovered')
        plt.pause(0.1)   # show dynamically

plt.show()
