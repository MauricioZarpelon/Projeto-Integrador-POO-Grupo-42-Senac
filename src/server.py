from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    print(">>> Carregando server.py correto")
    app = Flask(__name__)
    app.config.from_object("src.config.Config")

    # INICIALIZAÇÃO CORRETA DO DB
    db.init_app(app)

    with app.app_context():
        # Importar models DEPOIS de init_app
        import src.models

        from src.controllers.home_controller import home_bp
        from src.controllers.aluno_controller import aluno_bp
        from src.controllers.curso_controller import curso_bp
        from src.controllers.departamento_controller import departamento_bp
        from src.controllers.fornecedor_controller import fornecedor_bp
        from src.controllers.pessoa_fisica_controller import pessoa_fisica_bp
        from src.controllers.pessoa_juridica_controller import pessoa_juridica_bp
        from src.controllers.ProfessorNovo_controller import professor_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(aluno_bp)
        app.register_blueprint(curso_bp)
        app.register_blueprint(departamento_bp)
        app.register_blueprint(fornecedor_bp)
        app.register_blueprint(pessoa_fisica_bp)
        app.register_blueprint(pessoa_juridica_bp)
        app.register_blueprint(professor_bp)

        # Criar tabelas DENTRO do app_context
        db.create_all()

    return app