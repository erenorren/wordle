from rich.console import Console
from rich.panel import Panel
from src.game import ScrambleGame

console = Console()

class ScrambleUI:
    @staticmethod
    def show_banner(scrambled_word: str):
        console.print(
            Panel.fit(
                f"[bold cyan]🔤 WORD SCRAMBLE GAME[/bold cyan]\n\n"
                f"Susun huruf acak ini: [bold yellow]{scrambled_word}[/bold yellow]",
                border_style="cyan"
            )
        )

    @staticmethod
    def render_history(game: ScrambleGame):
        if game.history:
            console.print("\n[bold]Riwayat Tebakan Salah:[/bold]")
            for guess in game.history:
                if guess != game.target_word:
                    console.print(f"[dim red]❌ {guess}[/dim red]")