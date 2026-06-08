from flask import Flask, request, jsonify, render_template
from sistema import consultar_top_carreras

app = Flask(__name__)

# Ruta principal: Muestra la interfaz gráfica
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de la API: Recibe datos de JS y consulta a Prolog
@app.route('/api/inferir', methods=['POST'])
def inferir():
    datos = request.json
    habilidades = tuple(datos.get('habilidades', []))
    intereses = tuple(datos.get('intereses', []))
    
    # Aquí es donde Python usa funcional y consulta a Prolog
    resultados_prolog = consultar_top_carreras(habilidades, intereses)
    
    # Convertimos el resultado a JSON para mandarlo a la web
    respuesta = []
    for r in resultados_prolog:
        respuesta.append({
            "nombre": r.carrera,
            "puntaje": r.puntaje,
            "desc": r.descripcion
        })
    
        respuesta_limpia = []
        for item in respuesta: # Asumiendo que "respuesta" es tu lista original
            # Limpiamos el nombre
            nombre_limpio = item["nombre"]
            if isinstance(nombre_limpio, bytes):
                nombre_limpio = nombre_limpio.decode('utf-8')
                
            
            desc_limpia = item["desc"]
            if isinstance(desc_limpia, bytes):
                desc_limpia = desc_limpia.decode('utf-8')
                
            # Guardamos los datos ya como texto normal
            respuesta_limpia.append({
                "nombre": nombre_limpio,
                "desc": desc_limpia,
                "puntaje": item["puntaje"]
            })

        return jsonify(respuesta_limpia)
        
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True, threaded=False)

