import random

while True:
    print("----- Lottery -----")

    question = input("Generate? (y/n): ")

    if question == "y":
        player_number = random.randint(2, 10)
        machine = random.randint(2, 10)
        print("Machine number:", machine)
        print("Your number:", player_number)
        if machine == player_number:
            print("You win!")
        else:
            print("You lose! :(")
    if question == "n":
        break