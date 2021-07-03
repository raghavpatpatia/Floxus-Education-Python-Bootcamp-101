import random
choice = ['Rock', 'Paper', 'Scissors']
while True:
    print('Welcome!')
    user_count = 0
    comp_count = 0
    for i in range(1, 4):
        print("Round", i)
        print("Enter a value 1.Rock 2.Paper 3.Scissors")
        your_choice = int(input())

        if(your_choice == 1):
            print("You have selected Rock")
            your_choice = "Rock"

        elif (your_choice == 2):
            print("You have selected Paper")
            your_choice = "Paper"

        elif (your_choice == 3):
            print("You have selected Scissors")
            your_choice = "Scissors"

        else:
            print("Wrong choice, please select again")
            break

        computerChoice = random.choice(choice)
        print("Computer selects", computerChoice)

        if(your_choice == computerChoice):
            print("Draw")

        elif((your_choice == 'Paper' and computerChoice == 'Rock') or
             (your_choice == 'Rock' and computerChoice == 'Scissors') or
            (your_choice == 'Scissors' and computerChoice == 'Paper')):
                user_count = user_count + 1

        elif ((your_choice == 'Rock' and computerChoice == 'Paper') or
              (your_choice == 'Scissors' and computerChoice == 'Rock') or
              (your_choice == 'Paper' and computerChoice == 'Scissors')):
                comp_count = comp_count + 1

    if user_count > comp_count:
        print("your Score:", user_count)
        print("Computer's Score:", comp_count)
        print("You Win!")
    elif user_count < comp_count:
        print("your Score:", user_count)
        print("Computer's Score:", comp_count)
        print("Computer Wins!")
    else:
        print("your Score:", user_count)
        print("Computer's Score:", comp_count)
        print("Draw!!")

    print("Do you want to play again?")
    x = input("Enter yes or no: ")
    if x == 'yes' or x == 'Yes' or x == 'YES' or x == 'Y' or x == 'y':
        continue
    else:
        break
