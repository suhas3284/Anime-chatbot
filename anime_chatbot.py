import os
from typing import Dict

try:
    import openai
except Exception:
    openai = None

# Personality prompts for each character
CHARACTER_PROMPTS: Dict[str, str] = {
    "Naruto": (
        "You are Naruto Uzumaki from the Naruto series. "
        "You speak with enthusiasm and use phrases like 'Believe it!'."
    ),
    "Luffy": (
        "You are Monkey D. Luffy from One Piece. "
        "You are carefree, love meat, and dream of becoming Pirate King."
    ),
    "Goku": (
        "You are Goku from Dragon Ball. You are cheerful and always ready for a fight."
    ),
}

def generate_response(character: str, user_message: str) -> str:
    """Generate a chat response in the style of the chosen character."""
    persona = CHARACTER_PROMPTS[character]
    if openai and os.getenv("OPENAI_API_KEY"):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        messages = [
            {"role": "system", "content": persona},
            {"role": "user", "content": user_message},
        ]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return completion.choices[0].message["content"].strip()
    # Fallback offline mode: simple echo with persona prefix
    return f"{character} says: {user_message[::-1]}"

def main() -> None:
    print("Welcome to the Anime Chatbot!")
    print("Available characters:")
    for name in CHARACTER_PROMPTS:
        print(f"- {name}")
    character = ""
    while character not in CHARACTER_PROMPTS:
        character = input("Choose a character: ")
        if character not in CHARACTER_PROMPTS:
            print("Unknown character. Please choose again.")
    print(f"Chatting as {character}. Type 'quit' to exit.\n")
    while True:
        user_message = input("You: ")
        if user_message.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        response = generate_response(character, user_message)
        print(f"{character}: {response}\n")

if __name__ == "__main__":
    main()
