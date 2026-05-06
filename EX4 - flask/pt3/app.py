from flask import Flask

app = Flask(__name__)

@app.route('/idade/<nome>/<int:idade>')
def verificar_idade(nome, idade):
    if idade >= 18:
        return f"{nome} é maior de idade."
    else:
        return f"{nome} é menor de idade."
    
if __name__ == '__main__':
    app.run(debug=True)