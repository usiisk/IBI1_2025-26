import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05
T = 1000

# Different vaccination proportions (0% to 100%, step 10%)
vacc_rates = np.arange(0, 1.01, 0.1)

plt.figure(figsize=(8, 5), dpi=150)

for vrate in vacc_rates:
    # Initial state: vaccinated proportion is removed from susceptible group
    # Here we treat vaccinated individuals as initially recovered (immune)
    S = int(N * (1 - vrate)) - 1   # subtract the initial infected person
    I = 1
    R = int(N * vrate)
    if S < 0:
        S = 0
    
    I_list = [I]
    
    for t in range(T):
        infection_prob = beta * (I / N)
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()
        
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries
        
        I_list.append(I)
    
    plt.plot(I_list, label=f'{int(vrate*100)}% vaccinated')

plt.xlabel('Time step')
plt.ylabel('Number of infected')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend()
plt.show()
