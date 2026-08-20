import json
import random
from typing import List, Tuple

class ScrambleGame:
    def __init__(self, word_file: str = "data/words.json", max_attempts: int = 3):
        self.max_attempts = max_attempts
        self.attempts = max_attempts
        self.words = self._load_words(word_file)
        self.target_word = random.choice(self.words).upper()
        self.scrambled_word = self._scramble_word(self.target_word)
        self.history: List[str] = []

    def _load_words(self, file_path: str) -> List[str]:
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return ["LOGIC", "CYBER", "PIXEL", "GREEN", "WATER"]

    def _scramble_word(self, word: str) -> str:
        letters = list(word)
        # Kocok sampai hasil acakannya tidak sama dengan kata asli
        while True:
            random.shuffle(letters)
            scrambled = "".join(letters)
            if scrambled != word:
                return " ".join(scrambled)

    def validate_guess(self, guess: str) -> Tuple[bool, str]:
        guess = guess.upper().strip()
        if len(guess) != len(self.target_word):
            return False, f"Kata harus terdiri dari {len(self.target_word)} huruf!"
        return True, ""

    def make_move(self, guess: str) -> bool:
        guess = guess.upper().strip()
        self.history.append(guess)
        if guess != self.target_word:
            self.attempts -= 1
            return False
        return True

    def is_won(self) -> bool:
        return len(self.history) > 0 and self.history[-1] == self.target_word

    def is_game_over(self) -> bool:
        return self.is_won() or self.attempts <= 0