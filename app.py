from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Gaby acho que deu bom aqui!! To no Docker"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)