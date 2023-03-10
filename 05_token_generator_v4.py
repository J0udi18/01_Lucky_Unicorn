import random

# Main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loope to generate 20 tokens
for items in range (0,10):
    chosen_num = random.randint (1,100)

    #Adjust balance
    # if the random # is between 1 and 5,
    # users gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn" 
        balance += 4

    # if the random # is between 6 and 36
    #users gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        # The token is either a horse or zebra...
        # #in both cases, subtract $0.50 from the balance 
    else:
        # if the number is even, set the ohosen
        #item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen= "zebra"
        balance -= 0.5

    print("you got a {} .  your balance is "
          "${:.2f}".format(chosen,balance))
    
print()
print()
print("STARTING BALANCE: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))