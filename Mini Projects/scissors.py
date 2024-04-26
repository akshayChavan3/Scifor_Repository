import random

class RPSGame:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.results = {
            "Rock": {"Rock": "Draw", "Paper": "Lose", "Scissors": "Win"},
            "Paper": {"Rock": "Win", "Paper": "Draw", "Scissors": "Lose"},
            "Scissors": {"Rock": "Lose", "Paper": "Win", "Scissors": "Draw"}
        }

    def get_computer_choice(self):
        return random.choice(self.choices)

    def play_round(self, choice1, choice2):
        if choice1 not in self.choices or choice2 not in self.choices:
            return "Invalid choice"
        return self.results[choice1][choice2]


def main():
    game = RPSGame()
    rounds = int(input("Enter the number of rounds to play: "))
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        player_choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
        computer_choice = game.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = game.play_round(player_choice, computer_choice)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
