# test_professor.py
import os
import sys

sys.path.append(os.getcwd())

from src.server import db, create_app

app = create_app()

with app.app_context():
    try:
        from src.models import Professor

        print("🎯 Testando criação de professor...")

        # Tenta criar um professor
        professor = Professor()
        professor.nome = "Professor Teste"
        professor.matricula = "12345"
        professor.departamento = "Ciência da Computação"
        professor.titulacao = "Doutorado"

        db.session.add(professor)
        db.session.commit()

        print("✅ Professor criado com sucesso!")

        # Verifica se foi salvo
        professores = Professor.query.all()
        print(f"✅ Total de professores: {len(professores)}")

        # Mostra a estrutura da tabela
        from sqlalchemy import inspect

        inspector = inspect(db.engine)

        print("\n📊 Estrutura da tabela 'professores':")
        columns = inspector.get_columns('professores')
        for column in columns:
            print(f"  - {column['name']} ({column['type']}) - Nullable: {column['nullable']}")

    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback

        traceback.print_exc()