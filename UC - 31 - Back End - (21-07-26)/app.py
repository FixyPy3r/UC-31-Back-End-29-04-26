from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"


def ler_livros():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as f:
            json.dump([], f)

    with open(ARQUIVO, "r") as f:
        livros = json.load(f)
    return livros


def salvar_livros(livros):
    with open(ARQUIVO, "w") as f:
        json.dump(livros, f, indent=4)


@app.route("/")
def index():
    return render_template("cadastro.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    titulo = request.form["titulo"]
    autor = request.form["autor"]
    ano = request.form["ano"]
    categoria = request.form["categoria"]
    quantidade = request.form["quantidade"]

    if titulo == "" or autor == "" or ano == "" or categoria == "" or quantidade == "":
        return "Preencha todos os campos!"

    if not ano.isdigit():
        return "O ano deve conter apenas números!"

    if not quantidade.isdigit() or int(quantidade) <= 0:
        return "A quantidade deve ser um número inteiro maior que zero!"

    livros = ler_livros()

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "categoria": categoria,
        "quantidade": int(quantidade)
    }

    livros.append(novo_livro)
    salvar_livros(livros)

    return redirect(url_for("livros"))


@app.route("/livros")
def livros():
    lista_livros = ler_livros()
    return render_template("livros.html", livros=lista_livros)


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    livro_encontrado = None
    buscou = False

    if request.method == "POST":
        titulo_buscado = request.form["titulo"]
        buscou = True
        livros = ler_livros()

        for livro in livros:
            if livro["titulo"].lower() == titulo_buscado.lower():
                livro_encontrado = livro
                break

    return render_template("buscar.html", livro=livro_encontrado, buscou=buscou)


@app.route("/editar/<int:indice>", methods=["GET", "POST"])
def editar(indice):
    livros = ler_livros()

    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]
        categoria = request.form["categoria"]
        quantidade = request.form["quantidade"]

        if titulo == "" or autor == "" or ano == "" or categoria == "" or quantidade == "":
            return "Preencha todos os campos!"

        if not ano.isdigit():
            return "O ano deve conter apenas números!"

        if not quantidade.isdigit() or int(quantidade) <= 0:
            return "A quantidade deve ser um número inteiro maior que zero!"

        livros[indice]["titulo"] = titulo
        livros[indice]["autor"] = autor
        livros[indice]["ano"] = int(ano)
        livros[indice]["categoria"] = categoria
        livros[indice]["quantidade"] = int(quantidade)

        salvar_livros(livros)
        return redirect(url_for("livros"))

    livro = livros[indice]
    return render_template("editar.html", livro=livro, indice=indice)


@app.route("/excluir/<int:indice>")
def excluir(indice):
    livros = ler_livros()
    livros.pop(indice)
    salvar_livros(livros)
    return redirect(url_for("livros"))


if __name__ == "__main__":
    app.run(debug=True)
