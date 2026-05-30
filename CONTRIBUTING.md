# Contributing to AgentBrain

Thank you for your interest in contributing to AgentBrain!

## Code of Conduct

Be respectful, constructive, and focused on building the best agent memory system possible.

## How to Contribute

### Reporting Issues
- Use GitHub Issues
- Include reproduction steps, expected vs actual behavior
- Add relevant logs or benchmark output when possible

### Pull Requests
1. Fork the repository
2. Create a feature branch (`feat/temporal-indexing`)
3. Make focused, well-tested changes
4. Update documentation if needed
5. Submit a PR with a clear description

### Development Setup

```bash
git clone https://github.com/fahrenheit-research/AgentBrain
cd AgentBrain
pip install -e ".[dev]"
pytest
```

### Coding Standards

- Use type hints
- Keep functions focused and small
- Add docstrings for public methods
- Write tests for new features
- Run `ruff` and `black` before committing

### Areas Where Help is Welcome

- Better semantic retrieval (embeddings)
- Synthesis engine improvements
- New exporters (Notion, Markdown graph, etc.)
- Benchmark expansion
- Performance optimizations

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Maintained by Fahrenheit Research**