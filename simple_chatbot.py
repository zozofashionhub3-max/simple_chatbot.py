# simple_chatbot.py
# A simple chatbot that answers basic study-related questions
# Demonstrates: conditionals, loops, control statements, data types, and data structures

print("Hello! I’m EduBot 🤖 — your study helper chatbot!")
print("Ask me anything about studying, or type 'bye' to exit.\n")

responses = {
    "hello": "Hi there! How are you today?",
    "how are you": "I'm just a bot, but I'm here to help you study! 😊",
    "what is studying": "Studying is the process of learning and understanding new information.",
    "how to focus": "Try removing distractions, set short goals, and take breaks every 25 minutes (Pomodoro method).",
    "give motivation": "Believe in yourself! Every small step brings you closer to your goals. 🌟",
    "tips for exams": "Start early, review your notes, practice past papers, and get enough rest.",
    "thank you": "You're welcome! Keep learning. 📚",
}

while True:
    user_input = input("You: ").lower().strip()
    if user_input == "bye":
        print("EduBot: Goodbye! 👋 Stay motivated and keep studying!")
        break
    if user_input == "":
        print("EduBot: Please say something 🙂")
        continue
    if user_input in responses:
        print(f"EduBot: {responses[user_input]}")
    else:
        print("EduBot: Hmm, I don't know that yet. Try asking about studying or motivation!")
