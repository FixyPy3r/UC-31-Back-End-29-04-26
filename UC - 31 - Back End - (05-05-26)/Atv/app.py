from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login")
def login():
    nome = 'Vitor'
    return render_template("login.html", nome=nome)

if __name__ == "__main__":
    app.run(debug=True)