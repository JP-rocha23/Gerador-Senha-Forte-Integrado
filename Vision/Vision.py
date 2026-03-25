def exibir_menu():
    print('\n\t --- Gerador de Senhas Fortes ---\n')

    print('O que você deseja fazer?')
    print('[1] Gerar nova senha forte')
    print('[2] Visualizar senhas')
    print('[3] Editar senha')
    print('[4] Sair')
    return int(input("---> "))

def solicitar_tamanho_senha():
    return int(input('Digite o tamanho da senha desejada:'))

def exibir_senha_gerada(senhaforte):
    print(f'Senha forte gerada com sucesso: {senhaforte}')

def mensagem_erro(msg):
    print(f'[ERRO] {msg}')
    

