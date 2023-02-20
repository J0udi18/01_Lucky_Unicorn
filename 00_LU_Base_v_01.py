import random

# Function go here...
def yes_no (question) :
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


def instructions () :
       print("**** How to play ****")
       print()
       print("The rules of the game go here")
       print()
       return ""


def num_check (question, low, high):
    error = "please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:                
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print (error)


# Main Routine goes here...
played_before = yes_no ("Have you played the game before? ")

if played_before == "no":
        instructions ()

print()

# Ask user how much they want to play with...
# Main routine goe here
how_much = num_check("How much would you"
                   "like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":
    # inorease # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # users gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

        # if the random # is between 6 and 36
    # users gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    # The token is either a horse or zebra...
    # #in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the ohosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5

    print("you got a {}. your balance is "
          "${:.2f}".format(chosen, balance))

    if balance < 1:
        # if balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print("final balance", balance)
