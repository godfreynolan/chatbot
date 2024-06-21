from flask import Flask, request, jsonify, render_template
import openai
import config

app = Flask(__name__)

openai.api_key = config.OPENAI_API_KEY

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = openai.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:riis-llc::9cabEtl7",
        messages=[{
            "role": "user",
            "content" : user_input
        }],
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].message.content})

if __name__ == '__main__':
    app.run()
