# Hussar - Simple Agentic Search Library

Hussar is a simple agentic search library that uses OpenRouter + Chroma to answer questions about text content. The system stores text in a vector database and uses an LLM to provide intelligent answers.

## Hussar Workflow
<img width="2765" height="1684" alt="Hussar Diagram" src="https://github.com/user-attachments/assets/3e22a1c3-5a85-43a7-bfb2-c81faa916418" />


## ⚠️ Work in Progress

**IMPORTANT**: This library is currently under active development. Components are being built incrementally, starting with the core search tools and ending with the LLM agent integration. The current implementation is a minimal working version for testing and development purposes.

## Development Roadmap

The library is being developed in the following order:

### Phase 1: Core Search Tools ✅ (In Progress)

- [x] Basic project structure
- [x] Semantic search engine (Chroma integration)
- [ ] Text search engine (keyword-based)
- [ ] Regex search engine (pattern matching)
- [ ] Web search engine (real-time information)

### Phase 2: Document Processing

- [ ] Document loader
- [ ] Text chunking and preprocessing
- [ ] Metadata extraction and management

### Phase 3: Context Management

- [ ] Context builder and synthesizer
- [ ] Memory system for conversation history
- [ ] Context evaluation engine

### Phase 4: LLM Agent Integration

- [ ] Central LLM agent implementation
- [ ] Query generation and refinement
- [ ] Iterative context gathering
- [ ] Response synthesis and evaluation

### Phase 5: Advanced Features

- [ ] Multiple LLM provider support
- [ ] Advanced search strategies
- [ ] Performance optimization
- [ ] Comprehensive testing suite

## Features

- **Simple Workflow**: OpenRouter + Chroma + Text input only
- **Vector Search**: Uses Chroma for semantic search
- **LLM Integration**: OpenRouter for accessing various models
- **Easy to Use**: Simple API with just two main methods

## Quick Start

### 1. Installation

```bash
pip install hussar
```

### 2. Configuration

Copy the example environment file and add your OpenRouter API key:

```bash
cp .env.example .env
```

Edit `.env` with your API keys:

```bash
# Required: OpenRouter API key
HUSSAR_OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional: Chroma API key (uses local Chroma if not provided)
HUSSAR_CHROMA_API_KEY=your_chroma_api_key_here
```

### 3. Basic Usage

```python
from hussar import HussarAgent

# Initialize the agent
agent = HussarAgent()

# Add text content
text = "Python is a programming language. It was created by Guido van Rossum."
agent.add_text(text)

# Ask questions
answer = agent.query("Who created Python?")
print(answer)  # Guido van Rossum created Python.
```

## API Reference

### HussarAgent

The main class for interacting with Hussar.

#### `__init__(openrouter_api_key=None, chroma_api_key=None, model="openai/gpt-3.5-turbo")`

Initialize the agent.

- `openrouter_api_key`: OpenRouter API key (or set `HUSSAR_OPENROUTER_API_KEY` env var)
- `chroma_api_key`: Chroma API key (or set `HUSSAR_CHROMA_API_KEY` env var, optional)
- `model`: Model to use (e.g., "openai/gpt-3.5-turbo", "anthropic/claude-3-sonnet")

#### `add_text(text, metadata=None)`

Add text content to the vector database.

- `text`: The text content to add
- `metadata`: Optional metadata dictionary

#### `query(question, max_results=3)`

Ask a question about the loaded text.

- `question`: The question to ask
- `max_results`: Number of relevant chunks to use as context

## Examples

See `examples/simple_example.py` for a complete working example.

## Development

### Setup Development Environment

```bash
git clone https://github.com/hussar/hussar.git
cd hussar
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

## License

MIT License - see [LICENSE](LICENSE) for details.
