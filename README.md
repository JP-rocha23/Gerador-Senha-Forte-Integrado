# 🔐 Gerador de Senhas Fortes (MVC + MySQL)

Este é um projeto desenvolvido em **Python** que utiliza o padrão de arquitetura **MVC (Model-View-Controller)** para gerenciar e gerar senhas seguras, armazenando-as de forma organizada em um banco de dados **MySQL**.

## 🚀 Funcionalidades

* **Auto-Setup de Banco de Dados:** O sistema verifica e cria o banco de dados (`db_gerador_senhas`) e a tabela (`tb_senhas`) automaticamente na primeira execução.
* **Geração Inteligente:** Cria senhas complexas com base em um tamanho padrão configurável.
* **Gestão de Credenciais:** Permite adicionar, visualizar e editar (nome ou senha) os serviços cadastrados.
* **Segurança:** Implementação de queries parametrizadas para evitar ataques de *SQL Injection*.
* **Tratamento de Dados:** Padronização de strings (`strip` e `lower`) para garantir buscas precisas no banco.

## 🛠️ Pré-requisitos

Antes de rodar o projeto, você precisa ter:

1.  **Python 3.12+** instalado.
2.  **MySQL Server** em execução.
3.  A biblioteca de conexão instalada via terminal:
    ```bash
    pip install mysql-connector-python
    ```

## ⚙️ Configuração Local

Para que o programa se conecte ao seu MySQL, você deve ajustar as credenciais no arquivo `Model.py`:

1.  Abra `Model/Model.py`.
2.  No método `__init__`, localize o dicionário `self.config`.
3.  Insira seu usuário e senha do MySQL:

```python
self.config = {
    'host' : 'localhost',
    'user' : 'seu_usuario',      # Ex: 'root'
    'password' : 'sua_senha',    # Sua senha do MySQL
    'database' : 'db_gerador_senhas'
}
```

## 📂 Estrutura do Código (Arquitetura MVC)

O projeto está organizado seguindo o padrão **Model-View-Controller**, garantindo a separação de responsabilidades e facilitando a manutenção:

* **`Model/PasswordModel.py`**: Camada de persistência. Contém a classe responsável por toda a comunicação com o banco de dados **MySQL**. Realiza operações de `INSERT`, `SELECT` e `UPDATE`, além de gerenciar a criação automática da estrutura do banco.
* **`Controller/`**: Camada lógica. Responsável por importar e executar a função `gerarSenhaForte`, que processa as regras de negócio para a criação de strings aleatórias seguras.
* **`View/`**: Camada de interface. Contém as funções de entrada (`input`) e saída (`print`), gerenciando os menus interativos e a formatação das tabelas de visualização no terminal.
* **`main.py`**: O ponto de entrada (entry point) da aplicação. Orquestra a inicialização do banco de dados e o loop principal do sistema.

---

## 👨‍💻 Créditos e Desenvolvimento

Este projeto foi desenvolvido como parte do portfólio de estudos em **Engenharia de Software** e **Banco de Dados**.

* **Desenvolvedor:** [João Pedro](https://github.com/JP-rocha23)
* **Tecnologias:** Python 3.12, MySQL Server, MySQL Connector.

---