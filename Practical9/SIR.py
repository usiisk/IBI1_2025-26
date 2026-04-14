import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000          # total population
beta = 0.3         # infection probability per contact
gamma = 0.05       # recovery probability
T = 1000           # number of time steps

# Initial state
S = N - 1
I = 1
R = 0

# Record history
S_list = [S]
I_list = [I]
R_list = [R]

# Time loop
for t in range(T):
    # New infections: each susceptible gets infected with probability beta * (I/N)
    infection_prob = beta * (I / N)
    new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
    
    # New recoveries: each infected recovers with probability gamma
    new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
    
    # Update states
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries
    
    # Record
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time step')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.show()
