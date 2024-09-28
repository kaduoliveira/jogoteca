from jogoteca import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    imagem_jogo = db.Column(db.String(500))

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name