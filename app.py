from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Estudiante, Asistencia
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asistencia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

db.init_app(app)

# Crear tablas en la base de datos
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        
        # Verificar si el email ya existe
        if Estudiante.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'error')
            return redirect(url_for('registrar_estudiante'))
        
        nuevo_estudiante = Estudiante(nombre=nombre, email=email)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        
        flash('Estudiante registrado con éxito', 'success')
        return redirect(url_for('index'))
    
    return render_template('registrar.html')

@app.route('/asistencia/<int:estudiante_id>', methods=['GET', 'POST'])
def gestionar_asistencia(estudiante_id):
    estudiante = Estudiante.query.get_or_404(estudiante_id)
    
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        presente = 'presente' in request.form
        
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de fecha incorrecto', 'error')
            return redirect(url_for('gestionar_asistencia', estudiante_id=estudiante_id))
        
        # Verificar si ya existe registro para esa fecha
        if Asistencia.query.filter_by(estudiante_id=estudiante_id, fecha=fecha).first():
            flash('Ya existe un registro de asistencia para esta fecha', 'error')
            return redirect(url_for('gestionar_asistencia', estudiante_id=estudiante_id))
        
        nueva_asistencia = Asistencia(
            fecha=fecha,
            presente=presente,
            estudiante_id=estudiante_id
        )
        
        db.session.add(nueva_asistencia)
        db.session.commit()
        
        flash('Asistencia registrada con éxito', 'success')
        return redirect(url_for('gestionar_asistencia', estudiante_id=estudiante_id))
    
    asistencias = Asistencia.query.filter_by(estudiante_id=estudiante_id).order_by(Asistencia.fecha.desc()).all()
    return render_template('asistencia.html', estudiante=estudiante, asistencias=asistencias)

if __name__ == '__main__':
    app.run(debug=True)