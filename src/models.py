from src.server import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), nullable=False, unique=True)
    departamento = db.Column(db.String(100))
    titulacao = db.Column(db.String(100))

class Pessoa(db.Model):
    __tablename__ = "pessoas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    endereco = db.Column(db.String(300))
    telefone = db.Column(db.String(50))
    tipo = db.Column(db.String(50))

class PessoaFisica(Pessoa):
    __tablename__ = "pessoas_fisicas"

    id = db.Column(db.Integer, db.ForeignKey("pessoas.id"), primary_key=True)
    cpf = db.Column(db.String(20), nullable=False)
    rg = db.Column(db.String(50))
    data_nascimento = db.Column(db.Date)

class PessoaJuridica(Pessoa):
    __tablename__ = "pessoas_juridicas"

    id = db.Column(db.Integer, db.ForeignKey("pessoas.id"), primary_key=True)
    cnpj = db.Column(db.String(30), nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    nome_fantasia = db.Column(db.String(200))

class Curso(db.Model):
    __tablename__ = "cursos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    duracao_semestres = db.Column(db.Integer)

class Departamento(db.Model):
    __tablename__ = "departamentos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    sigla = db.Column(db.String(10))

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    pessoa_fisica_id = db.Column(db.Integer, db.ForeignKey('pessoas_fisicas.id'))
    matricula = db.Column(db.String(100), nullable=False)
    ano_ingresso = db.Column(db.Integer)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))

class Fornecedor(db.Model):
    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(30), nullable=False)
    razao_social = db.Column(db.String(200), nullable=False)
    ramo_atividade = db.Column(db.String(200))
    contato = db.Column(db.String(200))