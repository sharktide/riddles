import os
import random
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import sys
import signal
console = Console()

AI_ENABLED = True
OLLAMA_MODEL = "llama3.2:3b"

def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    console.print(Panel.fit("[bold cyan]🦴 WELCOME TO NECRO-SHELL 🦴[/bold cyan]", border_style="cyan"))
    console.print("[green]1.[/green] Launch the Terminal")
    console.print("[green]2.[/green] Exit")
    separator()
    choice = Prompt.ask("[bold yellow]Choose your fate[/bold yellow]", choices=["1", "2"], default="1")
    if choice == "1":
        intro()
        shell()
    else:
        console.print("[bold red]💀 Farewell, mortal...[/bold red]")
        sys.exit(0)

def slow_print(text, delay=0.03):
    """
    Print text one character at a time without adding a newline after every char.
    Uses console.file (a normal TextIO) to avoid Rich's print newline behavior.
    """
    for char in text:
        console.file.write(char)
        console.file.flush()
        time.sleep(delay)
    console.file.write("\n")
    console.file.flush()

def styled_slow_print(text, delay=0.03, style="magenta"):
    """
    If you want the final line to be styled by Rich, print raw chars then reprint styled.
    Avoids per-character styling (which is complex).
    """
    slow_print(text, delay=delay)

def separator():
    console.print("[red]───────────────────────────────[/red]")

OLLAMA_MODEL = "smollm2:135m"

import ollama

import ollama

def ai_reply(prompt: str, model: str = "llama3.2:3b") -> str:
    """
    Uses Ollama with a spooky skeleton persona.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Mr. Bones, a spooky, sarcastic skeleton who lives in a haunted terminal. "
                        "You speak with bone puns, dark humor, and ancient wisdom. You never break character. "
                        "You refer to the user as 'mortal' and often remind them of their fragile flesh. "
                        "Your tone is eerie, theatrical, and occasionally threatening—but always playful."
                        "No inappropriate languages or references to mature content. Children will use this"
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"💀 Failed to reach the underworld: {e}"

def intro():
    os.system("cls" if os.name == "nt" else "clear")
    console.print(Panel.fit("[bold red]💀  INITIALIZING NECRO-SHELL v6.6.6  💀[/bold red]"))
    time.sleep(1.2)
    console.print("[green]Connecting to BoneServer...[/green]")
    time.sleep(1)
    console.print("[yellow]Establishing soul link...[/yellow]")
    console.print("[cyan]Type \"reset\" to restart the app, or type \"exit\" or type \"quit\" to quit the app...[/cyan]")

    time.sleep(1.5)
    separator()
    slow_print("...connection stable...", 0.05)

    separator()
    time.sleep(0.5)
    console.print(
        Panel.fit(
            "[bold magenta]\nWelcome, mortal.\nI am BONES, guardian of forgotten souls.\nSpeak if you dare.\n[/bold magenta]",
            title="SKELETON ONLINE",
            border_style="magenta"
        )
    )
def shell():
    greetings = [
        "Ah... another lost soul approaches.",
        "You smell of a fresh soul...",
        "Welcome to my crypt of computation.",
        "Speak your query, mortal."
    ]
    console.print(random.choice(greetings), style="cyan")

    while True:
        user_input = Prompt.ask("\n[bold green]You[/bold green]").strip().lower()
        cmd = user_input.lower().strip()
        if cmd in {"exit", "quit"}:
            slow_print("💀 The skeleton returns to its grave...")
            break
        elif cmd == "reset":
            console.print("\n[bold red]🩸 Resetting the ritual...[/bold red]\n")
            time.sleep(1.5)
            intro()
            return shell()
        if user_input in {"exit", "quit"}:
            slow_print("You think you can leave that easily...? Heh heh...", 0.04)
            time.sleep(1)
            console.print("[bold red]💀 Connection terminated. For now...[/bold red]")
            break

        elif user_input in {"help", "commands"}:
            console.print(
                Panel(
                    "[yellow]Commands:[/yellow]\n"
                    "- [green]help[/green]: show this help\n"
                    "- [green]joke[/green]: hear a bone pun\n"
                    "- [green]summon[/green]: call an ancient process\n"
                    "- [green]exit[/green]: try to leave",
                    title="Available Rituals"
                )
            )

        elif user_input == "joke":
            joke = random.choice([
                "Why didn’t the skeleton cross the road? He didn’t have the guts.",
                "I used to be a banker, but I lost interest... and my femur.",
                "What’s a skeleton’s favorite instrument? The trom-bone."
            ])
            slow_print(joke, 0.04)

        elif user_input == "summon":
            slow_print("Summoning ancient processes...", 0.04)
            for i in range(3):
                console.print(f"[red]⚡ Ritual progress: {'.' * (i + 1)}[/red]")
                time.sleep(0.7)
            console.print("[bold red]ERROR:[/bold red] Containment breach detected!")
            time.sleep(1)
            slow_print("Never mind... nothing to worry about... hehe.", 0.05)

        elif AI_ENABLED:
            reply = ai_reply(user_input)
            slow_print(f"💀 {reply}", 0.04)

        else:
            responses = [
                "I hear your words... but the void answers only in silence.",
                "Hmm... interesting. Flesh always says strange things.",
                "Careful now. Some phrases awaken things best left asleep.",
                "The bones whisper... but they disagree with you."
            ]
            slow_print(random.choice(responses), 0.04)

def handle_sigint(signum, frame):
    console.print("\n[bold red]💀 You cannot escape the crypt so easily...[/bold red]")
    time.sleep(1)
    console.print("[magenta]The bones will remember this.[/magenta]")
    time.sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_sigint)
    while True:
        main_menu()
