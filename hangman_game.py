# hangman_class.py
import random
from wordlist import words

class Hangman:
    hangman_art = {
        0: ("   ",
            "   ",
            "   "),
        1: (" O ",
            "   ",
            "   "),
        2: (" O ",
            " | ",
            "   "),
        3: (" O ",
            "/| ",
            "   "),
        4: (" O ",
            "/|\\",
            "   "),
        5: (" O ",
            "/|\\",
            "/  "),
        6: (" O ",
            "/|\\",
            "/ \\")
    }

    def __init__(self):
        """Initialize the Hangman game."""
        self.answer = random.choice(words)
        self.hint = ["_"] * len(self.answer)
        self.wrong_guesses = 0
        self.guessed_letters = set()
        self.is_running = True

    def display_man(self):
        """Display hangman based on wrong guesses."""
        print("**********")
        for line in self.hangman_art[self.wrong_guesses]:
            print(line)
        print("**********")

    def display_hint(self):
        """Display the current word hint."""
        print(" ".join(self.hint))

    def display_answer(self):
        """Display the final answer."""
        print(f"The word was: {self.answer}")

    def guess_letter(self, guess):
        """Handle the player’s guess logic."""
        guess = guess.lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter one letter.")
            return

        if guess in self.guessed_letters:
            print(f"You already guessed '{guess}'.")
            return

        self.guessed_letters.add(guess)

        if guess in self.answer:
            for i, letter in enumerate(self.answer):
                if letter == guess:
                    self.hint[i] = guess
        else:
            self.wrong_guesses += 1

    def check_game_over(self):
        """Check win/lose conditions."""
        if "_" not in self.hint:
            self.display_man()
            self.display_answer()
            print("🎉 You Win!")
            self.is_running = False
        elif self.wrong_guesses >= len(self.hangman_art) - 1:
            self.display_man()
            self.display_answer()
            print("💀 You Lose!")
            self.is_running = False

    def play(self):
        """Main game loop."""
        print("Welcome to Hangman!")
        while self.is_running:
            self.display_man()
            self.display_hint()
            guess = input("Enter a letter: ")
            self.guess_letter(guess)
            self.check_game_over()


if __name__ == "__main__":
    game = Hangman()
    game.play()
