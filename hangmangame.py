import random

# Words categorized by themes
word_categories = {
    'animals': ['lion', 'elephant', 'zebra', 'giraffe', 'monkey'],
    'countries': ['india', 'canada', 'brazil', 'australia', 'france'],
    'movies': ['avatar', 'titanic', 'inception', 'frozen', 'jaws']
}

# Hangman ASCII art
hangman_graphics = [
    """
     ------
    |    |
    |
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    -
    """
]

class Hangman:
    def __init__(self):
        self.word = ""
        self.category = ""
        self.guesses_left = 6
        self.guessed_letters = []
        self.hint_taken = False

    def select_word(self, category):
        self.category = category.lower()
        if self.category in word_categories:
            self.word = random.choice(word_categories[self.category])
        else:
            raise ValueError("Invalid category.")

    def display_board(self):
        print(hangman_graphics[6 - self.guesses_left])
        print(f"Category: {self.category.capitalize()}")
        masked_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(f"Word: {masked_word}")
        print(f"Guesses left: {self.guesses_left}")
        print(f"Guessed letters: {', '.join(self.guessed_letters)}")

    def guess_letter(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print(f"You've already guessed '{letter}'. Try another letter.")
            return
        
        self.guessed_letters.append(letter)
        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
        else:
            print(f"Oops! '{letter}' is not in the word.")
            self.guesses_left -= 1

    def check_win(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def play(self):
        print("Welcome to Hangman!")
        print("Select a category:")
        for category in word_categories:
            print(f"- {category.capitalize()}")

        while True:
            category = input("Enter the category: ").strip().lower()
            try:
                self.select_word(category)
                break
            except ValueError:
                print("Invalid category. Please choose from the given options.")

        while self.guesses_left > 0:
            self.display_board()
            guess = input("Guess a letter: ").strip().lower()
            
            if guess == "hint" and not self.hint_taken:
                self.hint_taken = True
                print(f"Hint: The word is '{self.word}'")
                continue
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue
            
            self.guess_letter(guess)
            
            if self.check_win():
                self.display_board()
                print("Congratulations! You guessed the word correctly.")
                break
        
        if self.check_win():
            print("You win!")
        else:
            print(f"Game over! The word was '{self.word}'.")

# Main function to start the game
def main():
    game = Hangman()
    game.play()

if __name__ == "__main__":
    main()
