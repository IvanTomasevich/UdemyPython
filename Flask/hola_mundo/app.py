from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world(nombre="invitado"):
    nombre = request.args.get('nombre', nombre)
    return "Hola {}".format(nombre)


@app.route("/suma")
def suma(num1=0, num2=0):
    num1 = request.args.get('num1', num1)
    num2 = request.args.get('num2', num2)
    return "{} más {} es igual a {}".format(num1, num2, int(num1) + int(num2))
