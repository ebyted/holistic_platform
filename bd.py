from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar la URI para SQLite (puedes usar PostgreSQL o MySQL cambiando la URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///holistic_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir los modelos de la base de datos
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    heart_rate = db.Column(db.Integer)
    stress_level = db.Column(db.Integer)
    sleep_hours = db.Column(db.Integer)
    preferences = db.relationship('Preferences', backref='patient', lazy=True)

class Preferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_preference = db.Column(db.String(50))
    meditation_type = db.Column(db.String(50))
    session_duration = db.Column(db.Integer)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)

class MeditationSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_type = db.Column(db.String(50))  # Ej. Profunda, Guiada, etc.
    duration = db.Column(db.Integer)  # Duración en minutos
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    patient = db.relationship('Patient', backref=db.backref('sessions', lazy=True))

# Crear la base de datos
with app.app_context():
    db.create_all()

# Endpoints para interactuar con la base de datos

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(
        name=data['name'],
        heart_rate=data['heart_rate'],
        stress_level=data['stress_level'],
        sleep_hours=data['sleep_hours']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Paciente agregado exitosamente"}), 201

@app.route('/add_preferences', methods=['POST'])
def add_preferences():
    data = request.get_json()
    new_preferences = Preferences(
        music_preference=data['music_preference'],
        meditation_type=data['meditation_type'],
        session_duration=data['session_duration'],
        patient_id=data['patient_id']
    )
    db.session.add(new_preferences)
    db.session.commit()
    return jsonify({"message": "Preferencias agregadas exitosamente"}), 201

@app.route('/add_session', methods=['POST'])
def add_session():
    data = request.get_json()
    new_session = MeditationSession(
        session_type=data['session_type'],
        duration=data['duration'],
        patient_id=data['patient_id']
    )
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"message": "Sesión de meditación agregada exitosamente"}), 201

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    
    # Aquí iría la lógica para calcular la recomendación (IA, análisis de datos, etc.)
    # Por ahora, enviamos una recomendación de ejemplo.
    
    recommendation = {
        "meditation_type": "Meditación Guiada",
        "duration": "20 minutos",
        "music": "Sonido de agua"
    }
    return jsonify(recommendation)

if __name__ == '__main__':
    app.run(debug=True)
