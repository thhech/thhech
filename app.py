from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    reply = generate_reply(user_message)
    return jsonify({'reply': reply})


def generate_reply(message: str) -> str:
    message = message.strip().lower()
    if not message:
        return "Jeg forstod ikke beskeden."
    if 'hej' in message:
        return "Hej med dig! Hvordan kan jeg hjælpe?"
    if 'farvel' in message:
        return "Farvel!"
    return "Jeg er en simpel chatbot."

if __name__ == '__main__':
    app.run(debug=True)
