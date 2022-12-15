from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.contactos import Contacto

from utils.db import db

contactosEnrutador = Blueprint("contactos", __name__)  # PERMITE DIVIDIR CODIGO EN VARIAS SECCIONES SIN TENER QUE HACER TANTOS IMPORTS, ES UNA DEPENDENCIA CIRCULAR

@contactosEnrutador.route('/')
def index():
    todosLosContactos = Contacto.query.all()
    return render_template("index.html", contactos=todosLosContactos)

@contactosEnrutador.route("/add/", methods=["POST"])
def add():
    name =request.form["nombre"]
    email = request.form["email"]
    telefono =  request.form["telefono"]
    nuevo_contacto = Contacto(name,email,telefono)
    print(nuevo_contacto)
    db.session.add(nuevo_contacto)
    db.session.commit()
    flash("contacto agregado")
    return redirect(url_for('contactos.index'))

@contactosEnrutador.route("/update/<id>" , methods=["POST", "GET"])
def update(id):
    contactoAActualizar = Contacto.query.get(id)
    if request.method=="POST":
        contactoAActualizar.nombre =request.form["nombre"]
        contactoAActualizar.email = request.form["email"]
        contactoAActualizar.telefono =  request.form["telefono"]
        db.session.commit()
        flash("contacto actualizado")
        return redirect(url_for('contactos.index'))
    else:
        return render_template("updateForm.html", contacto=contactoAActualizar)

@contactosEnrutador.route("/delete/<id>")
def delete(id):
    contactoAEliminar = Contacto.query.get(id)
    db.session.delete(contactoAEliminar)
    db.session.commit()
    flash("contacto eliminado")
    return redirect(url_for('contactos.index'))

@contactosEnrutador.route("/formulario/")
def formulario():
    return render_template("formulario.html")

