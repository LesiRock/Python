from flask import Flask, render_template
from formulario import PersonaForm

from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_palabra_secreta'

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'tu_usuario'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tu_contraseña'
app.config['MYSQL_DATABASE_DB'] = 'nombre_de_tu_base_de_datos'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'#para configurar una base de datos local
#usuario, contraseña y la ruta que de el proveedor

@app.route('/')
def inicio ():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login ():
    return "BIENVENIDO Has iniciado sesión"

@app.route('/registro', methods=['POST', 'GET'])
def registro ():
    form = PersonaForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        email = form.email.data
        contrasena = form.contrasena.data
        return f'{nombre} has sido registrado!!!!!'
    return render_template('registro.html', form=form)

if __name__== '__main__':
    app.run(debug=True)

