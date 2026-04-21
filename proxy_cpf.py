from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)

@app.route('/cpf/<cpf>')
def consultar(cpf):
    try:
        # Tenta ReceitaWS primeiro
        r = requests.get(
            f'https://receitaws.com.br/v1/cpf/{cpf}',
            headers={
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Android; Mobile)'
            },
            timeout=15
        )
        text = r.text.strip()
        if text and text != '{}' and 'erro' not in text.lower()[:20]:
            resp = make_response(text, r.status_code)
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        # Fallback: CPFcerto API
        r2 = requests.get(
            f'https://api.cpfcnpj.com.br/5ae973d7a997af13f0aaf2bf60e65803/1/{cpf}',
            timeout=15
        )
        resp = make_response(r2.text, r2.status_code)
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    except Exception as e:
        resp = make_response(jsonify({'erro': str(e)}), 500)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
