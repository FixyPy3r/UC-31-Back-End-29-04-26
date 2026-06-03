from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def formulario():
    return render_template('index2.html')


@app.route('/cadastro', methods=['POST'])
def cadastro():

    nome   = request.form.get('nome',   '').strip().title()
    email  = request.form.get('email',  '').strip().lower()
    phone  = request.form.get('phone',  '').strip()
    cpf    = request.form.get('cpf',    '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso  = request.form.get('curso',  '').strip().title()
    idade  = request.form.get('idade',  '').strip()
    senha  = request.form.get('senha',  '').strip()


    phone_tratado = phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
    cpf_tratado   = cpf.replace('.', '').replace('-', '')

    erros = []

    if not all([nome, email, phone, cpf, cidade, estado, curso, idade, senha]):
        erros.append('Preencha todos os campos obrigatórios.')

    if len(nome) < 8:
        erros.append('Nome inválido.')

    if '@' not in email or '.com' not in email:
        erros.append('E-mail inválido.')

    if len(phone_tratado) != 11 or not phone_tratado.isdigit():
        erros.append('Telefone inválido.')

    if len(cpf_tratado) != 11 or not cpf_tratado.isdigit():
        erros.append('CPF inválido.')

    if len(cidade) < 3:
        erros.append('Cidade inválida.')

    if len(estado) != 2 or not estado.isalpha():
        erros.append('Estado inválido.')

    if not curso:
        erros.append('Curso obrigatório.')

    if not idade.isdigit() or int(idade) < 16:
        erros.append('Idade inválida.')

    if len(senha) < 8 or not any(c.isdigit() for c in senha):
        erros.append('Senha muito fraca.')


    if erros:
        return render_template('index.html', erros=erros)

    dados = {
        'nome':   nome,
        'email':  email,
        'phone':  phone_tratado,
        'cpf':    cpf_tratado,
        'cidade': cidade,
        'estado': estado,
        'curso':  curso,
        'idade':  idade,
    }
    return render_template('index2.html', dados=dados)


if __name__ == '__main__':
    app.run(debug=True)