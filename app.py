from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inventario como una lista vacía
inventario = []

# Ruta principal (muestra el inventario)
@app.route('/')
def index():
    return render_template('index.html', inventario=inventario)

# Ruta para agregar un producto
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    producto = {"nombre": nombre, "cantidad": cantidad}
    inventario.append(producto)
    return redirect(url_for('index'))

# Ruta para eliminar un producto
@app.route('/eliminar/<nombre>')
def eliminar_producto(nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            break
    return redirect(url_for('index'))

# Ruta para buscar un producto
@app.route('/buscar', methods=['POST'])
def buscar_producto():
    nombre = request.form['nombre']
    for producto in inventario:
        if producto['nombre'] == nombre:
            return render_template('buscar.html', producto=producto)
    return render_template('buscar.html', producto=None)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
