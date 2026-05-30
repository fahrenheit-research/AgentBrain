"""
Hermes Agent Provider for AgentBrain v2
Created by Fahrenheit Research
"""

from typing import Any, Dict, List, Optional
from datetime import datetime


class HermesAgentBrainProvider:
    """
    Memory provider adapter for Hermes Agent.
    Allows AgentBrain to be used via:
        hermes config set memory.provider agentbrain
    """

    def __init__(self, brain):
        self.brain = brain

    def store(self, content: str, metadata: Optional[Dict] = None) -> Dict:
        """Hermes-compatible store method."""
        entities = metadata.get("entities", []) if metadata else []
        timestamp = metadata.get("timestamp") if metadata else None
        if timestamp:
            timestamp = datetime.fromisoformat(timestamp)

        return self.brain.store(
            content=content,
            entities=entities,
            timestamp=timestamp
        )

    def recall(self, query: str, limit: int = 10, **kwargs) -> List[Dict]:
        """Hermes-compatible recall method."""
        return self.brain.recall(query=query, limit=limit, **kwargs)

    def get_stats(self) -> Dict:
        return {
            "entities": len(self.brain.entities),
            "relations": len(self.brain.relations),
            "tiers": len(set(self.brain.tier_assignments.values())),
        }