# 🔐 Gerador de Senhas Fortes Integrado

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-MVC-green?style=for-the-badge)

## 📌 Sobre o Projeto
Este é um projeto de estudo focado na criação de um **Gerador de Senhas Seguras** com persistência em banco de dados. O objetivo principal foi aplicar o padrão de arquitetura **MVC (Model-View-Controller)** para separar as responsabilidades do sistema, garantindo um código limpo e escalonável.

O projeto foi desenvolvido enquanto eu revisava conceitos de Python e explorava a integração com bancos de dados relacionais (MySQL).

## 🚀 Funcionalidades
- [x] Geração de senhas aleatórias fortes (letras, números e símbolos).
- [x] Escolha personalizada do tamanho da senha.
- [ ] Integração com MySQL para salvar senhas por serviço (Em desenvolvimento).
- [ ] Interface de usuário via terminal (CLI) organizada.

## 🏗️ Arquitetura do Projeto (MVC)
O projeto está organizado da seguinte forma:

- **Model**: Gerencia a conexão com o MySQL e a persistência dos dados.
- **Vision**: Responsável por toda a interação com o usuário (inputs e displays).
- **Controller**: Contém a lógica de negócio (algoritmo de geração de senha segura usando `secrets`).
- **Main**: Ponto de entrada que orquestra a comunicação entre as camadas.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem Principal:** Python 3.12+
- **Banco de Dados:** MySQL
- **IDE:** VS Code (com extensões Live Server e suporte a Python)

---

## 👨‍💻 Sobre mim
Atualmente sou estudante de **Ciência da Computação na UERJ** (prev. 2027) e estagiário de tecnologia no **TJRJ**. Faço parte do **Grupo de Foguetes do Rio de Janeiro (GFRJ)**, onde aplico tecnologia em projetos de extensão universitária.

### 📚 O que estou aprendendo agora:
<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dotnetcore/dotnetcore-original.svg" alt="dotnet" width="35" height="35"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/haskell/haskell-original.svg" alt="haskell" width="40" height="40"/>
</p>

---

## 🔧 Como Rodar o Projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/JP-rocha23/Gerador-Senha-Forte-Integrado.git](https://github.com/JP-rocha23/Gerador-Senha-Forte-Integrado.git)

---
> [!IMPORTANT]
> **OBS:** Para que o sistema funcione corretamente, é necessário ter o Python instalado e o driver de conexão com o banco de dados. 
> Execute o comando abaixo no seu terminal antes de rodar o `main.py`:
> ```bash
> pip install mysql-connector-python
> ```
