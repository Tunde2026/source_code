#!/usr/bin/env python3
"""
Interactive Test Script for MultimodalExpert AI Agent
Run this to ask questions directly to the AI agent.
"""

from ai import MultimodalExpert

def main():
    print("🤖 MultimodalExpert AI Agent - Interactive Test")
    print("=" * 55)
    print("Type your questions below. Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("👋 Goodbye! Thanks for testing the AI agent.")
                break

            if not user_input:
                continue

            print("\n🤖 MultimodalExpert:")
            response = MultimodalExpert(user_input)
            print(response)
            print("-" * 55)

        except KeyboardInterrupt:
            print("\n👋 Goodbye! Thanks for testing.")
            break
        except EOFError:
            print("\n👋 Goodbye! Thanks for testing.")
            break

if __name__ == "__main__":
    main()