from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ GPT Assistant läuft!"

@app.route("/assistant", methods=["POST"])
def assistant():
    data = request.get_json()
    prompt = data.get("prompt", "")

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein kluger Assistent. Antworte hilfreich."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
