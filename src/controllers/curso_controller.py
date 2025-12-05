# src/controllers/curso_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

# IMPORTAÇÕES CORRETAS
from src.server import db
from src.models import Curso

curso_bp = Blueprint("curso_bp", __name__, url_prefix="/cursos")


@curso_bp.route("/listar")
def listar():
    registros = Curso.query.order_by(Curso.id.desc()).all()
    return render_template("list_cursos.html", title="Cursos", registros=registros)


@curso_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template("form_curso.html", title="Novo Curso", registro=None)


@curso_bp.route("/", methods=["POST"])
def criar():
    nome = request.form.get("nome")
    duracao = request.form.get("duracao_semestres")

    if not nome or not duracao:
        flash("Nome e duração são obrigatórios.", "error")
        return redirect(url_for("curso_bp.formulario"))

    novo = Curso(nome=nome, duracao_semestres=int(duracao))

    db.session.add(novo)
    db.session.commit()

    flash("Curso criado com sucesso!", "success")
    return redirect(url_for("curso_bp.listar"))


@curso_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    curso = Curso.query.get_or_404(id)

    if request.method == "POST":
        curso.nome = request.form.get("nome")
        curso.duracao_semestres = int(request.form.get("duracao_semestres"))

        db.session.commit()

        flash("Curso atualizado com sucesso!", "success")
        return redirect(url_for("curso_bp.listar"))

    return render_template(
        "form_curso.html",
        title="Editar Curso",
        registro=curso
    )


@curso_bp.route("/excluir/<int:id>")
def excluir(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()

    flash("Curso excluído com sucesso!", "success")
    return redirect(url_for("curso_bp.listar"))
