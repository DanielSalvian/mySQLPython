O projeto apresentado é um sistema simples de gerenciamento de clientes, implementado em Python, que utiliza a biblioteca Tkinter para a interface gráfica e o módulo sqlite3 para manipulação de dados em um banco SQLite. Ele é composto por três módulos principais:

1. aplicacao.py
Esse módulo é responsável por orquestrar a lógica principal da aplicação. Ele conecta os componentes da interface gráfica com a camada de manipulação de dados.

Principais Funcionalidades:

Exibir Clientes: Lista todos os clientes registrados no banco de dados.
Buscar Clientes: Permite filtrar clientes por nome, sobrenome, e-mail ou CPF.
Inserir Clientes: Adiciona novos registros ao banco.
Atualizar Clientes: Edita informações de um cliente selecionado.
Deletar Clientes: Remove o cliente selecionado da base de dados.
Interatividade: O módulo utiliza eventos do Tkinter, como <<ListboxSelect>>, para vincular a seleção de itens no Listbox com a interface, preenchendo automaticamente os campos de entrada.

2. Gui.py
Esse módulo define a interface gráfica do usuário (GUI) da aplicação.

Estrutura da Interface:

Campos de entrada para Nome, Sobrenome, Email e CPF.
Um Listbox para exibição dos clientes cadastrados.
Botões para as operações principais: Ver Todos, Buscar, Inserir, Atualizar, Deletar e Fechar.
Organização Visual: A interface é organizada em um layout de grade (grid), com padding ajustável para uma melhor experiência visual.

Execução: O método run inicia o loop principal da janela, tornando a aplicação interativa.

3. objetodeTransacao.py
Esse módulo implementa a camada de acesso e manipulação de dados, utilizando a biblioteca sqlite3 para interagir com o banco de dados SQLite.

Estrutura do Banco: A tabela clientes armazena informações dos clientes com os campos:

id (chave primária)
nome
sobrenome
email
cpf

Principais Métodos:

initDB(): Cria a tabela clientes caso ainda não exista.
insert(): Adiciona novos registros.
view(): Recupera todos os registros da tabela.
search(): Realiza consultas filtradas por critérios específicos.
delete(): Remove um registro pelo id.
update(): Atualiza um registro existente.
