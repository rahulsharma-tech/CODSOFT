import random

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('rock', 'rock'): 0, ('rock', 'paper'): 2, ('rock', 'scissors'): 1,
        ('paper', 'rock'): 1, ('paper', 'paper'): 0, ('paper', 'scissors'): 2,
        ('scissors', 'rock'): 2, ('scissors', 'paper'): 1, ('scissors', 'scissors'): 0
    }
    return outcomes[(user_choice, computer_choice)]

def display_choices(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

def print_result(result):
    if result == 0:
        print("It's a draw!")
    elif result == 1:
        print("You win!")
    elif result == 2:
        print("Computer wins!")

def main():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors game!")

    play_again = True
    while play_again:
        print("\nChoose one: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()

        while user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Your choice: ").lower()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        
        print_result(result)

        if result == 1:
            user_score += 1
        elif result == 2:
            computer_score += 1

        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

    print(f"\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
