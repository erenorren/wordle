import json
import random
from typing import List, Tuple

class WordleGame:
    def __init__(self, word_file: str = "data/words.json", max_attempts: int = 6):
        self.max_attempts = max_attempts
        self.attempts = max_attempts
        self.word_length = 5
        self.words = self._load_words(word_file)
        self.target_word = random.choice(self.words).upper()
        self.history: List[Tuple[str, List[str]]] = []

    def _load_words(self, file_path: str) -> List[str]:
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return ["LOGIK", "CYBER", "KODING"]

    def validate_guess(self, guess: str) -> Tuple[bool, str]:
        guess = guess.upper().strip()
        if len(guess) != self.word_length:
            return False, f"Kata harus terdiri dari {self.word_length} huruf!"
        return True, ""

    def evaluate_guess(self, guess: str) -> List[str]:
        guess = guess.upper()
        feedback = []
        for i in range(len(guess)):
            if guess[i] == self.target_word[i]:
                feedback.append("CORRECT")     # Hijau
            elif guess[i] in self.target_word:
                feedback.append("PRESENT")     # Kuning
            else:
                feedback.append("ABSENT")      # Abu-abu
        return feedback

    def make_move(self, guess: str) -> List[str]:
        guess = guess.upper()
        evals = self.evaluate_guess(guess)
        self.history.append((guess, evals))
        self.attempts -= 1
        return evals

    def is_won(self) -> bool:
        return len(self.history) > 0 and self.history[-1][0] == self.target_word

    def is_game_over(self) -> bool:
        return self.is_won() or self.attempts <= 0