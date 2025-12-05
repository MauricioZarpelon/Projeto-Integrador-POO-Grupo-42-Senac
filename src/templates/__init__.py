class PessoaJuridica(Pessoa):
    def __init__(self, razao_social, cnpj, nome_fantasia=None, endereco=None, telefone=None):
        super().__init__(nome=razao_social, endereco=endereco, telefone=telefone)
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
