from flask import Flask, render_template

app = Flask(__name__)

cardapio = [
    {
        "nome": "Hamburguer",
        "slug": "hamburguer",
        "preco": "R$ 32,90",
        "descricao": "Hambúrguer artesanal 180g, queijo cheddar, alface, tomate e molho especial.",
        "imagem": "burger.jpeg",
    },
    {
        "nome": "Pizza Margherita",
        "slug": "pizza",
        "preco": "R$ 45,90",
        "descricao": "Pizza tradicional com molho de tomate, mozzarella fresca e manjericão.",
        "imagem": "pizza.jpg",
    },
    {
        "nome": "Batata Frita",
        "slug": "batata",
        "preco": "R$ 18,90",
        "descricao": "Porção generosa de batatas fritas crocantes com sal e tempero especial da casa.",
        "imagem": "batata.jpg",
    },
    {
        "nome": "Milkshake",
        "slug": "milkshake",
        "preco": "R$ 22,90",
        "descricao": "Milkshake cremoso nos sabores chocolate, morango ou baunilha. 500ml.",
        "imagem": "milkshake.jpg",
    },
]


pedidos = [
    {"cliente": "Ana Silva",     "pedido": "Pizza Margherita",    "valor": "R$ 45,90", "status": "Entregue"},
    {"cliente": "Pedro Alves",   "pedido": "Hamburguer",           "valor": "R$ 32,90", "status": "Em preparo"},
    {"cliente": "Maria Lima",    "pedido": "Batata + Milkshake",  "valor": "R$ 41,80", "status": "Saiu para entregar"},
    {"cliente": "João Souza",    "pedido": "2x Pizza Margherita", "valor": "R$ 91,80", "status": "Entregue"},
    {"cliente": "Carla Mendes",  "pedido": "Hamburguer + Batata",  "valor": "R$ 51,80", "status": "Em preparo"},
    {"cliente": "Lucas Ferreira","pedido": "Milkshake",           "valor": "R$ 22,90", "status": "Entregue"},
]

cidades_disponiveis = ["natal", "fortaleza", "mossoró", "parnamirim", "sobral"]


mensagens_lanche = {
    "pizza":      {"titulo": "Pizza Margherita", "msg": "Pizza tradicional com molho de tomate, mozzarella fresca e manjericão.", "preco": "R$ 45,90"},
    "hamburguer": {"titulo": "Hamburguer",        "msg": "Hambúrguer artesanal 180g, queijo cheddar, alface, tomate e molho especial.", "preco": "R$ 32,90"},
    "batata":     {"titulo": "Batata Frita",      "msg": "Porção generosa de batatas fritas crocantes com sal e tempero especial da casa.", "preco": "R$ 18,90"},
    "milkshake":  {"titulo": "Milkshake",         "msg": "Milkshake cremoso nos sabores chocolate, morango ou baunilha. 500ml.", "preco": "R$ 22,90"},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cardapio")
def cardapio_page():
    return render_template("cardapio.html", cardapio=cardapio)

@app.route("/lanche/<nome>")
def lanche(nome):
    nome_lower = nome.lower()
    info = mensagens_lanche.get(nome_lower)
    return render_template("lanche.html", nome=nome, info=info)

@app.route("/pedidos")
def pedidos_page():
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):
    disponivel = cidade.lower() in cidades_disponiveis
    return render_template("cliente.html", nome=nome, cidade=cidade, disponivel=disponivel)

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
