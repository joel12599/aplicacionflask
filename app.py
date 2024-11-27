import os
from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

@app.route("/")
def home():
    return "¡Hola, Flask!"

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    usuario_U = request.get_json()
    usuario_U["id"] = len(usuarios) + 1
    usuarios.append(usuario_U)
    return jsonify({"mensaje": "Usuario creado correctamente", "usuario": usuario_U}), 201

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify({"usuario": usuario})
    return jsonify({"error": "No encontrado"}), 404

if __name__ == "__main__":
    # Obtén el puerto de la variable de entorno PORT (o usa 5000 por defecto)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
