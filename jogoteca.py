from symtable import Class

from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
from flask_wtf.csrf import CSRFProtect

# essa parte do códigó não é mais necessária devido ao uso de banco de dados
'''

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#instanciando no código
jogo1 = Jogo('Mortal Kombat', 'Luta', 'Multiplataforma')
jogo2 = Jogo('Uncharted', 'Aventura', 'Playstation3')
jogo3 = Jogo('Forza Motorsport', 'Corrida', 'Xbox Series S&X')

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Carlos Oliveira', 'CO', '895623')
usuario2 = Usuario('Laura Oliveira', 'LO', '0704')
usuario3 = Usuario('Helena Oliveira', 'HO', '0605')

#dicionario de usuários 
usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}

    
lista = [jogo1, jogo2, jogo3]
'''

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from views import *
#codigo para outra maquina na rede ter acesso a aplicação
'''if __name__ == '__main__':
    app.run(debug=True, host='192.168.15.100')'''

if __name__ == '__main__':
    app.run(debug=True)