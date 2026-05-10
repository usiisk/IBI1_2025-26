import numpy as np
import matplotlib.pyplot as plt

# Model parameters
N = 10000                # Total population
beta = 0.3               # Infection rate
gamma = 0.05             # Recovery rate
T = 1000                 # Simulation time steps

# Vaccination rates from 0% to 100% with 10% step
vacc_rates = np.arange(0, 1.01, 0.1)

# Create figure
plt.figure(figsize=(8, 5), dpi=150)

# Simulate for each vaccination rate
for vrate in vacc_rates:
    # Initial conditions: vaccinated individuals are immune (considered as Recovered)
    R = int(N * vrate)
    S = N - R - 1         # Susceptible individuals
    I = 1                 # One initial infected individual
    
    # Ensure non-negative population
    S = max(S, 0)
    
    # Record infected individuals over time
    I_list = [I]
    
    # Time iteration
    for t in range(T):
        # Calculate new infections (binomial distribution for stochastic simulation)
        infection_prob = beta * (I / N)
        new_infections = np.random.binomial(S, infection_prob) if S > 0 else 0
        
        # Calculate new recoveries
        new_recoveries = np.random.binomial(I, gamma) if I > 0 else 0
        
        # Update SIR states
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries
        
        # Store results
        I_list.append(I)
    
    # Plot curve for current vaccination rate
    plt.plot(I_list, label=f'{int(vrate*100)}% vaccinated')

# Plot settings
plt.xlabel('Time step')
plt.ylabel('Number of infected')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.savefig("SIR_vaccination.png")  # Save figure as required
plt.show()
