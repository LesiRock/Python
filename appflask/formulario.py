from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField

class PersonaForm(FlaskForm):
    nombre = StringField('Ingresa tu nombre')
    edad = IntegerField('Edad')
    email = StringField('Correo')
    contrasena = PasswordField('Contrasena')
    enviar = SubmitField('Enviar')