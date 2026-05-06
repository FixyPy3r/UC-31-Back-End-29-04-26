from flask import Flask, render_template

app = Flask(__name__)

@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    soma = n1 + n2
    return f"A soma de {n1} + {n2} é {soma}"

if __name__ == '__main__':
    app.run(debug=True)