# src/controllers/departamento_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

# IMPORTAÇÕES CORRETAS
from src.server import db
from src.models import Departamento

departamento_bp = Blueprint("departamento_bp", __name__, url_prefix="/departamentos")


@departamento_bp.route("/listar")
def listar():
    registros = Departamento.query.order_by(Departamento.id.desc()).all()
    return render_template("list_departamentos.html", title="Departamentos", registros=registros)


@departamento_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template("form_departamento.html", title="Novo Departamento", registro=None)


@departamento_bp.route("/", methods=["POST"])
def criar():
    nome = request.form.get("nome")
    sigla = request.form.get("sigla")

    if not nome:
        flash("O nome é obrigatório.", "error")
        return redirect(url_for("departamento_bp.formulario"))

    novo = Departamento(nome=nome, sigla=sigla)

    db.session.add(novo)
    db.session.commit()

    flash("Departamento criado com sucesso!", "success")
    return redirect(url_for("departamento_bp.listar"))


@departamento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    departamento = Departamento.query.get_or_404(id)

    if request.method == "POST":
        departamento.nome = request.form.get("nome")
        departamento.sigla = request.form.get("sigla")

        db.session.commit()

        flash("Departamento atualizado com sucesso!", "success")
        return redirect(url_for("departamento_bp.listar"))

    return render_template(
        "form_departamento.html",
        title="Editar Departamento",
        registro=departamento
    )


@departamento_bp.route("/excluir/<int:id>")
def excluir(id):
    departamento = Departamento.query.get_or_404(id)

    db.session.delete(departamento)
    db.session.commit()

    flash("Departamento excluído com sucesso!", "success")
    return redirect(url_for("departamento_bp.listar"))
