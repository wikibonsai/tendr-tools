
# tendr-tools/langgraph

## LangGraph Integration

`tendr_tool.py` — A clean LangChain/LangGraph Tool for tending your WikiBonsai garden.

## Usage

```python
from langgraph.prebuilt import create_react_agent
from tendr_tools.langgraph.tendr_tool import tendr

tools = [tendr]

agent = create_react_agent(llm, tools)
```
