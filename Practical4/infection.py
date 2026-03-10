# Pseudocode:
# Set initial infected = 5
# Set growth rate = 0.4 (40%)
# Set total students = 91
# Set day = 1
# While infected < total:
#     Print day and infected so far
#     New infected = infected + infected * growth rate
#     infected = infected + infected * growth rate   (or infected = infected * (1 + rate))
#     day += 1
# After loop, print final day and total infected





# Initial values
infected = 5
rate = 0.4
total = 91
day = 1

print("Day 1:", infected, "infected")

while infected < total:
    infected = infected * (1 + rate)   # new infected = old + old*rate
    day += 1
    print(f"Day {day}: {infected} infected")

print(f"All {total} students infected on day {day}")
