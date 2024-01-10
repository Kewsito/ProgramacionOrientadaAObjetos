from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_pyfile("config.py")

from models import db
from models import Usuario


@app.route("/")
def inicio():
    return render_template('home.html')


@app.route("/registro_usuario", methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        if not request.form['name'] and not request.form['email'] and not request.form['password']:
            return render_template('Error.html', mensaje="POR FAVOR INGRESE LOS DATOS")
        else:
            user = Usuario(nombre=request.form['name'], correo=request.form['email'],
                           clave=generate_password_hash(request.form['password']))
            db.session.add(user)
            db.session.commit()
            return render_template('home.html')
    else:
        return render_template('registro_usuario.html')


@app.route("/acceso_usuario", methods=['GET', 'POST'])
def acceso_usuario():
    if request.method == 'POST':
        if not request.form['email'] and not request.form['password']:
            return render_template('Error.html', mensaje="POR FAVOR INGRESE USUARIO Y CONTRASEÑA")

        else:
            consultacorreo = Usuario.query.filter_by(correo=request.form['email']).first()
            if consultacorreo:
                clave = check_password_hash(consultacorreo.clave,request.form['password'])
                if clave:
                    return render_template('base_usuario.html')
                else:
                    return render_template('Error.html', mensaje="CONTRASEÑA INCORRECTA")
            else:
                return render_template('Error.html', mensaje="EL CORREO INGRESADO NO ES EL CORRECTO")
    else:
        return render_template('acceso_usuario.html')


@app.route("/compartir_receta", methods = ['GET', 'POST'])
def compartir_receta():
    return render_template('Error.html', mensaje = "ME METI JAJA")
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
