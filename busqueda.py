from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('busqueda.html')

# Ruta para procesar la búsqueda
@app.route('/buscar', methods=['GET'])
def buscar():
    filtro = request.args.get('filtro')
    termino = request.args.get('termino')

    proyectos_encontrados = []

    # Abrir el archivo CSV y buscar los proyectos
    with open('proyectos.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for proyecto in csv_reader:
            if termino.lower() in proyecto[filtro].lower():
                proyectos_encontrados.append(proyecto)

    return render_template('resultado_busqueda.html', proyectos=proyectos_encontrados)

if __name__ == '__main__':
    app.run(debug=True)
