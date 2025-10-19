"""
Simple example of using Hussar.

This example shows how to:
1. Create a Hussar agent with API keys
2. Add text content to Chroma
3. Ask questions about the content
"""

import os
from hussar import HussarAgent

def main():
    # Initialize the agent
    # Make sure to set HUSSAR_OPENROUTER_API_KEY environment variable
    # Optionally set HUSSAR_CHROMA_API_KEY for Chroma Cloud
    agent = HussarAgent()
    
    # Add some text content
    text_content = """
    Python is a high-level programming language known for its simplicity and readability.
    It was created by Guido van Rossum and first released in 1991. Python supports multiple
    programming paradigms including procedural, object-oriented, and functional programming.
    
    Python is widely used in web development, data science, artificial intelligence,
    scientific computing, and automation. It has a large standard library and an active
    community that contributes to thousands of third-party packages.
    
    Some popular Python frameworks include Django and Flask for web development,
    NumPy and Pandas for data analysis, and TensorFlow and PyTorch for machine learning.
    """
    
    print("Adding text content...")
    agent.add_text(text_content, metadata={"topic": "Python programming"})
    
    # Ask questions about the content
    questions = [
        "What is Python?",
        "When was Python first released?",
        "What are some popular Python frameworks?",
        "What programming paradigms does Python support?"
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        answer = agent.query(question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
