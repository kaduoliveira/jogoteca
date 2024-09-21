from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    titulo = 'Jogos maneiros'
    return render_template('lista.html', titulo=titulo)

app.run()
