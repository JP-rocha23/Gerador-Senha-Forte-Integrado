def exibir_menu():
    print('\n\t --- Gerador de Senhas Fortes ---\n')

    print('O que você deseja fazer?')
    print('[1] Gerar nova senha forte')
    print('[2] Visualizar senhas')
    print('[3] Editar serviços/senhas')
    print('[4] Sair')
    resposta = input("---> ")

    if resposta.isdigit():
        return int(resposta)
    return 0

# -----------------------------> Gerar nova senha forte
def solicitar_tamanho_senha():
    return int(input('Digite o tamanho da senha desejada:'))


def exibir_senha_gerada(senhaforte):
    print(f'Senha forte gerada com sucesso: {senhaforte}')


def solicitar_salvamento_senha():
    return str(input('Gostaria de salvar essa senha? [S/N]'))


def local_de_salvamento(resposta : str):
    if resposta.lower().strip() == 's' or resposta.lower().strip() == 'sim':
        return str(input('Qual o nome do app/site em que essa senha será utilizada?'))

    elif resposta.lower() == 'n' or resposta.lower() == 'nao':
        print('Ok, a senha não foi salva.')
        return ''
    
    else:
        mensagem_erro('Resposta inválida, tente novamente.')

# ----------------------------> Visualizar senha
def exibir_lista_senhas(lista_senhas):
    if not lista_senhas:
        print("\n[AVISO] Nenhuma senha cadastrada ainda.")
        return

    print("\n--- SENHAS SALVAS ---")
    print(f"{'ID':<4} | {'SERVIÇO':<20} | {'SENHA':<20}")
    print("-" * 50)
    for s in lista_senhas:
        print(f"{s['id']:<4} | {s['nome_servico']:<20} | {s['senha_gerada']:<20}")

# -------------------------------> Editar senha
def exibir_menu_edicao():
    print('O que você deseja editar?')
    print('[1] Editar Nome')
    print('[2] Editar Senha')
    print('[3] Voltar')
    resposta = input("---> ")

    if resposta.isdigit():
        return int(resposta)
    return 0

def solicitar_nome_antigo():
    return str(input('Qual o nome do servico que você deseja alterar? ')).strip().lower()

def solicitar_novo_nome():
        return str(input('Qual nome que você deseja colocar? ')).strip().lower()

# --------------------------------> Erro
def mensagem_erro(msg):
    print(f'[ERRO] {msg}')
    

