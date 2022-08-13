from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Gaby acho que deu bom aqui!!"

if __name__ == '__main__':
    app.run()