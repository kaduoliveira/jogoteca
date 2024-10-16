from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST' ,])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first() # request.form['usuario'], q vinha do formulario html foi substituido pelo padrao flask
    senha = check_password_hash(usuario.senha, form.senha.data) # comparando a senha do banco com a senha do formulario e devolvendo True ou False
    if usuario and senha: # essa condicional segue a diante se o usuario constar no banco e se a senha passar no teste
        # if form.senha.data == usuario.senha: # essa condição perdeu o sentido com a implementação do check_password_hash 
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname  + ' foi logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if proxima_pagina == 'None':
            proxima_pagina = '/'
        print(f"Redirecionando para: {proxima_pagina}")  # Mensagem de depuração
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
