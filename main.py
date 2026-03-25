from Vision.Vision import exibir_menu, solicitar_tamanho_senha, exibir_senha_gerada, mensagem_erro
from Controller.Controller import gerarSenhaForte

def iniciar():
    while True:
        resposta = exibir_menu()

        match resposta:
            case 1:
                try:
                    print('\n\t --- Gerar Nova Senha ---')
                    tamanhosenha = solicitar_tamanho_senha()
                    novasenhaforte = gerarSenhaForte(tamanhosenha)
                    exibir_senha_gerada(novasenhaforte)
                except ValueError:
                    mensagem_erro("Por favor, digite um número inteiro válido.\n")

            case 2:
                print('\n\t --- Visualizar senhas ---')

            case 3:
                print('\n\t --- Editar Senhas ---')

            case 4:
                print("Bye Bye...")
                break #Encerra o programa

            case _:
                mensagem_erro("Opcao inválida, tente novamente.")

if __name__ == "__main__":
    iniciar()

