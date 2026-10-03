# criar as rotas do nosso site

from flask import render_template, url_for, redirect
from FakePinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user # current user sabe quem está logado, é usado para o logout
from FakePinterest.forms import FormCriarConta, FormLogin
from FakePinterest.models import Usuario, Foto



@app.route("/", methods=["GET", "POST"]) # atributo q permite a pessoa só acessar isso caso use esse link
def homepage():

    form_login=FormLogin()

    if form_login.validate_on_submit(): # significa que preencheu o formulario e esta valido
        usuario = Usuario.query.filter_by(email=form_login.email.data).first() # ve se o email esta correto
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data): # ve se o usuario existe e a senha é igual a senha criptografada

            login_user(usuario) # faz o login

            return redirect(url_for("perfil", usuario=usuario.username)) # joga pra tela de perfil
        
    return render_template("homepage.html", form=form_login)

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():

    form_criarconta = FormCriarConta()

    if form_criarconta.validate_on_submit(): # verifica se o formulario que fizeram esta valido
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data) # criptografa a senha
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha,
                          email=form_criarconta.email.data) #olhar no model

        database.session.add(usuario) # armazena a variavel usuario no banco de dados
        database.session.commit()

        login_user(usuario, remember=True) # faz com que esteja logado pois a tela de usuario precisa estar com o login feito e lembra dele

        return redirect(url_for("perfil", usuario=usuario.username)) # redireciona para a funcao perfil após o criarconta
        
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<usuario>") # atributo q permite a pessoa só acessar isso caso use esse link
@login_required # atributo q restringe isso apenas a pessoas que estão logadas
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario)



@app.route("/logout")
@login_required
def logout():
    logout_user() # faz o logout
    return redirect(url_for("homepage")) # joga pro homepage


