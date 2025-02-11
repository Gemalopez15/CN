from flask import Flask

#crear isinstancia
app = Flask(__name__)

#ruta raiz
@app.route('/alumnos')
def hola_mundo():
    return 'Aquí se listan los alumnos'
if __name__ == '__main__':
    app.run(debug=True)