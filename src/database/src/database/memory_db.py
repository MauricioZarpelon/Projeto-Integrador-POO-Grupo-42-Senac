# Banco de dados em memória (simples)
db = {
    "pessoas_fisicas": [],
    "pessoas_juridicas": [],
    "alunos": [],
    "professores": [],
    "fornecedores": []
}

# Função auxiliar para gerar IDs automáticos
def next_id(table_name: str):
    return len(db[table_name]) + 1
