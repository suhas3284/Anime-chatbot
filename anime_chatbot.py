import os
from typing import Dict, List

try:
    from groq import Groq
except Exception:
    Groq = None

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
    "Saitama": (
        "You are Saitama from One Punch Man. You speak casually and are often bored unless there's a worthy opponent.",
    ),
    "Deku": (
        "You are Izuku Midoriya from My Hero Academia. You're earnest, analytical, and always striving to be a great hero.",
    ),
}


def create_client():
    """Instantiate a Groq client if the API key is available."""
    if Groq and os.getenv("GROQ_API_KEY"):
        return Groq(api_key=os.environ["GROQ_API_KEY"])
    return None


def generate_response(client: "Groq", messages: List[Dict[str, str]]) -> str:
    """Generate a chat response using the Groq client or fall back to offline mode."""
    if client:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages,
        )
        return completion.choices[0].message["content"].strip()
    # Offline mode
    last_user = messages[-1]["content"]
    return last_user[::-1]


def main() -> None:
    print("Welcome to the Anime Chatbot!")
    print("Available characters:")
    for name in CHARACTER_PROMPTS:
        print(f"- {name}")

    character = ""
    while character not in CHARACTER_PROMPTS:
        character = input("Choose a character: ").strip().title()
        if character not in CHARACTER_PROMPTS:
            print("Unknown character. Please choose again.")

    client = create_client()
    persona = CHARACTER_PROMPTS[character]
    messages: List[Dict[str, str]] = [{"role": "system", "content": persona}]

    print(f"Chatting as {character}. Type 'quit' to exit.\n")
    while True:
        user_message = input("You: ")
        if user_message.lower() in {"quit", "exit"}:
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": user_message})
        response = generate_response(client, messages)
        messages.append({"role": "assistant", "content": response})
        print(f"{character}: {response}\n")


if __name__ == "__main__":
    main()
