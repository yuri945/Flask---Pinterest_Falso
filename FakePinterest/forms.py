# criar os formularios do nosso site

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError # DataRequired = obriga a preencher o campo, EqualTo= ve se senha sao iguais, Length = so permite senha de tal tamanho, ValidationError = mensagem de erro caso tenha erro

from FakePinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    senha = PasswordField("Senha",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")


class FormCriarConta(FlaskForm): # é bom olhar no models o que o usuario tem no banco
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    username = StringField("Nome de usuario", validators=[DataRequired()])
    senha =  PasswordField("Senha",validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email): # valida se o usuario tem o email cadastrado
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")