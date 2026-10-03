# criar a estrutura do banco de dados

from FakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin # diz qual é a classe que vai gerenciar a estrutura de login


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(id_usuario) # pega o usuario de id tal da tabela usuario no banco


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuername = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto",backref="usuarios", lazy=True)



class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)