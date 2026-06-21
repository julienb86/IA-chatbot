import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # charge le .env automatiquement

client = Anthropic()  # lit ANTHROPIC_API_KEY depuis l'env
#faire le prompt system et le mettre en cache pour les prochains messages
#https://platform.claude.com/docs/en/build-with-claude/prompt-caching
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ],
)

print(message.content[0].text)