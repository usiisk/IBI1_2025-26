import numpy as np
import matplotlib.pyplot as plt

# Parameters for the SIR model
N = 10000          # Total population
beta = 0.3         # Infection probability per contact
gamma = 0.05       # Recovery probability
T = 1000           # Number of time steps

# Initial state of the population
S = N - 1          # Susceptible individuals
I = 1              # Infected individuals
R = 0              # Recovered individuals

# Lists to record the history of each compartment
S_list = [S]
I_list = [I]
R_list = [R]

# Time iteration for the stochastic SIR simulation
for t in range(T):
    # Calculate infection probability for susceptible individuals
    infection_prob = beta * (I / N)
    
    # Generate new infections (with boundary protection)
    new_infections = np.random.binomial(S, infection_prob) if S > 0 else 0
    
    # Generate new recoveries (with boundary protection)
    new_recoveries = np.random.binomial(I, gamma) if I > 0 else 0
    
    # Update the S, I, R compartments
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    
    # Append updated values to history lists
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot the simulation results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time step')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig("SIR_simulation.png")  # Save figure as required
plt.show()
