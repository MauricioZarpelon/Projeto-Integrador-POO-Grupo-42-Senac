from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "online",
        "message": "API do Projeto Integrador - Deploy PythonAnywhere bem-sucedido!"
    }

if __name__ == "__main__":
    app.run()
