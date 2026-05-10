# What does this piece of code do?
# Answer: This code runs a loop 11 times to generate 11 random integers between 1 and 10, accumulates their total sum, and prints the final total.

# Import libraries
# randint allows drawing a random number, e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer. e.g. ceil(4.2)=5
from math import ceil

# Initialize total sum of random numbers and loop progress
total_rand = 0
progress = 0

# Loop runs 11 times (progress from 0 to 10)
while progress <= 10:
    progress += 1               # Increment loop counter
    n = randint(1, 10)         # Generate random integer between 1 and 10
    total_rand += n            # Add random number to total sum

# Print the final sum of 11 random numbers
print(total_rand)
