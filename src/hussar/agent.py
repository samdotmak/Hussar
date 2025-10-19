"""
Hussar Agent - Simple OpenRouter + Chroma workflow.

This is the main class that users will interact with.
"""

import os
from typing import Optional, List, Dict, Any
from pathlib import Path

import chromadb


class Hussar:
    """
    A simple agent that uses OpenRouter + Chroma to evaluate questions about text.
    
    Workflow:
    1. Add text content to Chroma
    2. Search for relevant content using Chroma
    3. Use OpenRouter to answer questions based on found content
    """
    
    def __init__(
        self, 
        openrouter_api_key: Optional[str] = None, 
        collection_name: str = "default",
        storage_path: Optional[str] = None
    ):
        self.openrouter_api_key = openrouter_api_key or os.getenv("HUSSAR_OPENROUTER_API_KEY")
        self.collection_name = collection_name
        
        # Use visible hussar directory in user's home directory
        if storage_path is None:
            storage_path = str(Path.home() / "hussar" / "vectorstore")
        self.storage_path = storage_path
        
        # Use local persistent storage
        self.client = chromadb.PersistentClient(path=storage_path)
        
        # Get or create collection
        try:
            self.collection = self.client.get_collection(name=collection_name)
        except:
            self.collection = self.client.create_collection(name=collection_name)
    
    
    def ingest(self, text: str):
        print(f"hello world!")
        pass


if __name__ == "__main__":
    # Quick test
    agent = Hussar()
    agent.ingest("This is a test document about Python programming.")
    print("Text ingested successfully!")