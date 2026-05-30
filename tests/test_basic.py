from agentbrain import AgentBrain
from datetime import datetime


def test_basic_store_and_recall():
    brain = AgentBrain()
    brain.store("User likes coffee", entities=["User"])
    results = brain.recall("coffee")
    assert len(results) >= 1


def test_temporal_relation():
    brain = AgentBrain()
    now = datetime.utcnow()
    brain.store(
        "User worked at CompanyX",
        entities=["User", "CompanyX"],
        relations=[{"source_id": "User", "target_id": "CompanyX", "type": "worked_at"}],
        timestamp=now
    )
    results = brain.get_temporal_relations("User")
    assert len(results) >= 1