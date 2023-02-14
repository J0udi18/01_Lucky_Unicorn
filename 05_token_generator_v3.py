import random

# Main routine goes here
tokens = {"unicorn", "horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"}
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loope to generate 20 tokens
for items in range (0,500):
    chosen = random.choice (tokens)

    #Adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5


print()
print("STARTING BALANCE: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))