import mysql.connector
from Controller.Controller import gerarSenhaForte
from typing import Final

class PasswordModel:

    TABELA: Final = "tb_senhas"
    TAMANHO_PADRAO_SENHA: Final = 10

    def __init__(self):
        
        self.config = {
            'host' : 'localhost',
            'user' : 'SEU_USUARIO', # AlTERAR
            'password' : 'SUA_SENHA', # ALTERAR
            'database' : 'db_gerador_senhas'
        }

    def criar_tabela(self):
        
        config_sem_db = self.config.copy()
        if 'database' in config_sem_db:
            del config_sem_db['database'] 
        
        conexao = mysql.connector.connect(**config_sem_db)
        cursor = conexao.cursor()

        # Lista de comandos separados
        comandos = [
            "CREATE DATABASE IF NOT EXISTS db_gerador_senhas;",
            "USE db_gerador_senhas;",
            """
            CREATE TABLE IF NOT EXISTS tb_senhas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_servico VARCHAR(100) NOT NULL,
                senha_gerada VARCHAR(255) NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
        ]

        try:
            for sql in comandos:
                cursor.execute(sql)
            print("--- Banco de dados e tabela verificados com sucesso! ---")
        except mysql.connector.Error as err:
            print(f"Erro ao configurar banco: {err}")
        finally:
            cursor.close()
            conexao.close()


    def testar_conexao(self):
        try:
            conexao = mysql.connector.connect(**self.config)
            if conexao.is_connected():
                print("--- Conexão com o Banco de Dados estabelecida com sucesso! ---")
                conexao.close()
                return True
        
        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")
            return False
            

    def inserir_senha(self, servico, senha):
        try:
            conexao = mysql.connector.connect(**self.config)
            cursor = conexao.cursor()
            
            # %s evita SQL Injection --> Segurança
            comando_sql = "INSERT INTO tb_senhas (nome_servico, senha_gerada) VALUES (%s, %s)"
            dados = (servico, senha)
            
            cursor.execute(comando_sql, dados)
            conexao.commit() # IMPORTANTE: Sem o commit, o MySQL não grava os dados!
            
            print(f"\n[BANCO] Senha para '{servico}' salva com sucesso!")
            
        except mysql.connector.Error as err:
            print(f"\n[ERRO BANCO] Falha ao inserir dados: {err}")

        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
        

    def visualizar_senhas(self):
        try:
            conexao = mysql.connector.connect(**self.config)
            cursor = conexao.cursor(dictionary=True)

            comando_sql = "SELECT * FROM tb_senhas"
            cursor.execute(comando_sql)

            resultados = cursor.fetchall() #recupera todos os registros encontrados
            return resultados
        
        except mysql.connector.Error as err:
            print(f"Erro ao buscar senhas: {err}")
            return []
        
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def editar_nome(self, servico_antigo : str, servico_novo : str):
        antigo_tratado = servico_antigo.strip().lower() #Jogando as strings pra minusculo, pra comparar com o lower no sql
        novo_tratado = servico_novo.strip().lower()

        conexao = mysql.connector.connect(**self.config)
        cursor = conexao.cursor()

        comando_sql = f'UPDATE {self.TABELA} SET nome_servico = %s WHERE LOWER(nome_servico) = LOWER(%s)'
        valores = (novo_tratado, antigo_tratado)

        try:
            cursor.execute(comando_sql, valores)
            conexao.commit() # salvar as alterações no banco
            print(f"Serviço '{servico_antigo}' atualizado para '{servico_novo}' com sucesso!")

        except Exception as e:
            print(f"Erro ao editar: {e}")
            conexao.rollback() # Cancela a operação em caso de erro

        finally:
            cursor.close()
            conexao.close()

    
    def editar_senha(self, nome_servico : str):
        servico_tratado = nome_servico.strip().lower()

        conexao = mysql.connector.connect(**self.config)
        cursor = conexao.cursor()

        try:
            nova_senha = gerarSenhaForte(self.TAMANHO_PADRAO_SENHA)
            comando_sql = f'UPDATE {self.TABELA} SET senha_gerada = %s WHERE LOWER(nome_servico) = LOWER(%s)'
            valores = (nova_senha, servico_tratado)
            cursor.execute(comando_sql, valores)

            if cursor.rowcount() == 0: #Verificando se houve alguma alteração
                print(f"Aviso: Nenhum serviço encontrado com o nome '{nome_servico}'.")
            else:
                conexao.commit() 
                print(f"Senha de '{nome_servico}' atualizado para '{nova_senha}' com sucesso!")

        except Exception as e:
            print(f"Erro ao editar: {e}")
            conexao.rollback()

        finally:
            cursor.close()
            conexao.close()