import string
import secrets

def gerarSenhaForte(numerodeLetras : int):

    if numerodeLetras <= 4:
        raise ValueError('Tamanho de senha inválido, só é possível gerar senhas fortes com pelo menos 5 caracteres.')
    
    alfabeto = string.ascii_letters + string.digits + string.punctuation #Definindo as possíveis letras

    while True:
        senhaForte = ''.join(secrets.choice(alfabeto) for i in range(numerodeLetras)) #Gerando cada letra

        has_maiuscula = any(c.isupper() for c in senhaForte)
        has_minuscula = any(c.islower() for c in senhaForte)
        has_numero = any(c.isdigit() for c in senhaForte)
        has_simbolo = any(c in string.punctuation for c in senhaForte)

        if has_maiuscula and has_minuscula and has_numero and has_simbolo:
            return senhaForte




