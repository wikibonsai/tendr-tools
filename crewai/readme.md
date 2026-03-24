# CrewAI Integration

`tendr_tool.py` — A CrewAI Tool for safe WikiBonsai cultivation.

## Usage

```python
from crewai import Agent
from tendr_tools.crewai.tendr_tool import tendr

gardener = Agent(
    role="Knowledge Gardener",
    goal="Tend and cultivate the team's semantic memory",
    tools=[tendr],
    verbose=True
)
```

