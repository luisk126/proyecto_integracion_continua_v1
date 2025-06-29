from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    asistencias = db.relationship('Asistencia', backref='estudiante', lazy=True)

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, default=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)

    def __repr__(self):
        return f'<Asistencia {self.fecha} - {"Presente" if self.presente else "Ausente"}>'