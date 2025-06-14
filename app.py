from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, origins=["https://codax-six.vercel.app", "https://backk-1-5s4u.onrender.com/", "http://127.0.0.1:5501/"])

# 🔑 Substitua pelas suas credenciais
SUPABASE_URL = "https://aqvrwljdaoraeiwverku.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFxdnJ3bGpkYW9yYWVpd3Zlcmt1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk3NTY5NzYsImV4cCI6MjA2NTMzMjk3Nn0.d_9NmknRUALzVW0McoBJzc79NwM0kY2Yj0s48LOGTBE"

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

# tabela comentarios
@app.route('/comentarios', methods=['GET'])
def obter_comentarios():
    url = f"{SUPABASE_URL}/rest/v1/comentarios?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentar', methods=['POST'])
def comentar():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentarios"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

# tabela comentarios 2

@app.route('/comentariosDois', methods=['GET'])
def obter_comentariosDOIS():
    url = f"{SUPABASE_URL}/rest/v1/comentariosDois?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarDois', methods=['POST'])
def comentarDOIS():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosDois"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# tabela comentarioE

@app.route('/comentariosE', methods=['GET'])
def obter_comentariosE():
    url = f"{SUPABASE_URL}/rest/v1/comentariosE?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarE', methods=['POST'])
def comentarE():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosE"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# tabela comentariosL

@app.route('/comentariosL', methods=['GET'])
def obter_comentariosL():
    url = f"{SUPABASE_URL}/rest/v1/comentariosL?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarL', methods=['POST'])
def comentarDOIS():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosL"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
# tabela comentariosN

@app.route('/comentariosN', methods=['GET'])
def obter_comentariosDOIS():
    url = f"{SUPABASE_URL}/rest/v1/comentariosN?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarN', methods=['POST'])
def comentarDOIS():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosN"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# tabela comentariosO

@app.route('/comentariosO', methods=['GET'])
def obter_comentariosO():
    url = f"{SUPABASE_URL}/rest/v1/comentariosO?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarO', methods=['POST'])
def comentarO():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosO"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# tabela comentariosS

@app.route('/comentariosS', methods=['GET'])
def obter_comentariosS():
    url = f"{SUPABASE_URL}/rest/v1/comentariosS?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarS', methods=['POST'])
def comentarS():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosS"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# tabela comentariosV

@app.route('/comentariosV', methods=['GET'])
def obter_comentariosV():
    url = f"{SUPABASE_URL}/rest/v1/comentariosV?select=comentario,data&order=data.desc"
    response = requests.get(url, headers=headers)
    if response.ok:
        dados = response.json()
        comentarios = "\n\n".join([c["comentario"] for c in dados])
        return jsonify({"comentarios": comentarios})
    return jsonify({"erro": "Erro ao buscar comentários."}), 500

@app.route('/comentarV', methods=['POST'])
def comentarV():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        url = f"{SUPABASE_URL}/rest/v1/comentariosV"
        payload = {
            "comentario": comentario
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.ok:
            return jsonify({"message": "Comentário adicionado com sucesso!"}), 201
        else:
            print("STATUS:", response.status_code)
            print("TEXTO:", response.text)
            return jsonify({"erro": "Erro ao salvar comentário."}), 500
    return jsonify({"erro": "Comentário vazio."}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
