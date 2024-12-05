from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def sendExample():
    data = {
            "message" : "Hola a todos!, este es un archivo de ejemplo para la evidencia de git",
            "aprendiz" : "Juan Andres Ojeda Lugo",
            "instructor": "Oscar Campos",
            "evidence-codes": ["GA7-220501096-AA1-EV05", "GA7-220501096-AA1-EV04"],
            "date": "5-12-24"
        }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)