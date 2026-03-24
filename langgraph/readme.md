# LangGraph Integration

`tendr_tool.py` — A clean LangChain/LangGraph Tool for safely tending your WikiBonsai garden.

## Usage

```python
from langgraph.prebuilt import create_react_agent
from tendr_tools.langgraph.tendr_tool import tendr

tools = [tendr]

agent = create_react_agent(llm, tools)
```

The agent can now safely call `tendr` commands such as:

- `tendr tree`
- `tendr stat "Agentic Memory"`
- `tendr seed "New Concept"`
- `tendr doctor`
- `tendr rename OldName NewName`

See `tendr_tool.py` for the full list of supported commands and docstring.
