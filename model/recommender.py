def get_recommendation(health_data):
    # Asegurarse de que el valor sea un número entero
    heart_rate = int(health_data['heart_rate'])
    stress_level = int(health_data['stress_level'])
    
    # Lógica de recomendación basada en el ritmo cardíaco
    if heart_rate < 60:
        return "Recomendamos una meditación suave de 10 minutos."
    elif heart_rate > 100:
        return "Te recomendamos hacer una meditación profunda para relajar tu mente."
    else:
        return "Una meditación de 15 minutos podría ser ideal para ti."
