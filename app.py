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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

@app.route('/')
def index():
    return "API funcionando"
