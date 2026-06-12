#!/usr/bin/env python3
"""
Comprehensive Test Suite for MultimodalExpert AI Agent
This script runs all types of tests to ensure the AI agent works correctly.
"""

from ai import MultimodalExpert

def test_simple_questions():
    """Test simple direct-answer questions"""
    print("🧪 Testing Simple Questions")
    print("-" * 40)

    questions = [
        "What is AI?",
        "What is machine learning?",
        "What is deep learning?",
        "What is a neural network?"
    ]

    for q in questions:
        print(f"Q: {q}")
        print(f"A: {MultimodalExpert(q)}")
        print()

def test_code_generation():
    """Test code-related requests"""
    print("🧪 Testing Code Generation")
    print("-" * 40)

    questions = [
        "Write a Python function",
        "Create a simple Python script",
        "Generate JavaScript code for a calculator",
        "Write an algorithm for sorting"
    ]

    for q in questions:
        print(f"Q: {q}")
        print(f"A: {MultimodalExpert(q)}")
        print()

def test_document_generation():
    """Test document creation requests"""
    print("🧪 Testing Document Generation")
    print("-" * 40)

    questions = [
        "Create a report on AI trends",
        "Write a guide for beginners",
        "Generate a PDF document about Python"
    ]

    for q in questions:
        print(f"Q: {q}")
        print(f"A: {MultimodalExpert(q)}")
        print()

def test_media_generation():
    """Test image and video requests"""
    print("🧪 Testing Media Generation")
    print("-" * 40)

    questions = [
        "Generate an image of a robot",
        "Create a video about programming",
        "Make a visual diagram of AI concepts"
    ]

    for q in questions:
        print(f"Q: {q}")
        print(f"A: {MultimodalExpert(q)}")
        print()

def test_tools():
    """Test tool-enabled requests"""
    print("🧪 Testing Tool Integration")
    print("-" * 40)

    questions = [
        ("Search for the latest AI news", ['web/fetch']),
        ("Find code examples in the project", ['search/codebase']),
        ("Analyze complex data patterns", ['agent'])
    ]

    for q, tools in questions:
        print(f"Q: {q} (tools: {tools})")
        print(f"A: {MultimodalExpert(q, tools=tools)}")
        print()

def run_all_tests():
    """Run the complete test suite"""
    print("🤖 MultimodalExpert AI Agent - Complete Test Suite")
    print("=" * 60)
    print()

    test_simple_questions()
    test_code_generation()
    test_document_generation()
    test_media_generation()
    test_tools()

    print("✅ All tests completed!")
    print("\n💡 To run individual tests, use:")
    print("   python -m pytest test_ai_comprehensive.py::test_simple_questions -v")
    print("\n💡 To run interactively:")
    print("   python test_ai.py")

if __name__ == "__main__":
    run_all_tests()