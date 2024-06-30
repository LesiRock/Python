from flask import Flask, render_template
from formulario import PersonaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_palabra_secreta'

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

