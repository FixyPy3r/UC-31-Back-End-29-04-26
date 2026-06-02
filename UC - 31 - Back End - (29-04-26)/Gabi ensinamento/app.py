from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome="Vitor"
    return render_template('index.html', title='Página inicial', nome=nome)

@app.route('/usuario')
def usuario():
    usuario = {'nome:', 'Gaby', 'email:', 'cortezyasmin@gmail.com'}
    return render_template('index.html', title='Página Inicial', usuario=usuario, nome=None)

@app.route('/dados', defaults={"nome":"usuário comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'olá, {nome}!'

@app.route('/semestre/<int:x')
def semestre(x):
    return 'Estamos no semestre ' + str(x)

@app.route('/pagament/<float:valor>')
def pagamento(valor):
    return 'Você pagou: ' + str(valor)

@app.route('/somar', defaults={"n1": "0", "n2": "0"})
@app.route('/somar/<int:n1>/<int:n2>')
def somar(n1, n2):
        resultado = n1 + n2
        return str(resultado)

@app.route('/soma', defauts={"n1": "0", "n2": "0"})
@app.route('/soma/<int:n1>/<int:n2>')
def soma (n1,n2):
    resultado = n1 + n2
    return render_template('somar.html', n1=n1, n2=n2, resultado=resultado)



if __name__ == '__main__':
    app.run(debug=True)