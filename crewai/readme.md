# tendr-tools/crewai

## CrewAI Integration

`tendr_tool.py` — A CrewAI Tool for safe WikiBonsai cultivation.

## Usage

```python
from crewai import Agent
from tendr_tools.crewai.tendr_tool import tendr

researcher = Agent(
    role="Knowledge Gardener",
    goal="Tend the team's semantic memory",
    tools=[tendr],
    verbose=True
)
```
