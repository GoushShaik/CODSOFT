"""
CodSoft AI Internship - Task 4
Scoring-Based Recommendation System
Author: Goush Shaik
"""

import random

print("=" * 60)
print("        SCORING BASED RECOMMENDATION SYSTEM")
print("        CodSoft AI Internship Task 4")
print("=" * 60)

name = input("\nEnter your name: ")

print(f"\nWelcome {name}")
print("This system learns your preferences and recommends items accordingly.")

recommendations = {
    "movies": {
        "action": ["John Wick", "Avengers", "The Dark Knight", "Mad Max"],
        "comedy": ["Home Alone", "Jumanji", "Mr. Bean", "The Mask"],
        "drama": ["Forrest Gump", "Titanic", "The Shawshank Redemption"]
    },

    "books": {
        "horror": ["Dracula", "IT", "The Shining"],
        "fiction": ["Harry Potter", "The Hobbit", "The Alchemist"],
        "self_help": ["Atomic Habits", "Ikigai", "Rich Dad Poor Dad"]
    },

    "music": {
        "pop": ["Blinding Lights", "Shape of You", "Levitating"],
        "rock": ["Numb", "Believer", "In The End"]
    },

    "games": {
        "action": ["GTA V", "God of War", "Red Dead Redemption 2"],
        "sports": ["FIFA 25", "Cricket 24", "NBA 2K"]
    }
}

# Preference tracking
history = []
scores = {}

def update_score(category, genre):
    key = f"{category}-{genre}"
    scores[key] = scores.get(key, 0) + 1

while True:

    print("\nAvailable Categories:")
    print("1. Movies")
    print("2. Books")
    print("3. Music")
    print("4. Games")
    print("5. Exit")

    choice = input("\nEnter category: ").lower()

    if choice == "1":
        category = "movies"
    elif choice == "2":
        category = "books"
    elif choice == "3":
        category = "music"
    elif choice == "4":
        category = "games"
    elif choice == "5":
        print(f"\nGoodbye {name}. Thanks for using the system.")
        break
    else:
        print("Invalid choice. Try again.")
        continue

    print("\nAvailable genres:", ", ".join(recommendations[category].keys()))

    genre = input("Enter genre (or type 'surprise'): ").lower()

    if genre == "surprise":
        genre = random.choice(list(recommendations[category].keys()))
        print("Surprise genre selected:", genre)

    if genre not in recommendations[category]:
        print("Genre not found.")
        continue

    # Update tracking
    history.append(f"{category}-{genre}")
    update_score(category, genre)

    print("\nRecommended Items:")
    items = recommendations[category][genre]

    for item in items:
        print("-", item)

    print("\nTop suggestion:")
    print(random.choice(items))

    # Personalized insight after some usage
    if len(history) >= 2:
        print("\nBased on your activity:")

        most_used = max(scores, key=scores.get)
        cat, gen = most_used.split("-")

        print(f"You seem to prefer {gen} in {cat}.")

    again = input("\nDo you want another recommendation? (yes/no): ").lower()

    if again != "yes":
        print(f"\nSession ended. Goodbye {name}.")
        break