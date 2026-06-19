from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "seguro-segredo"

def get_lista():
    if "filmes" not in session:
        session["filmes"] = []
    return session["filmes"]


@app.route("/")
def index():
    filmes = get_lista()
    return render_template("index.html", filmes=filmes)


@app.route("/adicionar", methods=["POST"])
def adicionar():

    nome = request.form.get("nome")

    if nome:
        filmes = get_lista()

        novo_filme = {
            "nome": nome,
            "assistido":False
        }

        filmes.append(novo_filme)


        session["filmes"] = filmes

    return redirect(url_for("index"))


@app.route("/marcar/<int:indice>", methods=["POST"])
def marcar(indice):
    filmes = get_lista()

    if 0 <= indice < len(filmes):
        filmes[indice]["assistido"] = not filmes[indice]["assistido"]
        session["filmes"] = filmes

    return redirect(url_for("index"))


@app.route("/limpar", methods=["POST"])
def limpar():
    session.pop("filmes", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)