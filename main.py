from Vision.Vision import exibir_menu, solicitar_tamanho_senha, exibir_senha_gerada,solicitar_salvamento_senha, local_de_salvamento,exibir_lista_senhas, exibir_menu_edicao, solicitar_nome_antigo, solicitar_novo_nome, mensagem_erro
from Controller.Controller import gerarSenhaForte
from Model.Model import PasswordModel
import string

def iniciar():

    db = PasswordModel()
    db.criar_tabela()
    db.testar_conexao()

    while True:
        resposta = exibir_menu()

        match resposta:
            case 1:
                try:
                    print('\n\t --- Gerar Nova Senha ---')
                    tamanhosenha = solicitar_tamanho_senha()
                    novasenhaforte = gerarSenhaForte(tamanhosenha)
                    exibir_senha_gerada(novasenhaforte) #Senha gerada

                    salvarsenha = solicitar_salvamento_senha()
                    localdesalvamento = local_de_salvamento(salvarsenha)

                    if localdesalvamento and localdesalvamento.strip(): #Se a resposta for não retorna uma string vazia, que retorna falsa com o strip()
                        db.inserir_senha(localdesalvamento, novasenhaforte)
                    else:
                        pass

                except ValueError as e:
                    mensagem_erro(str(e))

            case 2:
                print('\n\t --- Visualizar senhas ---')
                tabela = db.visualizar_senhas()
                exibir_lista_senhas(tabela)

            case 3:
                print('\n\t --- Editar Serviços/Senhas ---')
                while True:
                    novaresposta = exibir_menu_edicao()

                    match novaresposta:
                        case 1: # editar nome
                            nome_antigo = solicitar_nome_antigo()
                            novo_nome = solicitar_novo_nome()
                            db.editar_nome(nome_antigo, novo_nome)

                        case 2: # editar senha
                            nome = solicitar_nome_antigo()
                            db.editar_senha(nome) #gera senha automaticamente

                        case 3:
                            break

                        case _:
                            mensagem_erro("Opcao inválida, tente novamente.")
            
            case 4:
                print("Bye Bye...")
                break #Encerra o programa

            case _:
                mensagem_erro("Opcao inválida, tente novamente.")

if __name__ == "__main__":
    iniciar()

