def MultimodalExpert(query, tools=None):
    """
    MultimodalExpert: A straightforward, multi-format AI expert like Gemini/ChatGPT.

    This function processes user queries with a direct, step-by-step approach,
    providing clear answers and generating various media formats as needed.

    Args:
        query (str): The user's question or request
        tools (list, optional): List of available tools ['web/fetch', 'search/codebase', 'agent']

    Returns:
        str: Direct response following the interaction style guidelines
    """

    # Available tools simulation
    available_tools = tools or ['web/fetch', 'search/codebase', 'agent']

    # Process the query based on type
    query_lower = query.lower()

    # Check for clarity - if vague, ask one targeted question
    # Allow simple greetings and common interactions
    if (len(query.split()) < 2 and not any(word in query_lower for word in ['explain', 'describe', 'what is', 'how to', 'why', 'hello', 'hi', 'hey', 'thanks', 'thank you'])) and '?' not in query:
        return "Please provide more specific details about what you need help with."

    # Direct answer first approach
    response_parts = []

    # Handle different types of requests
    if any(word in query_lower for word in ['document', 'pdf', 'report', 'guide']):
        response_parts.append("**Document Generation:**")
        response_parts.append("I'll create structured Markdown content suitable for PDF conversion.")
        response_parts.append("\n**Steps:**")
        response_parts.append("1. Analyze your requirements")
        response_parts.append("2. Structure content with clear headings")
        response_parts.append("3. Add formatting for professional appearance")
        response_parts.append("4. Provide conversion-ready Markdown")

    elif any(word in query_lower for word in ['image', 'visual', 'picture', 'svg', 'photo', 'drawing']):
        response_parts.append("**Image Generation:**")
        response_parts.append("Here's your generated image content:")
        response_parts.append("")

        # Generate actual SVG code for simple images
        if any(word in query_lower for word in ['robot', 'android', 'machine']):
            response_parts.append("**SVG Code for Robot Image:**")
            response_parts.append("```svg")
            response_parts.append('<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">')
            response_parts.append('  <rect x="50" y="50" width="100" height="100" fill="#4A90E2" stroke="#333" stroke-width="2"/>')
            response_parts.append('  <circle cx="75" cy="75" r="10" fill="#333"/>')
            response_parts.append('  <circle cx="125" cy="75" r="10" fill="#333"/>')
            response_parts.append('  <rect x="70" y="100" width="60" height="30" fill="#666"/>')
            response_parts.append('  <text x="100" y="180" text-anchor="middle" fill="#333" font-family="Arial" font-size="12">🤖 Robot</text>')
            response_parts.append('</svg>')
            response_parts.append("```")

        elif any(word in query_lower for word in ['sunset', 'sun', 'sky']):
            response_parts.append("**SVG Code for Sunset Image:**")
            response_parts.append("```svg")
            response_parts.append('<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">')
            response_parts.append('  <defs>')
            response_parts.append('    <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">')
            response_parts.append('      <stop offset="0%" style="stop-color:#FF6B35;stop-opacity:1" />')
            response_parts.append('      <stop offset="50%" style="stop-color:#F7931E;stop-opacity:1" />')
            response_parts.append('      <stop offset="100%" style="stop-color:#FFD23F;stop-opacity:1" />')
            response_parts.append('    </linearGradient>')
            response_parts.append('  </defs>')
            response_parts.append('  <rect width="300" height="200" fill="url(#skyGradient)"/>')
            response_parts.append('  <circle cx="150" cy="80" r="30" fill="#FFD23F" opacity="0.8"/>')
            response_parts.append('  <path d="M 0 150 Q 75 120 150 150 T 300 150 L 300 200 L 0 200 Z" fill="#8B4513"/>')
        elif any(word in query_lower for word in ['cat', 'kitten', 'feline']):
            response_parts.append("**SVG Code for Cat Image:**")
            response_parts.append("```svg")
            response_parts.append('<svg width="200" height="150" xmlns="http://www.w3.org/2000/svg">')
            response_parts.append('  <!-- Cat body -->')
            response_parts.append('  <ellipse cx="100" cy="100" rx="40" ry="30" fill="#FFA500"/>')
            response_parts.append('  <!-- Cat head -->')
            response_parts.append('  <circle cx="100" cy="60" r="25" fill="#FFA500"/>')
            response_parts.append('  <!-- Cat ears -->')
            response_parts.append('  <polygon points="85,45 90,25 95,45" fill="#FFA500"/>')
            response_parts.append('  <polygon points="105,45 110,25 115,45" fill="#FFA500"/>')
            response_parts.append('  <!-- Cat eyes -->')
            response_parts.append('  <circle cx="92" cy="55" r="3" fill="#000"/>')
            response_parts.append('  <circle cx="108" cy="55" r="3" fill="#000"/>')
            response_parts.append('  <!-- Cat nose -->')
            response_parts.append('  <polygon points="98,65 102,65 100,70" fill="#000"/>')
            response_parts.append('  <!-- Cat mouth -->')
            response_parts.append('  <path d="M 100 70 Q 95 75 90 70" stroke="#000" stroke-width="1" fill="none"/>')
            response_parts.append('  <path d="M 100 70 Q 105 75 110 70" stroke="#000" stroke-width="1" fill="none"/>')
            response_parts.append('  <!-- Cat tail -->')
            response_parts.append('  <path d="M 140 100 Q 160 80 155 100" stroke="#FFA500" stroke-width="8" fill="none"/>')
            response_parts.append('  <text x="100" y="140" text-anchor="middle" fill="#333" font-family="Arial" font-size="12">🐱 Cat</text>')
            response_parts.append('</svg>')
            response_parts.append("```")

        elif any(word in query_lower for word in ['dog', 'puppy', 'canine']):
            response_parts.append("**SVG Code for Dog Image:**")
            response_parts.append("```svg")
            response_parts.append('<svg width="200" height="150" xmlns="http://www.w3.org/2000/svg">')
            response_parts.append('  <!-- Dog body -->')
            response_parts.append('  <ellipse cx="100" cy="100" rx="45" ry="25" fill="#8B4513"/>')
            response_parts.append('  <!-- Dog head -->')
            response_parts.append('  <circle cx="100" cy="60" r="30" fill="#8B4513"/>')
            response_parts.append('  <!-- Dog ears -->')
            response_parts.append('  <ellipse cx="80" cy="45" rx="8" ry="15" fill="#654321"/>')
            response_parts.append('  <ellipse cx="120" cy="45" rx="8" ry="15" fill="#654321"/>')
            response_parts.append('  <!-- Dog eyes -->')
            response_parts.append('  <circle cx="90" cy="55" r="3" fill="#000"/>')
            response_parts.append('  <circle cx="110" cy="55" r="3" fill="#000"/>')
            response_parts.append('  <!-- Dog nose -->')
            response_parts.append('  <ellipse cx="100" cy="70" rx="4" ry="3" fill="#000"/>')
            response_parts.append('  <!-- Dog tail -->')
            response_parts.append('  <path d="M 145 90 Q 165 70 160 90" stroke="#8B4513" stroke-width="6" fill="none"/>')
            response_parts.append('  <!-- Dog spots -->')
            response_parts.append('  <circle cx="85" cy="80" r="3" fill="#654321"/>')
            response_parts.append('  <circle cx="115" cy="85" r="2" fill="#654321"/>')
            response_parts.append('  <text x="100" y="140" text-anchor="middle" fill="#333" font-family="Arial" font-size="12">🐶 Dog</text>')
            response_parts.append('</svg>')
            response_parts.append("```")

        else:
            # For other images, provide detailed DALL-E style prompts
            response_parts.append("**Detailed DALL-E Prompt:**")
            response_parts.append(f'"{query.replace("generate an image of", "").replace("create an image of", "").strip()},')
            response_parts.append('highly detailed, professional digital art, sharp focus, vibrant colors,')
            response_parts.append('8k resolution, photorealistic, cinematic lighting, masterpiece, artstation"')
            response_parts.append("")
            response_parts.append("**Style Options:**")
            response_parts.append("• Realistic: photorealistic, hyperrealistic, detailed")
            response_parts.append("• Artistic: digital art, illustration, concept art")
            response_parts.append("• Cartoon: animated, stylized, colorful")
            response_parts.append("• Abstract: minimal, geometric, artistic interpretation")

        response_parts.append("")
        response_parts.append("**Usage:**")
        response_parts.append("• Copy SVG code into an HTML file to display")
        response_parts.append("• Use DALL-E prompt with image generation tools")
        response_parts.append("• Save as .svg file for vector graphics")

    elif any(word in query_lower for word in ['video', 'storyboard', 'film', 'movie']) and not any(word in query_lower for word in ['code', 'function', 'program', 'python', 'javascript']):
        response_parts.append("**Video Production:**")
        response_parts.append("I'll create detailed storyboards and scripts.")
        response_parts.append("\n**Steps:**")
        response_parts.append("1. Define video objectives and audience")
        response_parts.append("2. Create scene-by-scene storyboard")
        response_parts.append("3. Write production script with timing")
        response_parts.append("4. Specify visual and audio requirements")

    elif any(word in query_lower for word in ['code', 'program', 'function', 'script']):
        response_parts.append("**Code Generation:**")
        response_parts.append("I'll provide complete, production-ready code.")
        response_parts.append("\n**Steps:**")
        response_parts.append("1. Clarify requirements and constraints")
        response_parts.append("2. Design solution architecture")
        response_parts.append("3. Write clean, documented code")
        response_parts.append("4. Include usage examples and testing")

    else:
        # General query handling - ALWAYS provide meaningful answers
        response_parts.append("**Direct Answer:**")

        # Handle common questions with specific answers
        if 'what is machine learning' in query_lower:
            response_parts.append("Machine learning is a subset of AI where systems learn from data to make predictions without explicit programming.")
        elif 'what is deep learning' in query_lower:
            response_parts.append("Deep learning is a subset of machine learning using neural networks with multiple layers to process data and make predictions.")
        elif 'what is ai' in query_lower or 'what is artificial intelligence' in query_lower:
            response_parts.append("Artificial Intelligence is the simulation of human intelligence in machines designed to think and learn like humans.")
        elif 'what is neural network' in query_lower or 'what are neural networks' in query_lower:
            response_parts.append("Neural networks are computing systems inspired by biological neural networks, consisting of interconnected nodes that process and transmit information.")
        elif 'what is python' in query_lower:
            response_parts.append("Python is a high-level programming language known for its simplicity and readability, widely used for web development, data science, AI, and automation.")
        elif 'what is javascript' in query_lower:
            response_parts.append("JavaScript is a programming language primarily used for web development to create interactive websites and web applications.")
        elif 'how to install python' in query_lower:
            response_parts.append("Download Python from python.org, run the installer, and follow the setup wizard. Make sure to check 'Add Python to PATH' during installation.")
        elif 'how to learn programming' in query_lower:
            response_parts.append("Start with Python or JavaScript basics, practice daily with small projects, use online resources like freeCodeCamp, and build real applications.")
        elif 'what is the meaning of life' in query_lower:
            response_parts.append("42 (according to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy'). More seriously, it's a philosophical question - the answer depends on your perspective.")
        elif 'tell me a joke' in query_lower:
            response_parts.append("Why did the AI go to school? To improve its learning algorithm! 🤖📚")
        elif 'what time is it' in query_lower:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            response_parts.append(f"The current time is {current_time}.")
        elif 'what day is it' in query_lower or 'what date is it' in query_lower:
            from datetime import datetime
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            response_parts.append(f"Today is {current_date}.")
        elif 'hello' in query_lower or 'hi' in query_lower:
            response_parts.append("Hello! I'm MultimodalExpert, your AI assistant. How can I help you today?")
        elif 'thank you' in query_lower or 'thanks' in query_lower:
            response_parts.append("You're welcome! I'm here to help anytime.")
        elif 'how are you' in query_lower:
            response_parts.append("I'm functioning optimally, thank you for asking! Ready to assist with any questions or tasks.")
        elif 'what can you do' in query_lower:
            response_parts.append("I can help with AI/ML questions, code generation, document creation, image generation, video production, and general knowledge queries.")
        elif 'who created you' in query_lower:
            response_parts.append("I was created as a MultimodalExpert AI agent, designed to be helpful, straightforward, and capable of handling various types of requests.")
        else:
            # For any other input, provide a helpful response
            # Check if it's a question (contains question words or ends with ?)
            is_question = ('?' in query or any(word in query_lower for word in ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'can you', 'do you', 'is it', 'are you', 'tell me']))

            if is_question:
                response_parts.append(f"I understand you're asking about: '{query}'")
                response_parts.append("")
                response_parts.append("While I don't have specific information about this exact topic, I can help you:")
                response_parts.append("• Break down the question into smaller parts")
                response_parts.append("• Suggest related topics to explore")
                response_parts.append("• Provide general guidance on how to find the answer")
                response_parts.append("• Help you formulate better questions")
                response_parts.append("")
                response_parts.append("Could you provide more context or rephrase your question?")
            else:
                response_parts.append(f"I see you said: '{query}'")
                response_parts.append("")
                response_parts.append("I'm here to help! You can ask me about:")
                response_parts.append("• AI and machine learning concepts")
                response_parts.append("• Programming and code generation")
                response_parts.append("• Document and report creation")
                response_parts.append("• Image and video production")
                response_parts.append("• General knowledge questions")
                response_parts.append("")
                response_parts.append("What would you like to know or create?")

        # Use available tools if relevant
        if 'web/fetch' in available_tools and any(word in query_lower for word in ['search', 'find', 'lookup', 'latest', 'news']):
            response_parts.append("\nUsing web search to gather current information.")
        elif 'search/codebase' in available_tools and any(word in query_lower for word in ['code', 'file', 'project', 'function']):
            response_parts.append("\nSearching codebase for relevant code and files.")
        elif 'agent' in available_tools and any(word in query_lower for word in ['complex', 'multi-step', 'analysis', 'research']):
            response_parts.append("\nDelegating to specialized agent for complex tasks.")

        response_parts.append("\n**Approach:**")
        response_parts.append("1. Understand the core question")
        response_parts.append("2. Provide direct answer")
        response_parts.append("3. Break down complex parts step-by-step")
        response_parts.append("4. Offer additional context if needed")

    # Add rules reminder if complex
    if any(word in query_lower for word in ['complex', 'difficult', 'advanced', 'multiple']):
        response_parts.append("\n**Why this approach:** Complex tasks need clear structure to avoid confusion.")

    return "\n".join(response_parts)


# Example usage
if __name__ == "__main__":
    # Test the function with various queries
    test_queries = [
        "Create a report on AI trends",
        "Generate an image of a robot",
        "Make a video about programming",
        "Write a Python function",
        "What is machine learning?",
        "How to install Python packages?",
        "Search for the latest AI news",
        "Find code examples for neural networks"
    ]

    for query in test_queries:
        print(f"\nQuery: {query}")
        print(f"Response: {MultimodalExpert(query)}")
        print("-" * 50)