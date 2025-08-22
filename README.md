# Anime Chatbot

This repository contains a simple command-line chatbot that lets you talk with popular anime characters. Choose a character and the bot will reply in that character's style.

## Requirements

- Python 3.8+
- Optional: an [OpenAI API key](https://platform.openai.com/) in the `OPENAI_API_KEY` environment variable for more natural responses.

## Usage

```bash
python anime_chatbot.py
```

1. Pick a character from the list.
2. Start chatting!
3. Type `quit` to exit.

Without an OpenAI key, the bot runs in a simple offline mode and echoes back your messages in reverse.
