from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo

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
    form = FormularioJogo()
    return render_template('novo.html', titulo = 'Novo Jogo', form=form)

@app.route('/criar', methods = ['POST' ,])
def criar():
    form = FormularioJogo(request.form)

    # validando, se NÃO atende aos requisitos da helpers nao ele recarrega o /novo
    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    # recuperando os valores do formulario FlaskForm
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    imagem_jogo = form.imagem_jogo.data

    # imprimindo os dados obtidos do formulario
    print('-'*30)
    print('Dados do novo jogo')
    print('Nome: ', nome)
    print('Categoria: ', categoria)
    print('Console: ', console)
    print('Link imagem on-line: ', imagem_jogo)
    print('-'*30)

    '''
    # recuperando os valores dos campos do formulário
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    imagem_padrao = 'https://www.buritama.sp.leg.br/imagens/parlamentares-2013-2016/sem-foto.jpg'
    imagem_jogo = request.form['imagem_jogo']

      if imagem_jogo == '':
            imagem_jogo = imagem_padrao
        else:
            imagem_jogo = imagem_jogo
        '''

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
    jogo = Jogos.query.filter_by(id=id).first() # recupero as informações do jogo diretamente do banco de dados
    form = FormularioJogo() # instanciando o objeto
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    form.imagem_jogo.data = jogo.imagem_jogo 
    return render_template('editar.html', titulo = 'Editando Jogos', id=id, form=form) # foi substituido o jogo=jogo pelo id=id, pois não é mais preciso passar todo o objeto

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

    form = FormularioJogo(request.form) #estou instanciando o objeto form com os dados quem estou buscando no formulário da página usando o metodo request

    if form.validate_on_submit(): #verificando se o formulario atende aos requisitos definidos na classe FlaskFlorm construida na helpers

        # Localizando o objeto no banco de dados
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        # Alocando novos valores buscando no formulario
        jogo.nome = form.nome.data #código substituido para atender os padrões FlaskForm request.form['nome']
        jogo.categoria = form.categoria.data #código substituido para atender os padrões FlaskForm request.form['categoria']
        jogo.console = form.console.data #código substituido para atender os padrões FlaskForm request.form['console']
        jogo.imagem_jogo = form.imagem_jogo.data #código substituido para atender os padrões FlaskForm request.form['imagem_jogo']
        # Gravando as informações no banco
        db.session.add(jogo)
        db.session.commit()
        flash(f'O jogo {jogo.nome} foi atualizado com sucesso.')

    return redirect(url_for('index'))


