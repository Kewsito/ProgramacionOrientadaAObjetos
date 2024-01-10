from __main__ import app
from flask_sqlalchemy import SQLAlchemy
#from datetime import DateTime

db = SQLAlchemy(app)


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(20), nullable=False, unique=True)
    clave = db.Column(db.String(20), nullable=False)
    receta = db.relationship("Receta", backref="usuario", cascade="all, delete-orphan")

class Receta(db.Model):
    __tablename__ = "receta"
    id = db.Column(db.Integer, primary_key=True)
    nombrereceta = db.Column(db.String(80), nullable=False)
    tiempo = db.Column(db.Integer, nullable=False)
    elaboracion = db.Column(db.Text, nullable=False)
    cantidadmegusta = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)
    ingredientes = db.relationship(
        "Ingredientes", backref="receta", cascade="all,delete-orphan"
    )
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))


class Ingredientes(db.Model):
    __tablename__ = "ingrediente"
    id = db.Column(db.Integer, primary_key=True)
    nombreingrediente = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    unidad = db.Column(db.Integer, nullable=False)
    receta_id = db.Column(db.Integer, db.ForeignKey("receta.id"))
