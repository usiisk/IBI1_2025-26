import numpy as np
import matplotlib.pyplot as plt

# Parameters for spatial SIR model
size = 100                  # Grid size (100x100)
beta = 0.3                  # Infection probability per neighbor contact
gamma = 0.05                # Recovery probability per time step
T = 100                     # Total simulation time steps

# Initialize grid: 0 = Susceptible, 1 = Infected, 2 = Recovered
population = np.zeros((size, size), dtype=int)

# Randomly select one individual as initial infection
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1

# Create figure for dynamic visualization
plt.figure(figsize=(6, 4), dpi=150)

# 8-directional neighbors for spatial infection
neighbors = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),          (0, 1),
             (1, -1),  (1, 0), (1, 1)]

# Main simulation loop
for t in range(T):
    # Use a copy to ensure simultaneous state update
    new_pop = population.copy()
    
    # Get coordinates of all infected individuals
    infected_coords = np.argwhere(population == 1)
    
    # Process each infected cell
    for (x, y) in infected_coords:
        # Recovery process
        if np.random.rand() < gamma:
            new_pop[x, y] = 2
        
        # Infection process: spread to 8 neighbors
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            # Check grid boundaries
            if 0 <= nx < size and 0 <= ny < size:
                # Only susceptible neighbors can be infected
                if population[nx, ny] == 0 and np.random.rand() < beta:
                    new_pop[nx, ny] = 1
    
    # Update population to new state
    population = new_pop
    
    # Plot and update animation every 10 steps or at final step
    if t % 10 == 0 or t == T - 1:
        plt.clf()
        plt.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        plt.title(f'Time step {t}')
        plt.colorbar(ticks=[0, 1, 2], label='0=Susceptible, 1=Infected, 2=Recovered')
        plt.pause(0.1)

# Save the final state of simulation
plt.savefig("spatial_SIR_final.png")
plt.show()
