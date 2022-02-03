import random


class Wordle:
    default_word_list = [
        "one",
        "ape",
        "ore",
        "two",
        "three",
        "four",
        "five",
        "apple",
    ]

    def __init__(self, word_list=None, max_guesses=6):
        self.max_guesses = max_guesses
        self.word_list = word_list or self.default_word_list
        self.current_letters = list()
        self.guess_count = 0

    def play(self):
        word = random.choice(self.word_list)
        used_letters = set()

        self._print_first_line(word)
        while self.guess_count < self.max_guesses:
            self._print_previously_guessed(used_letters)
            new_guess = self._prompt_for_guess(word)
            used_letters |= set(new_guess)
            self._add_guess(new_guess, word)
            self.guess_count += 1
            if self._problem_solved(new_guess, word):
                print(f"You did it! The word was: {word}")
                return

        self._print_failure_message(word)

    def _print_first_line(self, word):
        print("_" * len(word))

    def _prompt_for_guess(self, word: str) -> str:
        while True:
            guess = input("Enter a new letter to guess: ")
            valid_guess = self._validate_guess(guess, word)
            if valid_guess:
                return guess

    def _validate_guess(self, guess: str, word: str) -> bool:
        correct_length = len(guess) == len(word)
        in_word_list = guess in self.word_list
        return correct_length and in_word_list

    def _print_previously_guessed(self, used_letters: set):
        print("Letters used: ", "".join(used_letters))

    def _add_guess(
        self,
        guess: str,
        word: str,
    ):
        correct_letters_wrong_place = list()
        correct_letters_correct_place = list()
        for idx, (target_letter, guess_letter) in enumerate(zip(word, guess)):
            if target_letter == guess_letter:
                correct_letters_correct_place.append((idx, guess_letter))
            elif guess_letter in word:
                correct_letters_wrong_place.append((idx, guess_letter))
        self._print_guess_evaluation(
            word=word,
            correct_letters_wrong_place=correct_letters_wrong_place,
            correct_letters_correct_place=correct_letters_correct_place,
        )

    def _print_guess_evaluation(
        self,
        word: str,
        correct_letters_wrong_place: list[tuple[int, str]],
        correct_letters_correct_place: list[tuple[int, str]],
    ):
        correct_letters = dict(correct_letters_correct_place)
        wrong_letters = dict(correct_letters_wrong_place)
        evaluation_repr = list()
        for i in range(len(word)):
            if correct_letter := correct_letters.get(i):
                evaluation_repr.append(correct_letter)
            elif wrong_letter := wrong_letters.get(i):
                evaluation_repr.append(f"|{wrong_letter}|")
            else:
                evaluation_repr.append("*")
        print("".join([ch for ch in evaluation_repr]))

    def _problem_solved(
        self,
        guess: str,
        word: str,
    ) -> bool:
        return guess == word

    def _print_failure_message(self, word: str):
        print(f"Oh darn! You're not very good at this game! The word was: {word}")
