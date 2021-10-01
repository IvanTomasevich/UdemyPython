from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<nombre>")
def hello_world(nombre="invitado"):
    contexto = {'nombre': nombre}
    return render_template("index.html", **contexto)


@app.route("/suma/<int:num1>/<int:num2>")
@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1=0, num2=0):
    contexto = {'num1': num1, 'num2': num2}
    return render_template("suma.html", **contexto)


if __name__ == "__main__":
    app.run(debug=True)
