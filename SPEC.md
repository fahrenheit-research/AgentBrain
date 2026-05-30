# AgentBrain v2 — Technical Specification

**Version**: 2.0  
**Maintainer**: Fahrenheit Research  
**License**: MIT

## 1. Vision

AgentBrain v2 is a production-grade, open-source memory system for LLM agents that combines:

- Structured entity memory
- Temporal relationship tracking
- Hierarchical memory management
- Intelligent background synthesis

It is designed to be the default memory layer for serious agent developers while remaining simple to use.

## 2. Core Principles

- **Original Design** — Inspired by research (Zep, MemGPT) but implemented originally
- **Hermes First** — Native integration with Hermes Agent
- **Observable** — Excellent Obsidian export and debugging tools
- **Benchmarkable** — Every major feature has reproducible benchmarks
- **Production Ready** — Low latency, conflict-safe, provenance tracking

## 3. Architecture

### 3.1 Data Model

**Entity**
- `id`, `type`, `name`, `attributes`, timestamps, `confidence`, `source_count`

**Relation** (Temporal)
- `source_id`, `target_id`, `type`
- `valid_from`, `valid_to` (None = still valid)
- `confidence`, `source_message_ids`

### 3.2 Memory Tiers

| Tier       | Purpose                        | Retention     | Retrieval Priority |
|------------|--------------------------------|---------------|--------------------|
| Working    | Current context window         | Short         | Highest            |
| Episodic   | Recent sessions                | Medium        | High               |
| Semantic   | Long-term structured knowledge | Long          | Medium             |
| Archive    | Compressed historical facts    | Very Long     | Low                |

### 3.3 Key Components

- **Core** (`core.py`): Main `AgentBrain` class
- **Synthesis Engine** (`synthesis.py`): Entity merging, conflict resolution, abstraction
- **Hermes Provider** (`hermes_provider.py`): Adapter for Hermes Agent
- **Exporters** (`exporters.py`): Obsidian, JSON, etc.

## 4. API Surface

```python
brain = AgentBrain()

# Storage
brain.store(content, entities=[], relations=[], timestamp=None, tier="semantic")

# Retrieval
brain.recall(query, limit=10, time_range=None, tier=None)

# Temporal
brain.get_temporal_relations(entity_id, at_time=None)

# Synthesis
brain.synthesize()

# Export
brain.export_to_obsidian(path)
```

## 5. Benchmarks (Required)

- `temporal_retrieval`
- `entity_resolution`
- `synthesis_quality`
- `long_horizon_agent`

All benchmarks must be reproducible and documented.

## 6. Hermes Integration

```bash
hermes config set memory.provider agentbrain
```

The provider implements `store()`, `recall()`, and `get_stats()`.

## 7. Open Source Goals

- High-quality documentation
- Clean, modern Python
- Strong test coverage
- Public benchmark leaderboard
- Active maintenance by Fahrenheit Research

---

**Created by Fahrenheit Research**