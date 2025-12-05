# reset_database.py
import os
import sys

# Adiciona o diretório src ao path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from server import db, create_app

# Cria a aplicação
app = create_app()

with app.app_context():
    # Recria todas as tabelas
    db.drop_all()
    db.create_all()

    print("✅ Banco de dados recriado com sucesso!")
    print("✅ Todas as tabelas foram atualizadas.")

    # Verifica a estrutura da tabela professores
    from sqlalchemy import inspect

    inspector = inspect(db.engine)
    columns = inspector.get_columns('professores')

    print("\n📊 Estrutura da tabela 'professores':")
    for column in columns:
        print(f"  - {column['name']} ({column['type']}) - Nullable: {column['nullable']}")