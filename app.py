from flask import Flask, request, jsonify
import openai
import os

# Get the OpenAI API key from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot Server is running."

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return jsonify({"message": "Send a POST request to this endpoint with a JSON body containing a 'message' key."})
    
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
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
