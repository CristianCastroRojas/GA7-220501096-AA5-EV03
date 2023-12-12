from flask import Flask, render_template, request, redirect
import json  # Agregamos la importación de json

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el formulario de registro
@app.route('/registrar_cliente', methods=['POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        nombre_comercial = request.form['nombreComercial'].strip()
        correo = request.form['correoElectronico'].strip()
        telefono = request.form['telefono'].strip()
        ciudad = request.form['ciudad'].strip()
        comentarios = request.form['comentarios']

        # Crea un diccionario con los datos del cliente
        cliente_data = {
            'nombre': nombre,
            'apellido': apellido,
            'nombre_comercial': nombre_comercial,
            'correo': correo,
            'telefono': telefono,
            'ciudad': ciudad,
            'comentarios': comentarios
        }

        # Abre el archivo JSON (creándolo si no existe)
        with open('clientes.json', 'a', encoding='utf-8') as file:
            # Escribe el diccionario en el archivo JSON
            file.write(json.dumps(cliente_data, ensure_ascii=False) + '\n')

        # Redirige al usuario a la página de agradecimiento
        return redirect('/thanks')

# Ruta para la página de agradecimiento
@app.route('/thanks')
def agradecimiento():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
