# Letta Integration

`tendr_tool.py` — Companion tool for Letta Context Repositories / MemFS.

Best used together with Letta’s Obsidian plugin pointing at your WikiBonsai garden.

## Usage

```python
from tendr_tools.letta.tendr_tool import tendr

# Register with your Letta SDK (exact method depends on version)
tool = create_tool(tendr)
```

This gives your Letta agents safe, structured access to `tendr` commands while keeping the Markdown vault as the single source of truth.
