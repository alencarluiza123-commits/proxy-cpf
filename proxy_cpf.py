from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/cpf/<cpf>')
def consultar(cpf):
    try:
        r = requests.get(
            f'https://receitaws.com.br/v1/cpf/{cpf}',
            headers={'Accept': 'application/json'},
            timeout=10
        )
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
