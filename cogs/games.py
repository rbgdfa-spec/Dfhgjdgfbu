import random

class GamesCog:
    def rock_paper_scissors(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(choices)
        if user_choice == bot_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and bot_choice == 'scissors') or \
             (user_choice == 'paper' and bot_choice == 'rock') or \
             (user_choice == 'scissors' and bot_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

    def tic_tac_toe(self, board, player, position):
        if board[position] == ' ':
            board[position] = player
        else:
            return "Position already taken!"
        
        # Check for win conditions (to be implemented)
        return board

    def trivia(self, question, answer):
        # Simple trivia check
        response = input(question)
        return response.lower() == answer.lower()

    def fight(self, player1, player2):
        winner = random.choice([player1, player2])
        return f"The winner is {winner}!"

# Additional functionalities and command handlers can be added as needed