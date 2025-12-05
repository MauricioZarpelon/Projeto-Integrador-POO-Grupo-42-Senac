# src/controllers/fornecedor_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.server import db
from src.models import Fornecedor

fornecedor_bp = Blueprint(
    "fornecedor_bp",
    __name__,
    url_prefix="/fornecedores"
)


@fornecedor_bp.route("/listar")
def listar():
    registros = Fornecedor.query.order_by(Fornecedor.id.desc()).all()
    return render_template(
        "list_fornecedores.html",
        title="Fornecedores",
        registros=registros
    )


@fornecedor_bp.route("/novo", methods=["GET"])
def formulario():
    return render_template(
        "form_fornecedor.html",
        title="Novo Fornecedor",
        registro=None
    )


@fornecedor_bp.route("/", methods=["POST"])
def criar():
    cnpj = request.form.get("cnpj")
    nome_empresa = request.form.get("nome_empresa")
    ramo_atividade = request.form.get("ramo_atividade")
    contato = request.form.get("contato")

    if not cnpj or not nome_empresa:
        flash("CNPJ e Nome da Empresa são obrigatórios.", "error")
        return redirect(url_for("fornecedor_bp.formulario"))

    try:
        # Remove formatação do CNPJ
        cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')

        # Cria o Fornecedor diretamente (sem relacionamento)
        novo = Fornecedor(
            cnpj=cnpj_limpo,
            razao_social=nome_empresa,
            ramo_atividade=ramo_atividade,
            contato=contato
        )

        db.session.add(novo)
        db.session.commit()

        flash("Fornecedor criado com sucesso!", "success")
        return redirect(url_for("fornecedor_bp.listar"))

    except Exception as e:
        db.session.rollback()
        flash(f"Erro ao criar fornecedor: {str(e)}", "error")
        return redirect(url_for("fornecedor_bp.formulario"))


@fornecedor_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    registro = Fornecedor.query.get_or_404(id)

    if request.method == "POST":
        cnpj = request.form.get("cnpj")
        nome_empresa = request.form.get("nome_empresa")
        ramo_atividade = request.form.get("ramo_atividade")
        contato = request.form.get("contato")

        if not cnpj or not nome_empresa:
            flash("CNPJ e Nome da Empresa são obrigatórios.", "error")
            return redirect(url_for("fornecedor_bp.editar", id=id))

        try:
            # Remove formatação do CNPJ
            cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')

            # Atualiza diretamente
            registro.cnpj = cnpj_limpo
            registro.razao_social = nome_empresa
            registro.ramo_atividade = ramo_atividade
            registro.contato = contato

            db.session.commit()
            flash("Fornecedor atualizado com sucesso!", "success")
            return redirect(url_for("fornecedor_bp.listar"))

        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao atualizar fornecedor: {str(e)}", "error")
            return redirect(url_for("fornecedor_bp.editar", id=id))

    return render_template(
        "form_fornecedor.html",
        title="Editar Fornecedor",
        registro=registro
    )


@fornecedor_bp.route("/excluir/<int:id>")
def excluir(id):
    registro = Fornecedor.query.get_or_404(id)

    db.session.delete(registro)
    db.session.commit()

    flash("Fornecedor excluído com sucesso!", "success")
    return redirect(url_for("fornecedor_bp.listar"))