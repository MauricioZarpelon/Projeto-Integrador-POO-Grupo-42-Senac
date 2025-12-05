# src/controllers/pessoa_juridica_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

# IMPORTAÇÕES CORRETAS
from src.server import db
from src.models import PessoaJuridica

pessoa_juridica_bp = Blueprint(
    "pessoa_juridica_bp",
    __name__,
    url_prefix="/pessoas-juridicas"
)


@pessoa_juridica_bp.route("/listar")
def listar():
    registros = PessoaJuridica.query.order_by(PessoaJuridica.id.desc()).all()
    return render_template(
        "list_pessoas_juridicas.html",
        title="Pessoas Jurídicas",
        registros=registros
    )


@pessoa_juridica_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template(
        "form_pessoa_juridica.html",
        title="Nova Pessoa Jurídica",
        registro=None
    )


@pessoa_juridica_bp.route("/", methods=["POST"])
def criar():
    razao_social = request.form.get("razao_social")
    cnpj = request.form.get("cnpj")
    nome_fantasia = request.form.get("nome_fantasia")

    # CORREÇÃO: Adicionar campos da tabela Pessoa
    nome = request.form.get("nome") or razao_social  # Usa razão social como fallback
    endereco = request.form.get("endereco", "")
    telefone = request.form.get("telefone", "")

    if not razao_social or not cnpj:
        flash("Razão social e CNPJ são obrigatórios.", "error")
        return redirect(url_for("pessoa_juridica_bp.formulario"))

    nova = PessoaJuridica(
        # Campos da tabela Pessoa (OBRIGATÓRIOS)
        nome=nome,  # ← CORREÇÃO: Campo obrigatório da tabela pessoas
        endereco=endereco,
        telefone=telefone,
        tipo="Juridica",  # ← CORREÇÃO: Define o tipo para herança

        # Campos específicos da PessoaJuridica
        razao_social=razao_social,
        cnpj=cnpj,
        nome_fantasia=nome_fantasia
    )

    db.session.add(nova)
    db.session.commit()

    flash("Pessoa Jurídica criada com sucesso!", "success")
    return redirect(url_for("pessoa_juridica_bp.listar"))


@pessoa_juridica_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    registro = PessoaJuridica.query.get_or_404(id)

    if request.method == "POST":
        # CORREÇÃO: Atualizar também campos da tabela Pessoa
        registro.nome = request.form.get("nome") or request.form.get("razao_social")
        registro.endereco = request.form.get("endereco", "")
        registro.telefone = request.form.get("telefone", "")

        # Campos específicos
        registro.razao_social = request.form.get("razao_social")
        registro.cnpj = request.form.get("cnpj")
        registro.nome_fantasia = request.form.get("nome_fantasia")

        db.session.commit()
        flash("Registro atualizado com sucesso!", "success")

        return redirect(url_for("pessoa_juridica_bp.listar"))

    return render_template(
        "form_pessoa_juridica.html",
        title="Editar Pessoa Jurídica",
        registro=registro
    )


@pessoa_juridica_bp.route("/excluir/<int:id>")
def excluir(id):
    registro = PessoaJuridica.query.get_or_404(id)

    db.session.delete(registro)
    db.session.commit()

    flash("Registro excluído com sucesso!", "success")
    return redirect(url_for("pessoa_juridica_bp.listar"))