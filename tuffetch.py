import platform
import psutil
from rich.console import Console
from rich.panel import Panel

console = Console()

os_name = platform.system()
os_release = platform.release()
os_machine = platform.machine()
os_architecture = platform.architecture()
ram = psutil.virtual_memory()
ram_total = ram.total / 1024**3
use_pourcent = psutil.cpu_percent()

content = f"""
[bright_red]OS Name:[/bright_red] {os_name}
[bright_red]OS Release:[/bright_red] [white]{os_release}[/white]
[bright_red]OS Machine:[/bright_red] {os_machine}
[bright_red]OS Architecture[/bright_red]: [white]{os_architecture}[/white]
[bright_red]RAM:[/bright_red] [white]{ram_total} GB[/white]
[bright_red]Pourcent of used CPU:[/bright_red] [white]{use_pourcent} %[/white]
"""

panel = Panel(content, title="[bold red]TufFetch")
console.print(panel)