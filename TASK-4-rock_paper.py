import random

def your_choice():
    your_choice = input("Enter Rock , Paper , Scissor: ")
    while your_choice not in ["rock","paper","scissor"]:
        print("Invalid choice.")
        your_choice = input("Enter Rock , Paper , Scissor:")
    return your_choice

def computer_choice():
    return random.choice(("rock","paper","scissor"))

def winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "Draw"
    
    elif(
        (user_choice=="rock" and computer_choice=="scissor") or
        (user_choice=="paper" and computer_choice=="rock") or
        (user_choice=="scissor" and computer_choice=="paper")
    ):
        return "Wow!.You Win"
    else:
        return "Computer Win.\nTry Next Chance"
    
if __name__=="__main__":
    print("Welcome to Rock,Paper,Scissor Game")

    while True:
        your_choice== your_choice()
        computer_choice==computer_choice()

        print(f"You chose {your_choice()}")
        print(f"Computer chose {computer_choice()}")

        result= winner(your_choice,computer_choice)
        print(result)


        play_again= input("You want to play again?(yes/no):")
        if play_again != "yes":
            print("Thanks For Playing")
            break