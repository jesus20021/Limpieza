from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, session
from flask_session import Session
import plotly.express as px
import os
from datetime import datetime
from modelo_controlador.usuario import Usuario
from modelo_controlador.actividad import Actividad
from modelo_controlador.colonia import Colonia
from modelo_controlador.cuadrilla import Cuadrilla

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mi llave secreta xD'
app.config['SESSION_TYPE'] = 'filesystem'  # Puedes cambiar este tipo de almacenamiento según tus necesidades
Session(app)

@app.route("/")
def index():
    usuario = session.get("usuario", None)
    if usuario is None:
        return render_template('index.html')
    elif usuario.tipo == "admin":
        return redirect(url_for("admin"))
    elif usuario.tipo == "miembro":
        return redirect(url_for('miembro'))
    else:
        return redirect(url_for('menu'))
        
@app.route("/Login", methods=['POST'])
def login():
    session["usuario"] = Usuario.buscar(request.form.get("usuario"))
    usuario = session.get("usuario", None)
    print(request.form, usuario)
    if(usuario and usuario.contraseña == request.form.get("pass")):
        if usuario.tipo == "admin":
            return redirect(url_for("admin"))
        else:
            return redirect(url_for('menu'))
    else:
        return '''<script>
        alert("Usuario o Contraseña incorrectos");
        window.location.replace("/");
        </script>'''

@app.route("/Menu")
def menu():
    usuario = session.get("usuario", None)
    if usuario is not None:
        if usuario.tipo == "miembro":
            return redirect(url_for("miembro"))
        else:
            return render_template("menu.html", nombre = usuario.nombre)
    else:
        return redirect(url_for("index"))

@app.route("/Miembro")
def miembro():
    usuario = session.get("usuario", None)
    if usuario is not None:
        if usuario.tipo == "miembro":
            return render_template("menuMiembro.html", nombre = usuario.nombre)
        else:
            return redirect(url_for("menu"))
    else:
        return redirect(url_for("index"))

@app.route("/ActividadesAsignadas", methods={'post', 'get'})
def asignadas():
    usuario = session.get("usuario", None)
    if usuario is not None:
        actividades = Actividad.listarCuadrillaPendiente(usuario.cuadrilla)
        cuadrilla = Cuadrilla.buscar(usuario.cuadrilla)
        return render_template("asignadas.html", actividades = actividades, nombre = usuario.nombre, cuadrilla = cuadrilla.nombre)
    else:
        return redirect(url_for("index"))

@app.route("/actualizar", methods=["post"])
def actualizar():
    print("\n\n\n\n",request.files.to_dict())
    id = request.form.get('id')
    print(id)
    if len(id)==0:
        return '''<script>
        alert("No se seleccionó ninguna actividad");
        window.location.replace("/");
        </script>'''
    else:
        archivo = request.files['file']
        
        if archivo.filename == '':
            return '''<script>
        alert("No hay ninguna foto");
        window.location.replace("/");
        </script>'''
        directorio_destino = os.path.join(app.static_folder, "img")
        archivo.save(os.path.join(directorio_destino, archivo.filename))
        actividad = Actividad.buscar(id)
        actividad.foto = archivo.filename
        actividad.estado = "completada"
        actividad.fechaAcabado = datetime.now()
        actividad.actualizar()
        return '''<script>
        alert("Actividad actualizada correctamente");
        window.location.replace("/");
        </script>'''
    

@app.route("/getActividad", methods = {'post'})
def getActividad():
    actividad = Actividad.buscar(request.get_json()["id"])
    actividadJson = {
        'id':actividad.id, 
        'nombre':actividad.nombre, 
        'descripcion':actividad.descripcion, 
        'colonia':actividad.colonia, 
        'cuadrilla':actividad.cuadrilla, 
        'fechaPropuesta':actividad.fechaPropuesta, 
        'fechaCreacion':actividad.fechaCreacion, 
        'fechaAcabado':actividad.fechaAcabado, 
        'estado':actividad.estado, 
        'foto':actividad.foto
    }
    return jsonify(actividadJson)

