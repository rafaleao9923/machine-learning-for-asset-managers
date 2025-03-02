from typing import TypedDict, List, Optional
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    """State of the agent workflow"""
    messages: List[BaseMessage]
    data: dict
    metadata: Optional[dict]