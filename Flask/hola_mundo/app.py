import json
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
def hello_world(nombre="invitado"):
    try:
        data = json.loads(request.cookies.get('Data'))
    except TypeError: # averiguar como limpiar las cookies
        data = {}
    else:
        nombre = data.get('Nombre')

    contexto = {'nombre': nombre}
    return render_template("index.html", **contexto)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1=0, num2=0):
    contexto = {'num1': num1, 'num2': num2}
    return render_template("suma.html", **contexto)


@app.route("/contacto/")
def contacto():
    return render_template("contacto.html")


@app.route("/submit", methods=["POST"])
def submit():
    response = redirect(url_for('hello_world'))
    response.set_cookie('Data', json.dumps(dict(request.form.items())))
    return response


if __name__ == "__main__":
    app.run(debug=True)
