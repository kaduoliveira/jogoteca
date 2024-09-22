from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#instanciando no código
jogo1 = Jogo('Mortal Kombat', 'Luta', 'Multiplataforma')
jogo2 = Jogo('Uncharted', 'Aventura', 'Playstation3')
jogo3 = Jogo('Forza Motorsport', 'Corrida', 'Xbox Series S&X')
    
lista = [jogo1, jogo2, jogo3]

titulo = 'Jogos Maneiros Demais'

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('lista.html', titulo=titulo, jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '895623' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado']  + ' foi logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado.')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/') 
        
#codigo para outra maquina na rede ter acesso a aplicação
'''if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.15')'''

app.run(debug=True)