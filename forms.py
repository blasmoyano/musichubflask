from wtforms import Form, StringField,PasswordField,IntegerField,TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class Registrate(Form):
    username = StringField('username',
    [
        validators.Required(message="El username es requerido"),
        validators.length(min=4, max=25, message="Ingrese un usuario valido")
    ])
    nombrecompleto = StringField('nombre completo',
    [
        validators.Required(message="El username es requerido"),
        validators.length(min=4, max=25, message="Ingrese un usuario valido")
    ])
    email = EmailField ('Correo Electronico',
    [
            validators.Required(message="El username es requerido"),
            validators.length(min=4, max=25, message="Ingrese un usuario valido")
    ])
    passw = PasswordField('Contraseña',
    [
        validators.Required(message="El username es requerido"),
        validators.length(min=4, max=25, message="Ingrese un usuario valido")
    ])

class Login(Form):
    username = StringField('Nombre de Usuario',
    [
        validators.Required(message="El username es requerido"),
    ])
    passw = PasswordField('Contraseña',
    [
        validators.Required(message="El username es requerido"),
    ])

class EditPerfil(Form):
        nombrecompleto = StringField('Nombre de Usuarios')
        email = EmailField('Correo Electronico')
        contrasena = PasswordField('Contraseña')
        edad = IntegerField('Edad')
        telefono = IntegerField('Telefono')
        bio = TextAreaField('Bio')
