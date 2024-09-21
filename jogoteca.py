from flask import Flask, render_template, request, redirect

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

@app.route('/')
def index():

    return render_template('lista.html', titulo=titulo, jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)
