#!/usr/bin/env python3
"""
Web Chat Interface for MultimodalExpert AI Agent
Run this to start a web server and chat with the AI through a browser.
"""

from flask import Flask, render_template_string, request
from flask.json import jsonify
from ai import MultimodalExpert
import json

app = Flask(__name__)

# HTML template for the chat interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 MultimodalExpert AI Chat</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .chat-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 800px;
            height: 80vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
        }

        .chat-messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background: #f8f9fa;
        }

        .message {
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 15px;
            max-width: 70%;
            animation: fadeIn 0.3s ease-in;
        }

        .message.user {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: auto;
            text-align: right;
        }

        .message.ai {
            background: white;
            border: 1px solid #e9ecef;
            color: #333;
        }

        .message-header {
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 0.9em;
        }

        .message-content {
            line-height: 1.4;
        }

        .chat-input-area {
            padding: 20px;
            background: white;
            border-top: 1px solid #e9ecef;
            display: flex;
            gap: 10px;
        }

        #message-input {
            flex: 1;
            padding: 15px;
            border: 2px solid #e9ecef;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s ease;
        }

        #message-input:focus {
            border-color: #667eea;
        }

        #send-button {
            padding: 15px 25px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            transition: transform 0.2s ease;
        }

        #send-button:hover {
            transform: translateY(-2px);
        }

        #send-button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .typing-indicator {
            display: none;
            padding: 15px;
            color: #666;
            font-style: italic;
        }

        .typing-indicator.show {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .help-button {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.2);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
        }

        .help-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .help-content {
            background: white;
            padding: 30px;
            border-radius: 15px;
            max-width: 500px;
            width: 90%;
            text-align: center;
        }

        .help-content h3 {
            margin-bottom: 15px;
            color: #333;
        }

        .help-content ul {
            text-align: left;
            margin: 15px 0;
        }

        .help-content li {
            margin-bottom: 8px;
        }

        .close-help {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <button class="help-button" onclick="showHelp()">Help</button>

    <div class="chat-container">
        <div class="chat-header">
            🤖 MultimodalExpert AI Agent
        </div>

        <div class="chat-messages" id="chat-messages">
            <div class="message ai">
                <div class="message-header">🤖 MultimodalExpert</div>
                <div class="message-content">
                    Hello! I'm your MultimodalExpert AI assistant. I can help you with:
                    <br>• AI and Machine Learning questions
                    <br>• Code generation and programming
                    <br>• Document and report creation
                    <br>• Image and video production ideas
                    <br><br>Ask me anything! 🚀
                </div>
            </div>
        </div>

        <div class="typing-indicator" id="typing-indicator">
            🤖 MultimodalExpert is thinking...
        </div>

        <div class="chat-input-area">
            <input type="text" id="message-input" placeholder="Type your message here..." onkeypress="handleKeyPress(event)">
            <button id="send-button" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <div class="help-modal" id="help-modal">
        <div class="help-content">
            <h3>💡 How to Use MultimodalExpert</h3>
            <ul>
                <li><strong>Simple Questions:</strong> "What is AI?" or "What is machine learning?"</li>
                <li><strong>Code Requests:</strong> "Write a Python function" or "Create a JavaScript calculator"</li>
                <li><strong>Documents:</strong> "Create a report on AI trends" or "Write a guide for beginners"</li>
                <li><strong>Media:</strong> "Generate an image of a robot" or "Create a video storyboard"</li>
                <li><strong>Tools:</strong> "Search for latest AI news" (uses web tools)</li>
            </ul>
            <p><strong>Features:</strong></p>
            <ul>
                <li>Direct answers first</li>
                <li>Step-by-step explanations</li>
                <li>Multi-format support</li>
                <li>Tool integration ready</li>
            </ul>
            <button class="close-help" onclick="hideHelp()">Got it!</button>
        </div>
    </div>

    <script>
        let conversationHistory = [];

        function addMessage(content, isUser = false) {
            const messagesDiv = document.getElementById('chat-messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'ai'}`;

            const header = document.createElement('div');
            header.className = 'message-header';
            header.textContent = isUser ? 'You' : '🤖 MultimodalExpert';

            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.innerHTML = content.replace(/\\n/g, '<br>');

            messageDiv.appendChild(header);
            messageDiv.appendChild(contentDiv);
            messagesDiv.appendChild(messageDiv);

            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        function showTyping() {
            document.getElementById('typing-indicator').classList.add('show');
        }

        function hideTyping() {
            document.getElementById('typing-indicator').classList.remove('show');
        }

        async function sendMessage() {
            const input = document.getElementById('message-input');
            const message = input.value.trim();

            if (!message) return;

            // Add user message
            addMessage(message, true);
            conversationHistory.push({role: 'user', content: message});

            // Clear input
            input.value = '';

            // Show typing indicator
            showTyping();

            // Disable send button
            const sendButton = document.getElementById('send-button');
            sendButton.disabled = true;

            try {
                // Send to server
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });

                const data = await response.json();

                // Hide typing indicator
                hideTyping();

                // Add AI response
                addMessage(data.response);
                conversationHistory.push({role: 'assistant', content: data.response});

            } catch (error) {
                hideTyping();
                addMessage('❌ Sorry, there was an error processing your message. Please try again.');
                console.error('Error:', error);
            }

            // Re-enable send button
            sendButton.disabled = false;
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        function showHelp() {
            document.getElementById('help-modal').style.display = 'flex';
        }

        function hideHelp() {
            document.getElementById('help-modal').style.display = 'none';
        }

        // Focus on input when page loads
        window.onload = function() {
            document.getElementById('message-input').focus();
        };
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Serve the main chat interface"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        # Get AI response
        ai_response = MultimodalExpert(user_message)

        return jsonify({'response': ai_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def start_web_chat():
    """Start the web chat server"""
    print("🤖 Starting MultimodalExpert Web Chat Server...")
    print("=" * 50)
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("❌ Press Ctrl+C to stop the server")
    print("=" * 50)

    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Web server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")

if __name__ == "__main__":
    start_web_chat()