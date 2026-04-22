from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

@app.route('/cpf/<cpf>')
def consultar(cpf):
    try:
        r = requests.get(
            f'https://receitaws.com.br/v1/cpf/{cpf}',
            headers={
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Android; Mobile)'
            },
            timeout=15
        )
        text = r.text.strip()
        if not text:
            text = '{"erro":"sem resposta da ReceitaWS"}'
        resp = make_response(text, r.status_code)
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        resp = make_response(jsonify({'erro': str(e)}), 500)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
