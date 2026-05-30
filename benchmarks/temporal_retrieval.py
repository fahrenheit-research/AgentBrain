"""
Temporal Retrieval Benchmark for AgentBrain v2
Created by Fahrenheit Research
"""

from agentbrain import AgentBrain
from datetime import datetime, timedelta
import time


def run_temporal_benchmark():
    brain = AgentBrain()

    # Seed data with temporal relations
    now = datetime.utcnow()
    brain.store(
        "Alice joined as Engineer",
        entities=["Alice", "Engineering Team"],
        relations=[{"source_id": "Alice", "target_id": "Engineering Team", "type": "member_of"}],
        timestamp=now - timedelta(days=400)
    )

    brain.store(
        "Alice was promoted to Staff Engineer",
        entities=["Alice"],
        relations=[{"source_id": "Alice", "target_id": "Engineering Team", "type": "promoted_to"}],
        timestamp=now - timedelta(days=120)
    )

    # Query at different times
    results_2024 = brain.recall("Alice", time_range=(now - timedelta(days=500), now - timedelta(days=200)))
    results_2025 = brain.recall("Alice", time_range=(now - timedelta(days=200), now))

    print("Temporal Retrieval Benchmark Results:")
    print(f"  2024 records: {len(results_2024)}")
    print(f"  2025 records: {len(results_2025)}")
    return {"2024": len(results_2024), "2025": len(results_2025)}


if __name__ == "__main__":
    run_temporal_benchmark()