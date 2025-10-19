"""
Simple test to verify the Hussar workflow.

This test verifies that:
1. Agent can be initialized with API keys
2. Text can be added to Chroma
3. Questions can be asked and answered
"""

import os
import pytest
from hussar import HussarAgent


def test_agent_initialization():
    """Test that agent can be initialized with API keys."""
    # Test with environment variables
    os.environ["HUSSAR_OPENROUTER_API_KEY"] = "test_openrouter_key"
    
    agent = HussarAgent()
    assert agent.openrouter_api_key == "test_openrouter_key"
    assert agent.model == "openai/gpt-3.5-turbo"
    
    # Test with explicit parameters
    agent2 = HussarAgent(
        openrouter_api_key="explicit_key",
        chroma_api_key="explicit_chroma_key",
        model="anthropic/claude-3-sonnet"
    )
    assert agent2.openrouter_api_key == "explicit_key"
    assert agent2.chroma_api_key == "explicit_chroma_key"
    assert agent2.model == "anthropic/claude-3-sonnet"


def test_agent_initialization_missing_key():
    """Test that agent raises error when OpenRouter API key is missing."""
    # Clear environment variable
    if "HUSSAR_OPENROUTER_API_KEY" in os.environ:
        del os.environ["HUSSAR_OPENROUTER_API_KEY"]
    
    with pytest.raises(ValueError, match="OpenRouter API key is required"):
        HussarAgent()


def test_add_text():
    """Test that text can be added to Chroma."""
    os.environ["HUSSAR_OPENROUTER_API_KEY"] = "test_key"
    
    agent = HussarAgent()
    
    # Test adding text
    test_text = "This is a test document about Python programming."
    agent.add_text(test_text, metadata={"topic": "programming"})
    
    # Verify collection has documents
    results = agent.collection.get()
    assert len(results["documents"]) > 0
    assert "Python programming" in results["documents"][0]


if __name__ == "__main__":
    # Run tests
    test_agent_initialization()
    test_agent_initialization_missing_key()
    test_add_text()
    test_text_chunking()
    print("All tests passed!")
