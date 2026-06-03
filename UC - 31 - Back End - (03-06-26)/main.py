from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            mensagem = "O campo nome é obrigatório"
        else:
            mensagem = f"Cadastro realizado com sucesso! Bem-vindo, (nome)"
    return render_template('index.html', mensagem=mensagem)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/validacao', methods=['POST'])
def cadastro():
    
    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().title()
    phone = request.form.get('phone', '').strip().title()
    cpf = request.form.get('cpf', '').strip().title()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().title()
    curso = request.form.get('curso', '').strip().title()
    idade = request.form.get('idade', '').strip().title()
    senha = request.form.get('senha', '').strip().title()

    return f"""
    Nome: {nome} <br>
    Email: {email} <br>
    Telefone: {phone} <br>
    Cpf: {cpf} <br>
    Cidade: {cidade} <br>
    Estado: {estado} <br>
    Curso: {curso} <br>
    Idade: {idade} <br>
    Senha: {senha} <br>
    """

if __name__ == '__main__':
    app.run(debug=True)