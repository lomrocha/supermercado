# Importar bibliotecas
from flask \
  import Flask, render_template, request
from flaskext.mysql \
  import MySQL

# Instanciar aplicação
supermercado= Flask(__name__)

# Configurar banco de dados
banco.config["MYSQL_DATABASE_USER"] = "root"
banco.config["MYSQL_DATABASE_PASSWORD"] = "root"
banco.config["MYSQL_DATABASE_DB"] = "supermercado"

# Instanciar banco de dados
mysql = MySQL()
mysql.init_app(supermercado)

# Rota para /
@supermercado.route("/")

def index():
  return render_template("form_login.html")

# Rota para /login
@supermercado.route("/login")
