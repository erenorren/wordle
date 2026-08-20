from rich.console import Console
from rich.prompt import Prompt
from src.game import WordleGame
from src.ui import WordleUI

console = Console()

def main():
    WordleUI.show_banner()
    game = WordleGame()

    while not game.is_game_over():
        guess = Prompt.ask(f"\nTebakan kamu (Sisa {game.attempts})")
        valid, msg = game.validate_guess(guess)
        
        if not valid:
            console.print(f"[bold red]❌ {msg}[/bold red]")
            continue

        game.make_move(guess)
        WordleUI.render_board(game)

        if game.is_won():
            console.print(f"\n🎉 [bold green]EXCELLENT! Kamu berhasil menebak kata: {game.target_word}[/bold green]\n")
            return

    console.print(f"\n💀 [bold red]GAME OVER![/bold red] Kata yang benar adalah: [bold cyan]{game.target_word}[/bold cyan]\n")

if __name__ == "__main__":
    main()