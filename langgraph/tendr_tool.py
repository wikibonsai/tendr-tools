from langchain_core.tools import tool
import subprocess
from pathlib import Path
import os

# Set via env var or default to your garden
VAULT_PATH = Path(os.getenv("TENDR_VAULT", Path.home() / "garden"))

@tool
def tendr(command: str) -> str:
    """Safe, deterministic tendr-cli operations on the WikiBonsai garden.
    
    Preferred over raw file edits.
    Examples: "tree", "stat Agentic Memory", "seed 'New Concept'", "rename Old New", "doctor"
    """
    try:
        result = subprocess.run(
            ["tendr", *command.split()],
            cwd=VAULT_PATH,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = result.stdout.strip()
        if result.stderr:
            output += f"\n⚠️ {result.stderr.strip()}"
        return output or "✅ Operation completed."
    except Exception as e:
        return f"❌ Error: {str(e)}"
