from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.console}'


app = Flask(__name__)

@app.route('/inicio')
def ola():
    titulo = 'Jogos maneiros'

    #instanciando no código
    jogo1 = Jogo('Mortal Kombat', 'Luta', 'Multiplataforma')
    jogo2 = Jogo('Uncharted', 'Aventura', 'Playstation3')
    jogo3 = Jogo('Forza Motorsport', 'Corrida', 'Xbox Series S&X')
    
    lista_jogos = ['Street Figther',
                   'Mega Man 8',
                   'Super Star Soccer',
                   jogo1,
                   jogo2,
                   jogo3]

    return render_template('lista.html', titulo=titulo, jogos = lista_jogos)

app.run()
