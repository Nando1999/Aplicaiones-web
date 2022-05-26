#Importar la biblioteca de flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


#Arreglo guardar todos los datos
lista_tareas = []

#Controlador 
@app.route('/')
def index():
    return render_template('index3.html', lista_tareas=lista_tareas)


#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)