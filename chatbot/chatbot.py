"""
CodSoft AI Internship - Task 1
Rule Based Chatbot
Author: Goush Shaik
"""

from datetime import datetime

print("=" * 50)
print("        Welcome to CodBot")
print("      CodSoft AI Internship")
print("=" * 50)

name = input("Bot: What should I call you? ")

print(f"\nBot: Nice to meet you, {name}!\n How can I help you?")
print("Bot: Type 'help' to see available commands.")
print("Bot: Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print(f"Bot: Hello {name}!")

    elif user == "help":
        print("""
Available Commands

Greetings:
- hi
- hello
- hey

Information:
- what is your name
- who created you

AI & Programming:
- what is ai
- what is machine learning
- what is python

Conversation:
- how are you
- good
- fine

Motivation:
- motivate me
- study tips

Fun:
- tell me a joke

Utility:
- time

Calculator for two numbers like:
- add  10 20
- subtract 20 10
- multiply 5 6
- divide 100 5

Other:
- help
- bye
""")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking.")
        print("Bot: What about you?")

    elif user in ["good", "i am fine", "fine", "great", "awesome"]:
        print(f"Bot: That's great, {name}! Keep learning and keep growing.")

    elif user == "what is your name":
        print("Bot: My name is CodBot.")

    elif user == "who created you":
        print("Bot: I was created by Goush Shaik for the CodSoft AI Internship.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It helps machines perform tasks that normally require human intelligence.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI that allows computers to learn from data.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used in AI, Machine Learning, Web Development and more.")

    elif user == "motivate me":
        print("Bot: Every expert was once a beginner. Keep learning and never give up.")

    elif user == "study tips":
        print("Bot: Practice daily, build projects, and learn by doing.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs.")

    elif user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    elif user.startswith("add "):
        numbers = user.split()

        if len(numbers) == 3:
            result = float(numbers[1]) + float(numbers[2])
            print("Bot: Result =", result)
        else:
            print("Bot: Usage -> add 10 20")

    elif user.startswith("subtract "):
        numbers = user.split()

        if len(numbers) == 3:
            result = float(numbers[1]) - float(numbers[2])
            print("Bot: Result =", result)
        else:
            print("Bot: Usage -> subtract 20 10")

    elif user.startswith("multiply "):
        numbers = user.split()

        if len(numbers) == 3:
            result = float(numbers[1]) * float(numbers[2])
            print("Bot: Result =", result)
        else:
            print("Bot: Usage -> multiply 5 6")

    elif user.startswith("divide "):
        numbers = user.split()

        if len(numbers) == 3:

            if float(numbers[2]) != 0:
                result = float(numbers[1]) / float(numbers[2])
                print("Bot: Result =", result)
            else:
                print("Bot: Cannot divide by zero.")

        else:
            print("Bot: Usage -> divide 100 5")

    elif user == "bye":
        print(f"Bot: Goodbye {name}!")
        break

    else:
        print("Bot: I don't understand that yet. I'm still learning.")
        print("Bot: Type 'help' to see available commands.")