@app.route("/getColonia", methods = {'post'})
def getColonia():
    colonia = Colonia.buscar(request.get_json()['id'])
    coloniaJson = {
        'id': colonia.id, 
        'codigoPostal':colonia.codigoPostal, 
        'nombre':colonia.nombre
    }
    return jsonify(coloniaJson)

@app.route("/ActividadesRealizadas")
def realizadas():
    usuario = session.get("usuario", None)
    if(usuario is not None):
        actividades = Actividad.listarCuadrilla(usuario.cuadrilla)
        cuadrilla = Cuadrilla.buscar(usuario.cuadrilla)
        return render_template("realizadas.html", nombre = usuario.nombre, actividades = actividades, cuadrilla = cuadrilla.nombre)
    else:
        return redirect(url_for("index"))

@app.route("/Admin")
def admin():
    usuario = session.get("usuario", None)
    if usuario is not None:
        if usuario.tipo == "admin":
            return render_template("menuAdmin.html", nombre = usuario.nombre)
        else:
            return redirect(url_for("menu"))
    else:
        return redirect(url_for("index"))

@app.route("/Actividades")
def actividades():
    usuario = session.get("usuario", None)
    if usuario is not None:
        if usuario.tipo == "admin":
            actividades = Actividad.listar()
            colonias = Colonia.listar()
            cuadrillas = Cuadrilla.listar()
            return render_template("actividades.html", nombre = usuario.nombre, actividades = actividades, colonias=colonias, cuadrillas = cuadrillas)

@app.route("/crearActividad", methods=['post'])
def crear():
    id = request.get_json()['id']
    nombre = request.get_json()['nombre']
    descripcion = request.get_json()['descripcion']
    colonia = request.get_json()['colonia']
    propuesta = request.get_json()['propuesta']
    cuadrilla = request.get_json()['cuadrilla']
    actividad = Actividad(id, nombre, descripcion, colonia, cuadrilla, propuesta, datetime.now(), None, "pendiente", None)
    if actividad.crear():
        return jsonify({'estado':'creado'})
    else:
        return jsonify({'estado':'error'})

@app.route("/actualizarActividad", methods=['post'])
def actualizarActividad():
    id = request.get_json()['id']
    nombre = request.get_json()['nombre']
    descripcion = request.get_json()['descripcion']
    colonia = request.get_json()['colonia']
    propuesta = request.get_json()['propuesta']
    cuadrilla = request.get_json()['cuadrilla']
    termino = request.get_json()['termino']
    actividad = Actividad.buscar(id)
    if actividad is None:
        return jsonify({'estado':'error'})
    actividad.descripcion = descripcion
    actividad.nombre = nombre
    actividad.colonia = colonia
    actividad.fechaPropuesta = propuesta
    actividad.cuadrilla = cuadrilla
    actividad.fechaAcabado = termino
    if actividad.actualizar():
        return jsonify({'estado':'creado'})
    else:
        return jsonify({'estado':'error'})
    
@app.route("/eliminarActividad", methods=['post'])
def eliminar():
    id = request.get_json()['id']
    actividad = Actividad.buscar(id)
    if actividad is None:
        return jsonify({'estado':'error'})
    if actividad.eliminar():
        return jsonify({'estado':'creado'})
    else:
        return jsonify({'estado':'error'})

@app.route("/Dashboard")
def dashboard():
    cuadrillas = Cuadrilla.listar()
    x = []
    y = []
    for i in cuadrillas:
        x.append(i.nombre)
        y.append(len(Actividad.listarCuadrilla(i.idCuadrilla)))
    data = {
        'Cuadrillas': x,
        'Actividades realizadas': y
    }

    fig = px.bar(data, x='Cuadrillas', y='Actividades realizadas', title='Actividades por cuadrilla')

    # Convierte la figura de Plotly en HTML
    graph_html = fig.to_html(full_html=False)

    return render_template('dashboard.html', graph_html=graph_html)

@app.route("/Logout")
def logout():
    session["usuario"] = None
    return redirect(url_for("index"))

if (__name__ == "__main__"):
    app.run(debug=True)