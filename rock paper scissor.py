import random
count_p=0
count_c=0

selection=('rock','paper','scissor')
computer=random.choice(selection)
while True:
    player=input("Enter ur choice:")
    if player==computer:
        print("You:",player)
        print("Computer:",computer)
        print("It's a tie")
        count_p=count_p+1
        count_c=count_c+1
        print("You:",count_p)
        print("Computer:",count_c)
    elif player=="rock" and computer=="scissor":
        print("You:",player)
        print("Computer:",computer)
        print("You win!")
        count_p=count_p+1
        print("You:",count_p)
        print("Computer:",count_c)
    elif player=="paper" and computer=="rock":
        print("You:",player)
        print("Computer:",computer)
        print("You win!")
        count_p=count_p+1
        print("You:",count_p)
        print("Computer:",count_c)
    elif player=="scissor" and computer=="paper":
        print("You:",player)
        print("Computer:",computer)
        print("You win!")
        count_p=count_p+1
        print("You:",count_p)
        print("Computer:",count_c)

    else:
        print("You:",player)
        print("Computer:",computer)
        print("Computer Wins!")
        count_c=count_c+1
        print("You:",count_p)
        print("Computer:",count_c)

    again=input("Do you want to play again (y/n)?:")
    if again=='n':
        print("Thank you!!")
        break
    continue