from flask import Flask #(faz com que a função se torne a url)
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager # para a segurança dos formularios
from flask_bcrypt import Bcrypt      # para a segurança dos formularios

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "6no0njn9yo13qimf7r3ibg96y7o88j"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage" #quando nao esta logado vai para a homepage

from FakePinterest import routes