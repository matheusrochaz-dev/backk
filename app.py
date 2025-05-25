from flask import Flask, request, jsonify
from flask_cors import CORS
import os, json

app = Flask(__name__)
CORS(app, origins=["https://codax-six.vercel.app"])
ARQUIVO_COMENTARIOS = "comentarios.json"

# Carregar os comentários
def carregar_comentarios():
    if os.path.exists(ARQUIVO_COMENTARIOS):
        with open(ARQUIVO_COMENTARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salvar os comentários
def salvar_comentarios(comentarios):
    with open(ARQUIVO_COMENTARIOS, "w", encoding="utf-8") as f:
        json.dump(comentarios, f, ensure_ascii=False, indent=2)

@app.route('/comentarios', methods=['GET'])
def obter_comentarios():
    return jsonify(carregar_comentarios())

@app.route('/comentar', methods=['POST'])
def comentar():
    comentario = request.json.get("comentario", "").strip()
    if comentario:
        comentarios = carregar_comentarios()
        novo = {"id": len(comentarios) + 1, "texto": comentario}
        comentarios.append(novo)
        salvar_comentarios(comentarios)
        return jsonify({"message": "Comentário adicionado!"}), 201
    return jsonify({"message": "Comentário vazio."}), 400

@app.route('/editar/<int:id>', methods=['PUT'])
def editar(id):
    novo_texto = request.json.get("comentario", "").strip()
    comentarios = carregar_comentarios()
    for c in comentarios:
        if c["id"] == id:
            c["texto"] = novo_texto
            salvar_comentarios(comentarios)
            return jsonify({"message": "Comentário editado!"})
    return jsonify({"message": "Comentário não encontrado."}), 404

@app.route('/apagar/<int:id>', methods=['DELETE'])
def apagar(id):
    comentarios = carregar_comentarios()
    comentarios = [c for c in comentarios if c["id"] != id]
    salvar_comentarios(comentarios)
    return jsonify({"message": "Comentário apagado."})
