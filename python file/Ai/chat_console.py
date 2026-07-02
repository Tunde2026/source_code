#!/usr/bin/env python3
"""
Console Chat Interface for MultimodalExpert AI Agent
Run this to chat with the AI directly in the terminal.
"""

from ai import MultimodalExpert

def start_console_chat():
    """Start an interactive console chat with the AI agent"""
    print("🤖 MultimodalExpert AI Agent - Console Chat")
    print("=" * 50)
    print("Type your questions below. Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("Type 'help' for available commands.\n")

    conversation_history = []

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("\n👋 Goodbye! Thanks for chatting with MultimodalExpert.")
                break

            if user_input.lower() in ['help', 'h', '?']:
                show_help()
                continue

            if user_input.lower() == 'history':
                show_history(conversation_history)
                continue

            if user_input.lower() == 'clear':
                conversation_history.clear()
                print("🧹 Conversation history cleared.")
                continue

            if not user_input:
                continue

            # Get AI response
            print("\n🤖 MultimodalExpert:")
            response = MultimodalExpert(user_input)

            # Display response
            print(response)

            # Store in history
            conversation_history.append({
                'user': user_input,
                'ai': response,
                'timestamp': __import__('datetime').datetime.now().strftime("%H:%M:%S")
            })

            print("-" * 50)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for chatting.")
            break
        except EOFError:
            print("\n👋 Goodbye! Thanks for chatting.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.\n")

def show_help():
    """Display available commands"""
    print("\n📋 Available Commands:")
    print("  help     - Show this help message")
    print("  history  - Show conversation history")
    print("  clear    - Clear conversation history")
    print("  quit     - Exit the chat")
    print("\n💡 Ask me anything about:")
    print("  • AI and Machine Learning concepts")
    print("  • Code generation and programming")
    print("  • Document and report creation")
    print("  • Image and video production")
    print("  • General questions and tasks\n")

def show_history(history):
    """Display conversation history"""
    if not history:
        print("📝 No conversation history yet.")
        return

    print(f"\n📝 Conversation History ({len(history)} messages):")
    print("-" * 50)

    for i, msg in enumerate(history, 1):
        print(f"{i}. [{msg['timestamp']}] You: {msg['user']}")
        print(f"   🤖 AI: {msg['ai'][:100]}{'...' if len(msg['ai']) > 100 else ''}")
        print()

if __name__ == "__main__":
    start_console_chat()