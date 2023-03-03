import random


# Function go here...
def yes_no(question):
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


# displays instructions, returns 'None'
def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# checks users enter a number between two integers
def num_check(question, low, high):
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
            print(error)


def statement_generator(statement, var_decoration, lines=None):
    sides = var_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = var_decoration * len(statement)

    if lines == 1:
        print(statement)
    else:
        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""


# Main Routine goes here...
statement_generator("welcome to the Lucky Unicorn Game", "*")
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with...
# Main routine goe here
how_much = num_check("How much would you"
                     "like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
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
        decoration = "!"
        balance += 4

        # if the random # is between 6 and 36
    # users gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    # The token is either a horse or zebra...
    # #in both cases, subtract $0.50 from the balance
    else:
        # if the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "you got a {}. your balance is " \
              "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration, 1)

    if balance < 1:
        # if balance is too low, exit the game and
        # output a suitable message
        play_again = "xxx"
        print("sorry you have run out of money")

    else:
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print(f'final balance: ${balance:.2f}')
print("final balance", balance)
print("thank you for playing")
