# run bash shell cmd in Py
import subprocess

# from PyInquirer import prompt, print_json, Spearator
from rich import print as rprint
import typer

app = typer.Typer()


@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yellow]")


@app.command("list")
def guilist():
    subprocess.run(f"ls -l", shell=True)


if __name__ == "__main__":
    app()
