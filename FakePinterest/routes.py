# criar as rotas do nosso site@app.route("/")

from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required 
from FakePinterest.forms import FormCriarConta, FormLogin



@app.route("/", methods=["GET", "POST"]) # atributo q permite a pessoa só acessar isso caso use esse link
def homepage():
    formlogin=FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<usuario>") # atributo q permite a pessoa só acessar isso caso use esse link
@login_required # atributo q restringe isso apenas a pessoas que estão logadas
def perfil(usuario):
    return render_template("perfil.html", usuario = usuario)


