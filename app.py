from flask import Flask, request, render_template
from flask_cors import CORS
from openai import OpenAI
import json
import os

app = Flask(__name__)
CORS(app)

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)

conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    try:
        data = request.get_data(as_text=True)
        data = json.loads(data)
        input_text = data.get('prompt', '').strip()

        if not input_text:
            return "Please type a message.", 400

        # Build short conversation context
        messages = [
            {
                "role": "system",
                "content": "You are a friendly, concise chatbot inside a Flask web app."
            }
        ]

        for item in conversation_history[-6:]:
            messages.append({"role": "user", "content": item["user"]})
            messages.append({"role": "assistant", "content": item["bot"]})

        messages.append({"role": "user", "content": input_text})

        response = client.responses.create(
            model="gpt-5.4",
            input=messages
        )

        bot_text = response.output_text.strip()

        conversation_history.append({
            "user": input_text,
            "bot": bot_text
        })

        return bot_text

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)