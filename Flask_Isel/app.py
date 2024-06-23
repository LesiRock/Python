from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return render_template('index.html')

@app.route('/formulario')
def registro():
    return render_template('formulario.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)