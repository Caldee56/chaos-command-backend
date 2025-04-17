# Chaos-to-Command API

This backend listens to chaos, processes it through GPT, and executes intelligent commands.

## How It Works
1. Send POST to `/chaos` with a JSON body:
```json
{ "message": "Everything is crashing in sector 4A" }
```

2. GPT returns structured action:
```json
{ "command": "ALERT", "reason": "System outage detected" }
```

3. System executes response silently (logs, alerts, etc.)

## Deploy Instructions (Railway)
- Fork or upload this repo
- Go to https://railway.app
- New Project > GitHub Repo
- Set environment variable: `OPENAI_API_KEY`
- Done

## Local Dev
```bash
pip install -r requirements.txt
python app.py
```