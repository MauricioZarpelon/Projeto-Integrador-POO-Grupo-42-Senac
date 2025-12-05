from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.server import db
from src.models import Aluno, PessoaFisica

aluno_bp = Blueprint("aluno_bp", __name__, url_prefix="/alunos")


@aluno_bp.route("/listar")
def listar():
    registros = Aluno.query.order_by(Aluno.id.desc()).all()
    return render_template(
        "list_alunos.html",
        title="Alunos",
        registros=registros
    )


@aluno_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template(
        "form_aluno.html",
        title="Novo Aluno",
        registro=None
    )


@aluno_bp.route("/", methods=["POST"])
def criar():
    curso_id = request.form.get("curso_id")
    matricula = request.form.get("matricula")
    ano_ingresso = request.form.get("ano_ingresso")

    if not curso_id or not matricula:
        flash("Curso e matrícula são obrigatórios.", "error")
        return redirect(url_for("aluno_bp.formulario"))

    # Tenta usar uma pessoa física existente, ou usa um valor padrão
    pessoa_padrao = PessoaFisica.query.first()
    pessoa_fisica_id = pessoa_padrao.id if pessoa_padrao else 1

    novo = Aluno(
        pessoa_fisica_id=pessoa_fisica_id,  # Usa pessoa física disponível ou valor padrão
        curso_id=int(curso_id),
        matricula=matricula,
        ano_ingresso=int(ano_ingresso) if ano_ingresso else None
    )

    db.session.add(novo)
    db.session.commit()

    flash("Aluno criado com sucesso!", "success")
    return redirect(url_for("aluno_bp.listar"))


@aluno_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    registro = Aluno.query.get_or_404(id)

    if request.method == "POST":
        registro.curso_id = int(request.form.get("curso_id"))
        registro.matricula = request.form.get("matricula")
        ano_ingresso = request.form.get("ano_ingresso")
        registro.ano_ingresso = int(ano_ingresso) if ano_ingresso else None

        db.session.commit()
        flash("Aluno atualizado com sucesso!", "success")

        return redirect(url_for("aluno_bp.listar"))

    return render_template(
        "form_aluno.html",
        title="Editar Aluno",
        registro=registro
    )


@aluno_bp.route("/excluir/<int:id>")
def excluir(id):
    registro = Aluno.query.get_or_404(id)

    db.session.delete(registro)
    db.session.commit()

    flash("Aluno excluído com sucesso!", "success")
    return redirect(url_for("aluno_bp.listar"))