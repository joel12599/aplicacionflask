from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask!"

if __name__ == "__main__":
    app.run(debug=True)



@app.route("/usuarios", methods=["POST"])  
def crear_usuario():  
    nuevo_U = request.get_json()  
    nuevo_u["id"] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)  
    return jsonify({"mensaje": "listo vale mia", "usuario": nuevo_U}), 201  

@app.route("/usuarios", methods=["GET"])  
