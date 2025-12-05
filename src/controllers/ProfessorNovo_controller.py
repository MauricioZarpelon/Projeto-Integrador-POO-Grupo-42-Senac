from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.server import db
from src.models import Professor

professor_bp = Blueprint("professor_bp", __name__, url_prefix="/professores")


@professor_bp.route("/listar")
def listar():
    registros = Professor.query.order_by(Professor.id.desc()).all()
    return render_template(
        "list_professores.html",
        title="Professores",
        registros=registros
    )


@professor_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template(
        "form_professor.html",
        title="Novo Professor",
        registro=None
    )


@professor_bp.route("/", methods=["POST"])
def criar():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    departamento = request.form.get("departamento")
    titulacao = request.form.get("titulacao")

    if not nome or not matricula:
        flash("Nome e matrícula são obrigatórios.", "error")
        return redirect(url_for("professor_bp.formulario"))

    # Cria o professor sem usar o construtor personalizado
    novo = Professor()
    novo.nome = nome
    novo.matricula = matricula
    novo.departamento = departamento
    novo.titulacao = titulacao

    db.session.add(novo)
    db.session.commit()

    flash("Professor criado com sucesso!", "success")
    return redirect(url_for("professor_bp.listar"))


@professor_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    registro = Professor.query.get_or_404(id)

    if request.method == "POST":
        registro.nome = request.form.get("nome")
        registro.matricula = request.form.get("matricula")
        registro.departamento = request.form.get("departamento")
        registro.titulacao = request.form.get("titulacao")

        db.session.commit()
        flash("Professor atualizado com sucesso!", "success")

        return redirect(url_for("professor_bp.listar"))

    return render_template(
        "form_professor.html",
        title="Editar Professor",
        registro=registro
    )


@professor_bp.route("/excluir/<int:id>")
def excluir(id):
    registro = Professor.query.get_or_404(id)

    db.session.delete(registro)
    db.session.commit()

    flash("Professor excluído com sucesso!", "success")
    return redirect(url_for("professor_bp.listar"))