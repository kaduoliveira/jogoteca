from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Usuarios

titulo = 'Jogos Maneiros Demais'

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    print('Abrindo a página inicial.')
    return render_template('lista.html', titulo=titulo, jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado pro login.')
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods = ['POST' ,])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    imagem_padrao = 'https://www.buritama.sp.leg.br/imagens/parlamentares-2013-2016/sem-foto.jpg'
    imagem_jogo = request.form['imagem_jogo']
    
    if imagem_jogo == '':
        imagem_jogo = imagem_padrao
    else:
        imagem_jogo = imagem_jogo

    jogo = Jogos.query.filter_by(nome=nome).first()

    # testando se o jogo já existe
    if jogo:
        flash('Esse jogo já existe no cadastro')
        return redirect(url_for('index'))
    # inserindo no banco de dados
    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console, imagem_jogo=imagem_jogo)
    db.session.add(novo_jogo)
    db.session.commit()
    print(novo_jogo.imagem_jogo)
    print(f'O novo jogo "{nome}" foi criado e enviado para o banco de dados.')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionado para a página de edição de Jogos.')
        return redirect(url_for('login', proxima=url_for('editar')))
    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo = 'Editando Jogos', jogo=jogo)

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        print('Redirecionando para login antes de acessar o sistema.')
        return redirect(url_for('login'))
    jogo = Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso.')
    return redirect(url_for('index'))

@app.route('/atualizar', methods=['POST',])
def atualizar():
    # Localizando o objeto no banco de dados
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    # Alocando novos valores buscando no formulario
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']
    jogo.imagem_jogo = request.form['imagem_jogo']
    # Gravando as informações no banco
    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST' ,])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname  + ' foi logado com sucesso!')
            proxima_pagina = request.form['proxima']
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
