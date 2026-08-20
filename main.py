from rich.console import Console
from rich.prompt import Prompt
from src.game import ScrambleGame
from src.ui import ScrambleUI

console = Console()

def main():
    game = ScrambleGame()
    ScrambleUI.show_banner(game.scrambled_word)

    while not game.is_game_over():
        guess = Prompt.ask(f"\n[bold]Tebakan kamu[/bold] (Sisa {game.attempts}x kesempatan)")
        valid, msg = game.validate_guess(guess)
        
        if not valid:
            console.print(f"[bold red]⚠️ {msg}[/bold red]")
            continue

        is_correct = game.make_move(guess)
        ScrambleUI.render_history(game)

        if is_correct:
            console.print(f"\n🎉 [bold green]EXCELLENT! Tebakanmu benar: {game.target_word}[/bold green]\n")
            return

    console.print(f"\n💀 [bold red]GAME OVER![/bold red] Jawaban yang benar adalah: [bold cyan]{game.target_word}[/bold cyan]\n")

if __name__ == "__main__":
    main()