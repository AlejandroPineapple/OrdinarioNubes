from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el endpoint GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Vamos a hacer un consome'}), 200

# Ejecución de la app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)