from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludar', methods=['POST'])
def saludar():
    nombre = request.form['nombre']
    return f'Hola {nombre}!'

@app.route('/buen_dia', methods=['POST'])
def saludo_buen_dia():
    nombre = request.form['nombre']
    return f'Buen dia. Como estas {nombre}!'

@app.route('/buenas_noche', methods=['POST'])
def saludo_buenas_noche():
    nombre = request.form['nombre']
    return f'Buen dia. Como estas {nombre}!'

if __name__ == '__main__':
    app.run()