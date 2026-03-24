import subprocess
from pathlib import Path
import os

VAULT_PATH = Path(os.getenv("TENDR_VAULT", Path.home() / "garden"))

def tendr(command: str) -> str:
    """Safe tendr-cli operations — perfect companion to Letta Context Repositories / MemFS."""
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
        return output or "✅ Operation complete."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Register with: tool = create_tool(tendr)  # or your Letta SDK method
