# Write a rock, paper, scissors game
# import random module
import random
import inquirer

# Define game choices and win conditions
CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the game.
    
    Args:
        user_choice: The user's choice (str)
        computer_choice: The computer's choice (str)
    
    Returns:
        str: 'user' if user wins, 'computer' if computer wins, 'tie' if tie
    """
    if user_choice == computer_choice:
        return 'tie'
    elif computer_choice in WINS[user_choice]:
        return 'user'
    else:
        return 'computer'

def is_valid_choice(choice):
    """
    Check if a choice is valid.
    
    Args:
        choice: The choice to validate (str)
    
    Returns:
        bool: True if valid, False otherwise
    """
    return choice in CHOICES

def get_computer_choice():
    """
    Get a random choice for the computer.
    
    Returns:
        str: A random choice from CHOICES
    """
    return random.choice(CHOICES)

def main():
    """Main function that handles the rock-paper-scissors-lizard-spock game logic."""
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("=" * 50)
    print("\nUse arrow keys to select your choice and press Enter\n")
    
    # Game loop
    while True:
        # Create interactive menu
        questions = [
            inquirer.List('choice',
                         message="What do you throw?",
                         choices=CHOICES + ['Quit'],
                         carousel=True)
        ]
        
        # Get user selection
        answers = inquirer.prompt(questions)
        
        # Handle case where user cancels (Ctrl+C)
        if answers is None:
            print("\nThanks for playing! Goodbye!")
            break
        
        user_choice = answers['choice'].lower()
        
        # Check if user wants to quit
        if user_choice == 'quit':
            print("\nThanks for playing! Goodbye!")
            break
        
        # Computer makes random choice
        computer_choice = get_computer_choice()
        print(f"\n🎯 You chose: {user_choice.upper()}")
        print(f"🤖 Computer chose: {computer_choice.upper()}")
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        if result == 'tie':
            print("🤝 It's a tie!")
        elif result == 'user':
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")
        print()

if __name__ == "__main__":
    main()