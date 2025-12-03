import json
import rich.console

def LoadJson(filePath: str) -> dict:
    try:
        console = rich.console.Console()
        with open(filePath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red][ERROR][/bold red]: File not found - {filePath}")
        return {}
    except json.JSONDecodeError:
        console.print(f"[bold red][ERROR][/bold red]: JSON decode error - {filePath}")
        return {}
