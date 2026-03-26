import mysql.connector

class PasswordModel:

    def __init__(self):
        
        self.config = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : 'jp2004',
            'database' : 'db_gerador_senhas'
        }


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
    