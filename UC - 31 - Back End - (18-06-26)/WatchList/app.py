"""
Lista de filmes/séries para assistir.

A lista NÃO é salva em nenhum arquivo ou banco de dados.
Ela fica guardada na "session" do Flask, que é só um cookie no
navegador do usuário. Por isso, se você limpar os cookies ou abrir
em outro navegador, a lista volta a ficar vazia.
"""

from flask import Flask, render_template, request, redirect, url_for, session

# Cria a aplicação Flask. É sempre o primeiro passo.
app = Flask(__name__)

# O Flask precisa dessa "chave secreta" para conseguir criptografar
# o cookie de sessão. Pode ser qualquer texto, mas em um projeto real
# o ideal é não deixar fixo no código.
app.secret_key = "seguro-segredo"

# Função auxiliar: pega a lista de filmes que está guardada na
# sessão. Se ainda não existir nenhuma lista, cria uma vazia.

def get_lista():
    if "filmes" not in session:
        session["filmes"] = []
    return session["filmes"]

# Rota "/" -> mostra a página principal: formulário + lista

@app.route("/")
def index():
    filmes = get_lista()
    return render_template("index.html", filmes=filmes)

# Rota "/adicionar" -> recebe os dados do formulário (POST) e
# adiciona um novo filme/série na lista da sessão

@app.route("/adicionar", methods=["POST"])
def adicionar():
    # request.form é onde ficam os dados enviados pelo <form method="post">
    nome = request.form.get("nome")

    if nome:  # só adiciona se o usuário digitou algo
        filmes = get_lista()

        novo_filme = {
            "nome": nome,
            "assistido": False  # todo filme começa como "não assistido"
        }

        filmes.append(novo_filme)

        # Importante: depois de alterar a lista, é preciso reatribuir
        # em session["filmes"] para o Flask salvar a mudança no cookie.
        session["filmes"] = filmes

    # redireciona de volta para a página principal
    return redirect(url_for("index"))


# Rota "/marcar/<indice>" -> alterna entre assistido e não assistido
# <indice> é a posição do filme na lista (0, 1, 2...)

@app.route("/marcar/<int:indice>", methods=["POST"])
def marcar(indice):
    filmes = get_lista()

    if 0 <= indice < len(filmes):
        # "not" inverte o valor: True vira False, False vira True
        filmes[indice]["assistido"] = not filmes[indice]["assistido"]
        session["filmes"] = filmes

    return redirect(url_for("index"))



# Rota "/limpar" -> apaga toda a lista da sessão

@app.route("/limpar", methods=["POST"])
def limpar():
    session.pop("filmes", None)  # remove a chave "filmes" da sessão
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)