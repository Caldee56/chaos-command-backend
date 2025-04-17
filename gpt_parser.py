import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_with_gpt(message: str) -> dict:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You're an AI agent that converts chaotic input into structured commands. Respond in JSON like: {\"command\": \"ALERT\", \"reason\": \"...\"}"},
                {"role": "user", "content": message}
            ]
        )
        content = response['choices'][0]['message']['content']
        return json.loads(content)
    except Exception as e:
        return {"command": "ERROR", "reason": str(e)}

def execute_command(parsed: dict):
    command = parsed.get("command", "UNKNOWN")
    reason = parsed.get("reason", "No reason given")
    print(f"[ACTION] {command}: {reason}")
