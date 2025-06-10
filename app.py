from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite chamadas do frontend

# Configurações do banco (use o seu host entre colchetes se for IPv6)
DB_HOST = "[2600:1f1e:75b:4b0f:88e8:c066:9023:7a74]"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "@FAMILIA1234@"
DB_PORT = 5432

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

# Cria a tabela caso não exista
def criar_tabela():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS comentarios (
            id SERIAL PRIMARY KEY,
            texto TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/comentarios', methods=['GET'])
def carregar_comentarios():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM comentarios ORDER BY id DESC")
    comentarios = cur.fetchall()
    cur.close()
    conn.close()
    # Retorna só os textos dos comentários numa lista
    lista = [c['texto'] for c in comentarios]
    return jsonify({"comentarios": lista})

@app.route('/comentar', methods=['POST'])
def enviar_comentario():
    data = request.json
    texto = data.get('comentario', '').strip()
    if texto == '':
        return jsonify({"error": "Comentário vazio"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO comentarios (texto) VALUES (%s)", (texto,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Comentário enviado!"}), 201

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
