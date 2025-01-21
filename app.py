from flask import Flask, render_template, request, jsonify
from model.recommender import get_recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Obtener los datos del formulario
    health_data = request.json['health_data']
    # Llamar a la función de recomendación basada en IA
    recommendation = get_recommendation(health_data)
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
