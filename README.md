
[readme_V2 (3) (1).md](https://github.com/user-attachments/files/23545990/readme_V2.3.1.md)
# 🧩 Projeto Integrador — Desenvolvimento de Sistemas Orientado a Objetos

<div align="center">

<!-- ![Java](https://img.shields.io/badge/Java-17+-orange?style=for-the-badge&logo=java)
![UML](https://img.shields.io/badge/UML-Modelagem-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge) -->

**Centro Universitário Senac**  
Programação Orientada a Objetos | 2025

</div>


## 🧠 Objetivo do Projeto

O projeto tem como objetivo aplicar os conceitos de **Programação Orientada a Objetos (POO)** e **modelagem UML** no desenvolvimento de um sistema voltado ao **cadastro de pessoas e entidades**.  

O sistema foi planejado para permitir o cadastro e gerenciamento de:
- Pessoas Físicas  
- Pessoas Jurídicas  
- Alunos  
- Professores  
- Fornecedores  

---

## 👥 Integrantes do Grupo

| Nome | GitHub |
|------|--------|
| Gabriel Barreto Fragoso | [@gabriel-usuario] https://github.com/barretao00 |
| Miryam da Silva Souza | [@miryam-usuario] https://github.com/Miryamsilva
| Thais Helena Bezerra da Silva | [@thais-usuario]  https://github.com/thaishbs
| Gustavo Henrique de Souza | [@gustavo-usuario] https://github.com/gustavohsw |
| Cristiano Reis Santos | [@cristiano-usuario] https://github.com/CrisRSantos|
| Roger Vinicius Teixeira Seixas Cruz | [@roger-usuario] https://github.com/RogerVCruz |
| Mauricio Zarpelon Antunes dos Santos | [@mauricio-usuario] https://github.com/MauricioZarpelon | | Responsável pelo Repositório |


---

## 🎯 Funcionalidades do Sistema

O sistema permite o cadastro e gerenciamento de:

- 👤 **Pessoas Físicas** - Cadastro de indivíduos com dados pessoais
- 🏢 **Pessoas Jurídicas** - Cadastro de empresas e organizações
- 🎓 **Alunos** - Gerenciamento de alunos vinculados a cursos
- 👨‍🏫 **Professores** - Cadastro de docentes e suas informações acadêmicas
- 🏭 **Fornecedores** - Registro de fornecedores e seus serviços

---

## 📐 Fase 1: Modelagem UML

### Diagrama de Casos de Uso

O diagrama abaixo representa as interações entre o **Administrador do Sistema** e os diferentes módulos de cadastro:

![Diagrama de Casos de Uso](./diagramas/diagrama-casos-uso.png)

**Casos de Uso Implementados:**

#### 👤 UC01: Cadastrar Pessoa Física
- **Ator Principal:** Administrador do Sistema
- **Pré-condições:** Administrador autenticado com permissões de cadastro
- **Fluxo Principal:**
  1. Administrador seleciona "Pessoa Física"
  2. Preenche formulário (Nome, CPF, RG, Data de Nascimento, Endereço, Telefone)
  3. Sistema valida os dados (formato e unicidade do CPF)
  4. Sistema armazena os dados
  5. Exibe mensagem: "Cadastro realizado com sucesso!"

#### 🏢 UC02: Cadastrar Pessoa Jurídica
- **Ator Principal:** Administrador do Sistema
- **Pré-condições:** Administrador autenticado
- **Fluxo Principal:**
  1. Administrador seleciona "Nova Pessoa Jurídica"
  2. Preenche dados (Razão Social, Nome Fantasia, CNPJ,)
  3. Sistema valida CNPJ (formato e unicidade)
  4. Sistema armazena os dados
  5. Exibe mensagem de sucesso

**Fluxo Alternativo:** Se CNPJ já existe, operação é bloqueada com mensagem de erro.

#### 🎓 UC03: Cadastrar Aluno
- **Ator Principal:** Administrador do Sistema
- **Pré-condições:** Curso já cadastrado no sistema
- **Fluxo Principal:**
  1. Administrador seleciona "Cadastrar Aluno"
  2. Preenche dados pessoais (herda de Pessoa Física) e acadêmicos (Matrícula, Curso, Ano de Ingresso)
  3. Sistema valida unicidade de CPF e Matrícula
  4. Cria associação entre Pessoa Física e Aluno
  5. Exibe confirmação

**Fluxo Alternativo:** Matrícula duplicada bloqueia operação.

#### 👨‍🏫 UC04: Cadastrar Professor
- **Ator Principal:** Administrador do Sistema
- **Pré-condições:** Departamento já cadastrado
- **Fluxo Principal:**
  1. Administrador seleciona "Cadastrar Professor"
  2. Preenche dados pessoais e funcionais (Departamento, Titulação)
  3. Sistema valida existência do Departamento e unicidade do CPF
  4. Cria associação entre Pessoa Física e Professor
  5. Exibe sucesso

**Fluxo Alternativo:** Departamento inválido bloqueia operação.

#### 🏭 UC05: Cadastrar Fornecedor
- **Ator Principal:** Administrador do Sistema
- **Pré-condições:** Administrador autenticado
- **Fluxo Principal:**
  1. Administrador seleciona "Cadastrar Fornecedor"
  2. Preenche dados da empresa e específicos (Ramo de Atividade, Contato)
  3. Sistema valida unicidade do CNPJ
  4. Cria associação entre Pessoa Jurídica e Fornecedor
  5. Exibe confirmação

---

### 📋 Diagrama de Classes

O diagrama de classes apresenta a estrutura completa do sistema, aplicando os princípios de **herança**, **polimorfismo** e **composição**:

![Diagrama de Classes](./diagramas/diagrama-classes.png)


### Visão Geral


#### Hierarquia de Classes

```
Pessoa (abstrata)
├── PessoaFisica
│   ├── Aluno (associação)
│   └── Professor (associação)
└── PessoaJuridica
    └── Fornecedor (associação)

Curso (independente)
└── Aluno (relacionamento)

Departamento (independente)
└── Professor (relacionamento)
```

---

### 📦 Detalhamento das Classes

### 🔸 Classe Abstrata: Pessoa

**Responsabilidade:** Classe base que define atributos e comportamentos comuns a todas as pessoas no sistema.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `nome` | String | Nome completo da pessoa |
| `endereco` | String | Endereço residencial ou comercial |
| `telefone` | String | Número de telefone para contato |

**Métodos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Persiste os dados da pessoa no banco |
| `+validar()` | void | Valida os dados obrigatórios |
| `+buscarPorCPF()` | void | Busca registro por CPF |

**Características:**
- ✅ Classe abstrata (não pode ser instanciada diretamente)
- ✅ Implementa padrão Template Method
- ✅ Define contrato para classes filhas

---

### 🔹 Classe: PessoaFisica

**Herda de:** Pessoa

**Responsabilidade:** Representa indivíduos cadastrados no sistema (cidadãos).

**Atributos Próprios:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `cpf` | String | CPF no formato 000.000.000-00 |
| `rg` | String | Número do RG |
| `dataNascimento` | Date | Data de nascimento |

**Métodos Herdados + Sobrescritos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Salva pessoa física (sobrescreve método da classe pai) |
| `+validar()` | void | Valida CPF, RG e data de nascimento |
| `+buscarPorCPF()` | void | Busca pessoa física por CPF |

**Validações:**
- ✅ CPF deve ser válido e único no sistema
- ✅ RG deve estar preenchido
- ✅ Data de nascimento deve ser anterior à data atual

---

### 🔹 Classe: PessoaJuridica

**Herda de:** Pessoa

**Responsabilidade:** Representa empresas e organizações cadastradas no sistema.

**Atributos Próprios:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `cnpj` | String | CNPJ no formato 00.000.000/0000-00 |
| `razaoSocial` | String | Razão social da empresa |
| `nomeFantasia` | String | Nome fantasia (opcional) |

**Métodos Herdados + Sobrescritos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Salva pessoa jurídica |
| `+validar()` | void | Valida CNPJ e razão social |
| `+buscarPorCNPJ()` | void | Busca empresa por CNPJ |

**Validações:**
- ✅ CNPJ deve ser válido e único
- ✅ Razão Social deve estar preenchida
- ✅ Nome Fantasia é opcional

---

### 🔹 Classe: Aluno

**Associada a:** PessoaFisica (composição)

**Responsabilidade:** Gerenciar informações acadêmicas de estudantes.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `matricula` | String | Número único de matrícula |
| `anoIngresso` | int | Ano de ingresso no curso |

**Métodos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Salva dados acadêmicos do aluno |
| `+historicoAluno()` | void | Gera histórico escolar completo |

**Relacionamentos:**
- **Curso** (N:1): Um aluno pertence a um curso
- **PessoaFisica** (1:1): Cada aluno está associado a uma pessoa física

**Validações:**
- ✅ Matrícula deve ser única
- ✅ Ano de ingresso deve ser válido
- ✅ Deve estar associado a um curso cadastrado

---

### 🔹 Classe: Professor

**Associada a:** PessoaFisica (composição)

**Responsabilidade:** Gerenciar informações funcionais de docentes.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `titulacao` | String | Titulação acadêmica (Graduação, Mestrado, Doutorado, etc.) |

**Métodos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Salva dados do professor |
| `+listarTurmas()` | void | Lista todas as turmas do professor |

**Relacionamentos:**
- **Departamento** (N:1): Um professor pertence a um departamento
- **PessoaFisica** (1:1): Cada professor está associado a uma pessoa física

**Validações:**
- ✅ Titulação deve estar preenchida
- ✅ Deve estar vinculado a um departamento existente

---

### 🔹 Classe: Fornecedor

**Associada a:** PessoaJuridica (composição)

**Responsabilidade:** Gerenciar informações de fornecedores de produtos/serviços.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `ramoAtividade` | String | Área de atuação do fornecedor |
| `contato` | String | Contato comercial principal |

**Métodos:**
| Método | Retorno | Descrição |
|--------|---------|-----------|
| `+salvar()` | void | Salva dados do fornecedor |
| `+gerarRelacaoDePedidos()` | void | Gera relatório de pedidos realizados |

**Relacionamentos:**
- **PessoaJuridica** (1:1): Cada fornecedor está associado a uma pessoa jurídica

**Validações:**
- ✅ Ramo de atividade deve estar preenchido
- ✅ Contato comercial é obrigatório

---

### 🔹 Classe: Departamento

**Classe Independente**

**Responsabilidade:** Organizar professores por áreas de conhecimento.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `nome` | String | Nome do departamento |
| `id` | String | Identificador único |
| `sigla` | String | Sigla do departamento |

**Relacionamentos:**
- **Professor** (1:N): Um departamento possui vários professores

**Validações:**
- ✅ ID deve ser único
- ✅ Sigla deve ter no máximo 5 caracteres

---

### 🔹 Classe: Curso

**Classe Independente**

**Responsabilidade:** Representar cursos oferecidos pela instituição.

**Atributos:**
| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `nome` | String | Nome do curso |
| `id` | String | Identificador único |
| `duracaoSemestres` | int | Duração em semestres |

**Relacionamentos:**
- **Aluno** (1:N): Um curso possui vários alunos matriculados

**Validações:**
- ✅ ID deve ser único
- ✅ Duração deve ser maior que 0

---

## 🎨 Fase 2: Prototipação de Interfaces

Os protótipos foram desenvolvidos utilizando **[Miro]** seguindo a modelagem da Fase 1.

### 1️⃣ Protótipo: Cadastro de Pessoa Física

![Tela - Cadastro Pessoa Física](https://miro.com/app/board/uXjVJsQwh7Y=/?moveToWidget=3458764648130207522&cot=10)

**Campos do Formulário:**
- Nome Completo
- CPF (com máscara: 000.000.000-00)
- RG
- Data de Nascimento
- Endereço Completo (Rua, Número, Bairro, Cidade, Estado, CEP)
- Telefone

---

### 2️⃣ Protótipo: Cadastro de Pessoa Jurídica

![Tela - Cadastro Pessoa Jurídica](https://miro.com/app/board/uXjVJsQwh7Y=/?moveToWidget=3458764648129014779&cot=10)

**Campos do Formulário:**
- Razão Social
- Nome Fantasia
- CNPJ (com máscara: 00.000.000/0000-00)
- Inscrição Estadual
- Endereço Completo
- Telefone Comercial

---

### 3️⃣ Protótipo: Cadastro de Professores

![Tela - Cadastro Professor](https://miro.com/app/board/uXjVJsQwh7Y=/?moveToWidget=3458764648131771369&cot=10)

**Campos do Formulário:**
- Dados Pessoais (herda campos de Pessoa Física)
- Departamento (seleção)
- Titulação (Graduação, Especialização, Mestrado, Doutorado)

---

### 4️⃣ Protótipo: Cadastro de Fornecedores

![Tela - Cadastro Fornecedor](https://miro.com/app/board/uXjVJsQwh7Y=/?moveToWidget=3458764648131397629&cot=10)

**Campos do Formulário:**
- Dados da Empresa (herda campos de Pessoa Jurídica)
- Ramo de atividade
- Contato

---

### 5️⃣ Protótipo: Cadastro de Alunos

![Tela - Cadastro Aluno](https://miro.com/app/board/uXjVJsQwh7Y=/?moveToWidget=3458764648129402283&cot=14)

**Campos do Formulário:**
- Dados Pessoais (herda campos de Pessoa Física)
- Número de Matrícula
- Curso
- Area de ingresso

---

## 📂 Estrutura do Repositório

```
projeto-integrador-poo/
│
├── README.md                          # Documentação principal
│
├── diagramas/                         # Diagramas UML (Fase 1)
│   ├── diagrama-casos-uso.png
│   └── diagrama-classes.png
│
├── prototipos/                        # Protótipos de Interface (Fase 2)
│   ├── cadastro-pessoa-fisica.png
│   ├── cadastro-pessoa-juridica.png
│   ├── cadastro-professores.png
│   ├── cadastro-fornecedores.png
│   └── cadastro-alunos.png
│
└── src/                               # Código-fonte (Fase 3 - Futura)
    ├── Main.java
    ├── model/
    ├── view/
    └── controller/
```

---

## 🛠️ Tecnologias Utilizadas

### Modelagem
- **UML** - Unified Modeling Language
- **Ferramentas:** ...

### Prototipação
- **Miro** - Design de interfaces

### Desenvolvimento (Planejado)
- **Linguagem:** Java
- **Paradigma:** Programação Orientada a Objetos
- **Conceitos aplicados:**
  - Herança e Polimorfismo
  - Encapsulamento
  - Abstração
  - Reutilização de código
  - Validação de dados (CPF, CNPJ, Matrícula)

### Documentação
- **Markdown** - Formatação da documentação
- **GitHub** - Controle de versão e colaboração

---

## 📈 Resultados e Conclusão

O desenvolvimento deste projeto integrador está proporcionando ao grupo:

✅ **Consolidação prática** dos conceitos de POO  
✅ **Experiência** em modelagem UML profissional  
✅ **Habilidades** de análise de requisitos  
✅ **Trabalho colaborativo** com controle de versão (Git/GitHub)  
✅ **Documentação** padronizada segundo normas ABNT  

A aplicação dos conhecimentos teóricos em um projeto real demonstra a relevância da **Engenharia de Software** no desenvolvimento de sistemas robustos e escaláveis.

---

## 📚 Referências Bibliográficas

- BOOCH, G.; RUMBAUGH, J.; JACOBSON, I. **UML: Guia do Usuário.** 2. ed. Rio de Janeiro: Elsevier, 2005.

- SOMMERVILLE, I. **Engenharia de Software.** 10. ed. São Paulo: Pearson, 2019.

- PRESSMAN, R. S.; MAXIM, B. R. **Engenharia de Software: Uma Abordagem Profissional.** 9. ed. Porto Alegre: AMGH, 2016.

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023:** Informação e documentação – Referências – Elaboração. Rio de Janeiro, 2018.

- CENTRO UNIVERSITÁRIO SENAC. **Guia de Normalização de Trabalhos Acadêmicos.** São Paulo: Senac, 2023.

---

<div align="center">

**Centro Universitário Senac**  
Programação Orientada a Objetos | 2025

Feito pelo Grupo 42

</div>
