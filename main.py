import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

WORD_LIST = ["LOGIK", "KODING", "CYBER", "PINTU", "TUGAS", "PRAKT"]

def print_banner():
    console.print(
        Panel.fit(
            "[bold cyan]WORDLE CLI GAME[/bold cyan]\n[dim]Tebak kata 5 huruf dalam 6 kali percobaan[/dim]",
            border_style="cyan"
        )
    )

def evaluate_guess(guess, target):
    feedback = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
            # Hijau: Huruf & Posisi Benar
            feedback.append(f"[white on green] {guess[i]} [/white on green]")
        elif guess[i] in target:
            # Kuning: Huruf Benar, Posisi Salah
            feedback.append(f"[black on yellow] {guess[i]} [/black on yellow]")
        else:
            # Abu-abu: Huruf Tidak Ada
            feedback.append(f"[white on bright_black] {guess[i]} [/white on bright_black]")
    return " ".join(feedback)

def play():
    print_banner()
    target = random.choice(WORD_LIST)
    attempts = 6
    history = []

    while attempts > 0:
        guess = Prompt.ask(f"\n[bold]Tebakan kamu ({attempts} sisa)[/bold]").upper().strip()

        if len(guess) != 5:
            console.print("[bold red]❌ Kata harus terdiri dari 5 huruf![/bold red]")
            continue

        result = evaluate_guess(guess, target)
        history.append(result)

        # Tampilkan riwayat papan tebakan
        console.print("\n[bold]Papan Permainan:[/bold]")
        for board_line in history:
            console.print(board_line)

        if guess == target:
            console.print("\n🎉 [bold green]SELAMAT! Tebakan kamu benar![/bold green]\n")
            return

        attempts -= 1

    console.print(f"\n💀 [bold red]GAME OVER![/bold red] Kata yang benar adalah: [bold cyan]{target}[/bold cyan]\n")

if __name__ == "__main__":
    play()