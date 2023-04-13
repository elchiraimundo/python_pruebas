from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludar', methods=['POST'])
def saludar():
    nombre = request.form['nombre']
    return f'Hola {nombre}!'

if __name__ == '__main__':
    app.run()