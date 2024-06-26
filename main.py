usuarios = {
    "Kaiky": "123",
    "Pedro": "321",
    "João": "342"
}


print("Olá. Vamos logar ao sistema.")
print()

username = input("Digite o Usuário: ")
senha = input("Digite a Senha: ")


if username in usuarios and usuarios[username] == senha:
    print("Usuário Logado!")
else:
    print("Não encontrado na base de dados")