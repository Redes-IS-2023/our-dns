from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def endpoint():
    data = request.json  # Obtener los datos enviados en formato JSON
    print(data)
    # Aquí puedes procesar los datos como desees
    # ...

    response = {'message': 'Datos recibidos correctamente'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
