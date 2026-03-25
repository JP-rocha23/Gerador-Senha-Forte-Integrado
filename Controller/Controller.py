import string
import secrets

def gerarSenhaForte(numerodeLetras : int):
    alfabeto = string.ascii_letters + string.digits + string.punctuation #Definindo as possíveis letras

    senhaForte = ''.join(secrets.choice(alfabeto) for i in range(numerodeLetras)) #Gerando cada letra

    return senhaForte

