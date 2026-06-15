from flask import (Flask, render_template, session, redirect, url_for, request, flask)
from datetime import timedelta # para configurar duração da sessão

app = Flask(__name__)

# SECRET_KEY - obrigatório para a session funcionar
# Sem ela: RuntimeError: ao tentar usar session
app.config['SECRET_KEY'] = 'chave-aula18-uc31'

# Quanto tempo a session dura quando for permanente
# timedelta(days=7) - 7 dias
# timedelta(hours=2) - 2 horas
# timedelta(minutes=30) - 30 minutos
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/')
def inicio():
    
    nome = session.get('nome', None)
    tema = session.get('tema', 'claro')
    idioma = session.get('idioma', 'pt')
    visitas = session.get('visitas', 0)

    session['visitas'] = visitas + 1

    return render_template(
        'inicio.html', 
        nome    = nome, 
        tema    = tema, 
        idioma  = idioma, 
        visitas = session['visitas']
        )
