from flask import Flask, request, jsonify
from gpt_parser import parse_with_gpt, execute_command

app = Flask(__name__)

@app.route('/')
def home():
    return 'Chaos-to-Command API is live!'

@app.route('/chaos', methods=['POST'])
def chaos_handler():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    message = data['message']
    gpt_result = parse_with_gpt(message)
    execute_command(gpt_result)

    return jsonify({
        'status': 'executed',
        'input': message,
        'result': gpt_result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
