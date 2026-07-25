from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'chavesegredo_#acabahoradaIA'

@app.route('/cantinho')
def cantinho():
    nome = session.get('usuario_nome')

    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

    return render_template('cantinho.html',
    nome      = nome,
    cor       = 'Azul',
    linguagem = 'Python',
    frase     = 'Algo que me representa',
    visitas   = visitas
    )
