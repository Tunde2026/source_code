#!/usr/bin/env python3
"""
Launcher for MultimodalExpert AI Chat Interfaces
Choose between console chat, web interface, or demo HTML.
"""

import sys
import os

def show_menu():
    """Display the main menu"""
    print("🤖 MultimodalExpert AI Agent - Interface Launcher")
    print("=" * 55)
    print("Choose how you want to chat with the AI:")
    print()
    print("1. 🖥️  Console Chat (Terminal)")
    print("   - Interactive chat in your terminal")
    print("   - Commands: help, history, clear, quit")
    print()
    print("2. 🌐 Web Interface (Browser)")
    print("   - Modern web chat interface")
    print("   - Runs on http://localhost:5000")
    print("   - Requires Flask (already installed)")
    print()
    print("3. 📄 HTML Demo (Browser)")
    print("   - Static HTML with sample responses")
    print("   - No server required - just open in browser")
    print()
    print("4. 🧪 Run Tests")
    print("   - Comprehensive test suite")
    print("   - Verify all AI functions work")
    print()
    print("5. ❌ Exit")
    print()

def launch_console():
    """Launch the console chat interface"""
    print("🚀 Starting Console Chat...")
    print("Type 'quit' to exit, 'help' for commands.")
    print("-" * 40)

    try:
        from chat_console import start_console_chat
        start_console_chat()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("Make sure chat_console.py is in the same directory.")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

def launch_web():
    """Launch the web interface"""
    print("🚀 Starting Web Interface...")
    print("🌐 Open your browser to: http://localhost:5000")
    print("❌ Press Ctrl+C to stop the server")
    print("-" * 40)

    try:
        from chat_web import start_web_chat
        start_web_chat()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("Make sure chat_web.py is in the same directory.")
        print("Also ensure Flask is installed: pip install flask")
    except Exception as e:
        print(f"❌ Error starting web server: {e}")

def launch_html_demo():
    """Launch the HTML demo"""
    html_path = os.path.join(os.path.dirname(__file__), 'chat_demo.html')

    if os.path.exists(html_path):
        print("🚀 Opening HTML Demo...")
        print(f"📄 File: {html_path}")
        print("🌐 Opening in your default browser...")
        print("-" * 40)

        # Try to open in browser
        import webbrowser
        webbrowser.open(f'file://{html_path}')

        print("✅ HTML demo opened in browser!")
        print("💡 This is a static demo with sample responses.")
        print("💡 For full AI functionality, use option 2 (Web Interface).")
    else:
        print(f"❌ Error: HTML demo file not found at {html_path}")

def run_tests():
    """Run the comprehensive test suite"""
    print("🧪 Running Comprehensive Test Suite...")
    print("-" * 40)

    try:
        from test_ai_comprehensive import run_all_tests
        run_all_tests()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("Make sure test_ai_comprehensive.py is in the same directory.")

def main():
    """Main launcher function"""
    while True:
        show_menu()

        try:
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                launch_console()
                break
            elif choice == '2':
                launch_web()
                break
            elif choice == '3':
                launch_html_demo()
                input("\nPress Enter to return to menu...")
            elif choice == '4':
                run_tests()
                input("\nPress Enter to return to menu...")
            elif choice == '5':
                print("👋 Goodbye! Thanks for using MultimodalExpert.")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                input("Press Enter to continue...")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()