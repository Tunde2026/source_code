#!/usr/bin/env python3
"""
Example usage of MultimodalExpert AI Agent
"""

from ai import MultimodalExpert

def main():
    print("🤖 MultimodalExpert AI Agent Examples")
    print("=" * 50)

    # Example 1: Simple question
    print("\n1. Simple Question:")
    query1 = "What is machine learning?"
    response1 = MultimodalExpert(query1)
    print(f"Q: {query1}")
    print(f"A: {response1}")

    # Example 2: Code generation request
    print("\n2. Code Generation Request:")
    query2 = "Write a Python function to calculate factorial"
    response2 = MultimodalExpert(query2)
    print(f"Q: {query2}")
    print(f"A: {response2}")

    # Example 3: Document creation
    print("\n3. Document Creation Request:")
    query3 = "Create a report on AI trends"
    response3 = MultimodalExpert(query3)
    print(f"Q: {query3}")
    print(f"A: {response3}")

    # Example 4: Using tools
    print("\n4. Tool-Enabled Request:")
    query4 = "Search for the latest AI news"
    response4 = MultimodalExpert(query4, tools=['web/fetch', 'search/codebase', 'agent'])
    print(f"Q: {query4}")
    print(f"A: {response4}")

if __name__ == "__main__":
    main()