# src/controllers/pessoa_fisica_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

from src.server import db
from src.models import PessoaFisica

pessoa_fisica_bp = Blueprint(
    "pessoa_fisica_bp",
    __name__,
    url_prefix="/pessoas-fisicas"
)


@pessoa_fisica_bp.route("/listar")
def listar():
    registros = PessoaFisica.query.order_by(PessoaFisica.id.desc()).all()
    return render_template(
        "list_pessoas_fisicas.html",
        title="Pessoas Físicas",
        registros=registros
    )


@pessoa_fisica_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template(
        "form_pessoa_fisica.html",
        title="Nova Pessoa Física",
        registro=None
    )


@pessoa_fisica_bp.route("/", methods=["POST"])
def criar():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    endereco = request.form.get("endereco")
    telefone = request.form.get("telefone")

    if not nome or not cpf:
        flash("Nome e CPF são obrigatórios.", "error")
        return redirect(url_for("pessoa_fisica_bp.formulario"))

    nova = PessoaFisica(
        nome=nome,
        cpf=cpf,
        endereco=endereco,
        telefone=telefone
    )

    db.session.add(nova)
    db.session.commit()

    flash("Pessoa Física criada com sucesso!", "success")
    return redirect(url_for("pessoa_fisica_bp.listar"))


@pessoa_fisica_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    pessoa = PessoaFisica.query.get_or_404(id)

    if request.method == "POST":
        pessoa.nome = request.form.get("nome")
        pessoa.cpf = request.form.get("cpf")
        pessoa.endereco = request.form.get("endereco")
        pessoa.telefone = request.form.get("telefone")

        db.session.commit()
        flash("Registro atualizado com sucesso!", "success")
        return redirect(url_for("pessoa_fisica_bp.listar"))

    return render_template(
        "form_pessoa_fisica.html",
        title="Editar Pessoa Física",
        registro=pessoa
    )


@pessoa_fisica_bp.route("/excluir/<int:id>")
def excluir(id):
    pessoa = PessoaFisica.query.get_or_404(id)

    db.session.delete(pessoa)
    db.session.commit()

    flash("Registro excluído com sucesso!", "success")
    return redirect(url_for("pessoa_fisica_bp.listar"))
