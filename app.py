from flask import Flask, request, jsonify
import openai
import os

# Get the OpenAI API key from environment variables
openai.api_key = os.environ.get("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")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot Server is running."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call OpenAI API using old (compatible) method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a compassionate, non-judgmental therapist trained to listen and help users with their thoughts and feelings. Do not mention that you are an AI or language model. Always speak empathetically and offer supportive, thoughtful responses."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
