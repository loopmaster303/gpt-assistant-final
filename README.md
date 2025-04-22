# GPT Assistant für Render.com

## 📦 Endpunkt
- `POST /assistant`
- JSON: `{ "prompt": "Was steht heute an?" }`

## 🚀 Deploy auf Render
1. Erstelle GitHub-Repo, lade alle Dateien hoch
2. Deploy via Render.com (Web Service):
   - Runtime: Python 3
   - Start Command: `python main.py`
   - Environment Variable: `OPENAI_API_KEY`
3. Fertig! Du bekommst eine öffentliche URL

