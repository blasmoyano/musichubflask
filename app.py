from flask import Flask,session, request, render_template, redirect, url_for
from hashlib import md5
from functools import wraps
import base
import random
import forms

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def randomimagen():
    fondo = ['mh-fondo1.jpg','mh-fondo2.jpg','mh-fondo3.jpg']
    global seleccion
    seleccion = random.choice(fondo)

@app.route("/registrate", methods=['GET','POST'])
def registracion():
    randomimagen()
    registracion_form = forms.Registrate(request.form)
    if request.method == 'POST'and registracion_form.validate():
        passw = md5((registracion_form.passw.data).encode('utf-8')).hexdigest()
        insertusuario = base.Persona.create(
        username=registracion_form.username.data,
        nombrecompleto=registracion_form.nombrecompleto.data,
        email= registracion_form.email.data,
        contrasena = passw)
        return render_template('login.html',seleccion = seleccion,form = registracion_form)
    return render_template('registrate.html',seleccion = seleccion, form = registracion_form) #renderiaza por defecto


@app.route("/login", methods=['GET','POST'])
def login():
    randomimagen()
    login_form = forms.Login(request.form)
    if request.method == 'POST':
        password = md5((login_form.passw.data).encode('utf-8')).hexdigest()
        try:
            user1 = base.Persona.select().where(base.Persona.username == login_form.username.data , base.Persona.contrasena == password).get()
            session['susername'] = user1.username
            return redirect(url_for('home'))
        except base.Persona.DoesNotExist:
            error = "La contraseña no coincide"
            return render_template('login.html',seleccion = seleccion, error = error,form = login_form)
    return render_template('login.html',seleccion = seleccion,form = login_form) #renderiaza por defecto

@app.route("/")
@app.route("/home")
def home():
    if 'susername' in session:
        usuario = session['susername']
        return render_template('home.html',usuario = usuario)
    elif 'susername' not in session and request.endpoint in ['home']:
        return redirect('login')

@app.route("/perfil", methods=['GET', 'POST'])
def perfil():
    if 'susername' in session:
        usuario = session['susername']
        user1 = base.Persona.select().where(base.Persona.username == usuario).get()
        nombre = user1.nombrecompleto
        email = user1.email
        edad = user1.edad
        bio = user1.bio
        perfil_form = forms.EditPerfil(request.form)
        if request.method == 'POST':
            user1.nombrecompleto = perfil_form.nombrecompleto.data
            user1.email = perfil_form.email.data
            user1.edad = perfil_form.edad.data
            user1.bio = perfil_form.bio.data
            user1.save()
            return render_template('perfil.html',usuario = usuario,nombre = nombre, email = email, form = perfil_form,edad=edad,refresh = "refresh")

        return render_template('perfil.html',
                                usuario = usuario,
                                nombre = nombre,
                                email = email,
                                form = perfil_form,
                                bio = bio,
                                edad=edad)
    elif 'susername' not in session and request.endpoint in ['perfil']:
        return redirect('login')

@app.route('/banda')
def banda():
    return render_template('banda.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('susername', None)
    return redirect('login')


if __name__ == "__main__":
	app.run(debug=True)
