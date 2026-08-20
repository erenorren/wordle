from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from src.game import WordleGame

console = Console()

class WordleUI:
    @staticmethod
    def show_banner():
        console.print(
            Panel.fit(
                "[bold cyan]🎯 WORDLE CLI PROFESSIONAL[/bold cyan]\n"
                "[dim]Built with Python & Rich | Modular Architecture[/dim]",
                border_style="cyan"
            )
        )

    @staticmethod
    def render_board(game: WordleGame):
        console.print("\n[bold]Papan Permainan:[/bold]")
        for guess, evals in game.history:
            formatted_letters = []
            for char, status in zip(guess, evals):
                if status == "CORRECT":
                    formatted_letters.append(f"[bold white on green] {char} [/bold white on green]")
                elif status == "PRESENT":
                    formatted_letters.append(f"[bold black on yellow] {char} [/bold black on yellow]")
                else:
                    formatted_letters.append(f"[bold white on bright_black] {char} [/bold white on bright_black]")
            console.print(" ".join(formatted_letters))